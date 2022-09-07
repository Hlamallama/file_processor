

import datetime
import requests


class RestService():

    def __init__(self):
        self.exchange_rate_url = 'https://sdw-wsrest.ecb.europa.eu/service/'
        self.resource = 'data'
        self.flowRef ='EXR'


    def convert_currency(self, start_period:datetime.date, end_period: datetime.date, currency_from: str, currency_to: str = 'EUR') -> requests.Response:
        """
        Converts currency to EUR.

        param start_period: The start date of the currency rate.
        param end_period: The end date of the currency rate.
        param currency_from: the currency that to change from.
        param currency_to: The currency to change to.
        returns: A Response object.
        """

        key = 'D.'+currency_from+'.'+currency_to+'.SP00.A'

        url = self.exchange_rate_url + self.resource + '/'+ self.flowRef + '/' + key

        param = {
            'startPeriod': start_period,
            'endPeriod': end_period,
        }

        response = requests.get(url=url, params=param)  # type: ignore

        return response