import datetime
from django.shortcuts import render

import csv

from .models import FileData

from .client import ProcessorClient

from .api_models import FileRequestData

import xml.etree.ElementTree as ET


class FileProcessor():
    def __init__(self):
        pass

    def processFile(self, csv_file):
        """"""

        client = ProcessorClient()

        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:

                #TODO change therow to dict

                startTime = datetime.date.fromisoformat(row[0])
                endTime = startTime + datetime.timedelta(days=1)
                currencyFrom = row[3]

                currency_data = client.convert_currency(
                    start_period=startTime,
                    end_period=endTime,
                    currency_from=currencyFrom,
                )

                ex_rate = currency_data['message:DataSet']['generic:Series']['generic:Series']['generic:ObsValue']['@value']


                # FileRequestData(**file_data)

                file_data = FileData(
                    date= row[0],
                    country = row[1], 
                    purchase = row[2],
                    currency = ex_rate,
                    net = int(row[4]),
                    Vat = float(row[5]))

                file_data.save()


    def retrieveRows(self, country, date):
        """
        """

        data = FileData.objects.filter(country=country,date=date)

        return data

