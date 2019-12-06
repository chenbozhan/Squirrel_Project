import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        with open(options['csv_file'],'w') as fp:
            writer = csv.writer(fp)
            header = [
            'Latitude',
            'Longitude',
            'Unique_Squirrel_ID',
            'Shift',
            'Date',
            'Age',
            'Primary_Fur_Color',
            'Location',
            'Specific_Location',
            'Running',
            'Chasing',
            'Climbing',
            'Eating',
            'Foraging',
            'Other_Activities',
            'Kuks',
            'Quaas',
            'Moans',
            'Tail_flags',
            'Tail_twitches',
            'Approaches',
            'Indifferent',
            'Runs_from',
        ]
            writer.writerow(header)
            
            for i in Squirrel.objects.all():
                data = [ 
                       i.Latitude,
                       i.Longitude,
                       i.Unique_Squirrel_ID,
                       i.Shift,
                       i.Date,
                       i.Age,
                       i.Primary_Fur_Color,
                       i.Location,
                       i.Specific_Location,
                       i.Running,
                       i.Chasing,
                       i.Climbing,
                       i.Eating,
                       i.Foraging,
                       i.Other_Activities,
                       i.Kuks,
                       i.Quaas,
                       i.Moans,
                       i.Tail_flags,
                       i.Tail_twitches,
                       i.Approaches,
                       i.Indifferent,
                       i.Runs_from
            ]
                writer.writerow(data)
