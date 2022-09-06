
import xmltodict

from .rest_service import RestService
from .api_models import GenericData

rest_service = RestService()

class ProcessorClient():

    def convert_currency(self, start_period, end_period, currency_from, currency_to: str = 'EUR'):
        """
        Converts currency to EUR.

        param request: a HttpRequest object.
        returns json object.
        """

        currency_data =  rest_service.convert_currency(start_period, end_period, currency_from, currency_to)

        currency_dict = xmltodict.parse(currency_data.text)

        generic_data = currency_dict.pop("message:GenericData")

        breakpoint()

        tt = GenericData(**generic_data)

        return tt