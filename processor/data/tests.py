import datetime
from http import HTTPStatus
from pathlib import Path

import json

from django.test import TestCase
from .rest_service import RestService
from .api_models import GenericData
from .models import FileData
from .client import ProcessorClient
from .views import FileProcessor

from unittest.mock import patch, MagicMock

rest_service = RestService()
client = ProcessorClient()

class currencyTestCase(TestCase):

    def setUp(self):
        FileData.objects.create(date="2020-01-01", country="ZA", purchase=100, currency=1, net=70, Vat=15.00)
        FileData.objects.create(date="2020-01-03", country="ZA", purchase=100, currency=1, net=70, Vat=15.00)
        FileData.objects.create(date="2020-01-01", country="US", purchase=100, currency=1, net=70, Vat=15.00)

    def test_currency_exchange(self):
        """
        Test the happy path to get the currency works.
        """
        start_date = '2020-01-01'
        end_date = '2020-01-03'
        resp = rest_service.convert_currency(
            start_period=datetime.date.fromisoformat(start_date),
            end_period=datetime.date.fromisoformat(end_date),
            currency_from='ZAR',
            currency_to='EUR')

        assert resp.status_code == 200
        assert str(resp.url) == 'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.ZAR.EUR.SP00.A?startPeriod=2020-01-01&endPeriod=2020-01-03'

    def test_currency_exchange_client(self):
        """
        Test the client can access the rest service.
        """

        c = client.convert_currency(
                '2020-01-01',
                '2020-01-03',
                currency_from="ZAR")

        with open("data/response_200.json") as f:
            fake_currency_data =  json.load(f)

        fake_resp = MagicMock()
        fake_resp.json = MagicMock(return_value=fake_currency_data)
        fake_resp.status_code = HTTPStatus.OK

        start_date = '2020-01-01'
        end_date = '2020-01-03'

        with patch.object( client, 'convert_currency') as mock:
            client.convert_currency(
                start_period=start_date,
                end_period=end_date,
                currency_from='ZAR'
            )
            mock.assert_called()

        # assert isinstance(fake_currency_data, GenericData)


    def test_process_file(self):
        """
        Test the processing of CSV data to the file data table and we can get the currency.
        """

        file_processor = FileProcessor(client)

        datadir = Path("""./data""")
        filename = datadir/"file_to_save.csv"

        resp = file_processor.processFile(filename)

        assert resp is True


    def test_retriev_rows(self):
        """
        Test retrieving file data.
        """

        file_processor = FileProcessor(client)

        resp = file_processor.retrieveRows('ZA', datetime.date.fromisoformat('2020-01-01'))

        assert resp
        assert resp[0].country == 'ZA'
        assert resp[0].date == '2020-01-01'


