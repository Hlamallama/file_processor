
import datetime
import xmltodict

from .rest_service import RestService
from .api_models import GenericData

rest_service = RestService()

class ProcessorClient():

    def convert_currency(self, start_period: datetime.date, end_period: datetime.date, currency_from: str, currency_to: str = 'EUR') -> GenericData:
        """
        Converts currency to EUR.

        param start_period: The start date of the currency rate.
        param end_period: The end date of the currency rate.
        param currency_from: the currency that to change from.
        param currency_to: The currency to change to.
        returns: A Generic data object.
        """

        currency_data =  rest_service.convert_currency(
            start_period,  # type: ignore
            end_period,  # type: ignore
            currency_from,
            currency_to
        )

        currency_dict = xmltodict.parse(currency_data.text)

        generic_data = currency_dict.pop("message:GenericData")

        g_data = GenericData(**generic_data)

        return g_data