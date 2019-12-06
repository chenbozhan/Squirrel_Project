# Generated by Django 3.0 on 2019-12-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('Latitude', models.FloatField(help_text='Latitude coordinate for squirrel sighting point')),
                ('Longitude', models.FloatField(help_text='Longitude coordinate for squirrel sighting point')),
                ('Unique_Squirrel_ID', models.CharField(help_text='Identification tag for each squirrel sightings', max_length=30, primary_key=True, serialize=False)),
                ('Shift', models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], help_text='Whether or not the sighting session occurred in the morning or late afternoon', max_length=2)),
                ('Date', models.DateTimeField(help_text='Concatenation of the sighting session day and month.')),
                ('Age', models.CharField(blank=True, help_text='Value is either Adult or Juvenile.', max_length=20, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, help_text='Value is either Gray, Cinnamon or Black.', max_length=20, null=True)),
                ('Location', models.CharField(blank=True, help_text='Value is either Ground Plane or Above Ground. Sighters were instructed to indicate the location of where the squirrel was when first sighted.', max_length=30, null=True)),
                ('Specific_Location', models.CharField(blank=True, help_text='Sighters occasionally added commentary on the squirrel location. These notes are provided here.', max_length=30, null=True)),
                ('Running', models.BooleanField(help_text='Squirrel was seen running.')),
                ('Chasing', models.BooleanField(help_text='Squirrel was seen chasing another squirrel.')),
                ('Climbing', models.BooleanField(help_text='Squirrel was seen climbing a tree or other environmental landmark.')),
                ('Eating', models.BooleanField(help_text='Squirrel was seen eating.')),
                ('Foraging', models.BooleanField(help_text='Squirrel was seen foraging for food.')),
                ('Other_Activities', models.CharField(blank=True, max_length=30, null=True)),
                ('Kuks', models.BooleanField(help_text='Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.')),
                ('Quaas', models.BooleanField(help_text='Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.')),
                ('Moans', models.BooleanField(help_text='Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.')),
                ('Tail_flags', models.BooleanField(help_text="Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air.")),
                ('Tail_twitches', models.BooleanField(help_text='Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.')),
                ('Approaches', models.BooleanField(help_text='Squirrel was seen approaching human, seeking food.')),
                ('Indifferent', models.BooleanField(help_text='Squirrel was indifferent to human presence.')),
                ('Runs_from', models.BooleanField(help_text='Squirrel was seen running from humans, seeing them as a threat.')),
            ],
        ),
    ]
