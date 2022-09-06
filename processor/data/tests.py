from http import HTTPStatus
from pathlib import Path

import json

from django.test import TestCase
from .rest_service import RestService
from .api_models import GenericData
from .client import ProcessorClient
from .views import FileProcessor

from unittest.mock import patch, MagicMock

rest_service = RestService()
client = ProcessorClient()

class currencyTestCase(TestCase):

    def test_currency_exchange(self):
        """
        """
        start_date = '2020-01-01'
        end_date = '2020-01-31'
        resp = rest_service.convert_currency(
            start_period=start_date,
            end_period=end_date,
            currency_from='ZAR',
            currency_to='EUR')

        assert resp.status_code == 200

        assert str(resp.url) == 'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/D.ZAR.EUR.SP00.A?startPeriod=2020-01-01&endPeriod=2020-01-31'

    def test_currency_exchange_client(self):
        """
        """

        with open("data/response_200.json") as f:
            fake_currency_data =  json.load(f)

        fake_resp = MagicMock()
        fake_resp.json = MagicMock(return_value=fake_currency_data)
        fake_resp.status_code = HTTPStatus.OK

        with patch.object( client, 'convert_currency') as mock:
            client.convert_currency('2020-01-01', '2020-01-02', 'ZAR')
            mock.assert_called()
        breakpoint()

        # assert isinstance(fake_resp.json, GenericData)


    # def test_process_file(self):

    #     file_processor = FileProcessor()

    #     datadir = Path("""./data""")
    #     filename = datadir/"file_to_save.csv"

    #     file_saver = file_processor.processFile(filename)


    def test_retriev_rows(self):

        file_processor = FileProcessor()

        file_saver = file_processor.retrieveRows('ZA', '2020-01-01')


