import datetime
import typing
from django.core import serializers

import csv

from .models import FileData

from .client import ProcessorClient

from .api_models import FileRequestData


class FileProcessor():
    def __init__(self, client: ProcessorClient):
        self.client = client

    def processFile(self, csv_file):
        """
        Process data from a csv and save into the file data table.

        param: csv_file file to process
        """
        try:
            with open(csv_file, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:

                    start_time = datetime.date.fromisoformat(row[0])
                    end_time = start_time + datetime.timedelta(days=1)
                    currency_from = row[3]

                    currency_data = self.client.convert_currency(
                        start_period=start_time,
                        end_period=end_time,
                        currency_from=currency_from,
                    )

                    ex_rate = currency_data.dataSet.series['generic:Obs']['generic:ObsValue']['@value']

                    file_data = FileData(
                        date=row[0],
                        country= row[1],
                        purchase=row[2],
                        currency =ex_rate,
                        net=int(row[4]),
                        Vat=float(row[5]))

                    FileRequestData(
                        date=file_data.date,
                        country=file_data.country,
                        purchase =file_data.purchase,
                        currency = file_data.currency,
                        net = file_data.net,
                        Vat = file_data.Vat)

                    file_data.save()

                    return True
        except (FileNotFoundError, IOError):
             raise ValueError("File not found")


    def retrieveRows(self, country: str, date: datetime.date) -> typing.Any:
        """
        Retrieve a list of file data.

        param: country: the country to filter bu
        patam: date: the date t filter by.

        returns a QuerySet of File data
        """

        data = FileData.objects.filter(country=country,date=date)

        json_data = serializers.serialize('json', data)

        return json_data

