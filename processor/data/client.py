

import json
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

        data_dict = xmltodict.parse(currency_data.text)

        generic_data = data_dict.pop("message:GenericData")


        g = GenericData(**generic_data)

        breakpoint()


        # return json_data.json()