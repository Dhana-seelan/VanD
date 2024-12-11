# import_excel_data.py

from django.core.management.base import BaseCommand
import pandas as pd
from vehicle.models import Location

class Command(BaseCommand):
    help = 'Import data from Excel file into the Django database'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        
        # Read Excel file
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to read Excel file: {e}"))
            return

        # Iterate over rows and create Location instances
        for index, row in df.iterrows():
            location = Location(
                name=row['Name'],
                latitude=row['Latitude'],
                longitude=row['Longitude'],
                address=row['Address']
            )
            location.save()

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))
