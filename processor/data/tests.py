

from django.test import TestCase
from .rest_service import RestService
from .api_models import GenericData
from .client import ProcessorClient

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
        end_date = '2020-01-31'
        resp = client.convert_currency(
            start_period=start_date,
            end_period=end_date,
            currency_from='ZAR',
            currency_to='EUR')

        breakpoint()

        # assert resp.status_code == 200

