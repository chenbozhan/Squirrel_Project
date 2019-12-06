import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
from datetime import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            L = [
            item['Running'],
            item['Chasing'],
            item['Climbing'],
            item['Eating'],
            item['Foraging'],
            item['Kuks'],
            item['Quaas'],
            item['Moans'],
            item['Tail flags'],
            item['Tail twitches'],
            item['Approaches'],
            item['Indifferent'],
            item['Runs from']
        ]
            for i in range(len(L)):
                if L[i] in ('FALSE', 'false'):
                    L[i] = False
                elif L[i] in ('TRUE', 'true'):
                    L[i] = True

            s = Squirrel(
                Latitude=item['Y'],
                Longitude=item['X'],
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Shift=item['Shift'],
                Date=datetime.strptime(item['Date'], '%m%d%Y'),
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=L[0],
                Chasing=L[1],
                Climbing=L[2],
                Eating=L[3],
                Foraging=L[4],
                Other_Activities=item['Other Activities'],
                Kuks=L[5],
                Quaas=L[6],
                Moans=L[7],
                Tail_flags=L[8],
                Tail_twitches=L[9],
                Approaches=L[10],
                Indifferent=L[11],
                Runs_from=L[12],
            )
            s.save() 
