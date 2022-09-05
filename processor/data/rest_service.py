
from urllib import response

import requests


class RestService():

    def __init__(self):
        self.exchange_rate_url = 'https://sdw-wsrest.ecb.europa.eu/service/'
        self.resource = 'data'
        self.flowRef ='EXR'


    def convert_currency(self, start_period, end_period, currency_from, currency_to: str = 'EUR'):
        """
        Converts currency to EUR.

        param request: a HttpRequest object.
        returns a HttpResponse object.
        """
        key = 'D.'+currency_from+'.'+currency_to+'.SP00.A'

        url = self.exchange_rate_url + self.resource + '/'+ self.flowRef + '/' + key

        param = {
            'startPeriod': start_period,
            'endPeriod': end_period,
        }

        response = requests.get(url=url, params=param)

        return response




    country_currency_mapping = {
        'USD': 'US dollar',
        'JPY': 'Japanese yen',
        'BGN': 'Bulgarian lev',
        'CZK': 'Czech koruna',
        'DKK': 'Danish krone',
        'GBP': 'Pound sterling',
        'HUF': 'Hungarian forint',
        'PLN': 'Polish zloty',
        'RON': 'Romanian leu',
        'SEK': 'Swedish krona',
        'CHF': 'Swiss franc',
        'ISK': 'Icelandic krona',
        'NOK': 'Norwegian krone',
        'HRK': 'Croatian kuna',
        'RUB': 'Russian rouble',
        'TRY': 'Turkish lira',
        'AUD': 'Australian dollar',
        'BRL': 'Brazilian real',
        'CAD': 'Canadian dollar',
        'CNY': 'Chinese yuan renminbi',
        'HKD': 'Hong Kong dollar',
        'IDR': 'Indonesian rupiah',
        'ILS': 'Israeli shekel',
        'INR': 'Indian rupee',
        'KRW': 'South Korean won',
        'MXN': 'Mexican peso',
        'MYR': 'Malaysian ringgit',
        'NZD': 'New Zealand dollar',
        'PHP': 'Philippine piso',
        'SGD': 'Singapore dollar',
        'THB': 'Thai baht',
        'ZAR': 'South African rand',
    }