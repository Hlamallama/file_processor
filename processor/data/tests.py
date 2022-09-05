from http import HTTPStatus
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

        start_date = '2020-01-01'
        end_date = '2020-01-03'
        resp = client.convert_currency(
            start_period=start_date,
            end_period=end_date,
            currency_from='ZAR',
            currency_to='EUR')

        with open("data/response_200.json") as f:
            fake_currency_data =  json.load(f)

        fake_resp = MagicMock()
        fake_resp.json = MagicMock(return_value=fake_currency_data)
        fake_resp.status_code = HTTPStatus.OK


        start_date = '2020-01-01'
        end_date = '2020-01-31'
        resp = client.convert_currency(
            start_period=start_date,
            end_period=end_date,
            currency_from='ZAR',
            currency_to='EUR')

        assert resp


    def test_process_file(self):

        file_processor = FileProcessor()

        from pathlib import Path

        datadir = Path("""/data""")
        fale_to_save = datadir/"file_to_save.csv"

        file_saver = file_processor.process_file(fale_to_save)


