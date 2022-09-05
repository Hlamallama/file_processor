from django.shortcuts import render

import csv

from .models import FileData

from .client import ProcessorClient

from .api_models import FileRequestData


class FileProcessor():

    def process_file(self, csv_file):
        """"""

        client = ProcessorClient()

        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:

                breakpoint()
                FileRequestData(**row)

                currency = client.convert_currency(
                    start_period=row.date,
                    end_period=row.date,
                    currency_from=row.currency,
                )

                file_data = FileData()
                file_data.date = row
                file_data.country = row
                file_data.purchase = row
                file_data.currency = currency
                file_data.net = row
                file_data.Vat = row

                file_data.save()
