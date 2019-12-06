from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    AM = 'AM'
    PM = 'PM'
    Shift_Choices = (
            (AM, 'am'),
            (PM, 'pm'),
     )
    # Add characteristics of Squirrel

    Latitude = models.FloatField(
            help_text=_('Latitude coordinate for squirrel sighting point'),
     )
    
    Longitude = models.FloatField(
            help_text=_('Longitude coordinate for squirrel sighting point'),
     )

    Unique_Squirrel_ID = models.CharField(
            help_text=_('Identification tag for each squirrel sightings'),
            max_length=30,
            primary_key=True,
     )

    Shift = models.CharField(
            help_text=_('Whether or not the sighting session occurred in the morning or late afternoon'),
            max_length=2,
            choices=Shift_Choices,
     )

    Date = models.DateTimeField(
            help_text=_('Concatenation of the sighting session day and month.'),
     )

    Age = models.CharField(
            help_text=_('Value is either Adult or Juvenile.'),
            max_length=20,
            blank=True,
            null=True,
     )

    Primary_Fur_Color = models.CharField(
            help_text=_('Value is either Gray, Cinnamon or Black.'),
            max_length=20,
            blank=True,
            null=True,
     )

    Location = models.CharField(
            help_text=_('Value is either Ground Plane or Above Ground. Sighters were instructed to indicate the location of where the squirrel was when first sighted.'),
            max_length=30,
            blank=True,
            null=True,
     )
    Specific_Location = models.CharField(
            help_text=_('Sighters occasionally added commentary on the squirrel location. These notes are provided here.'),
            max_length=30,
            blank=True,
            null=True,
     )

    Running = models.BooleanField(
            help_text=_('Squirrel was seen running.'),
     )

    Chasing = models.BooleanField(
            help_text=_('Squirrel was seen chasing another squirrel.'),
     )

    Climbing = models.BooleanField(
            help_text=_('Squirrel was seen climbing a tree or other environmental landmark.'),
     )

    Eating = models.BooleanField(
            help_text=_('Squirrel was seen eating.'),
     )

    Foraging = models.BooleanField(
            help_text=_('Squirrel was seen foraging for food.'),
     )
    Other_Activities = models.CharField(
            max_length=30,
            blank=True,
            null=True,
     )
    Kuks = models.BooleanField(
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'),
     )
  
    Quaas = models.BooleanField(
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.'),
     )
    
    Moans = models.BooleanField(
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.'),
     )
    
    Tail_flags = models.BooleanField(
            help_text=_("Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air."),
     )
    
    Tail_twitches = models.BooleanField(
            help_text=_('Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.'),
     )

    Approaches = models.BooleanField(
            help_text=_('Squirrel was seen approaching human, seeking food.'),
     )
    
    Indifferent = models.BooleanField(
            help_text=_('Squirrel was indifferent to human presence.'),
     )
    
    Runs_from = models.BooleanField(
            help_text=_('Squirrel was seen running from humans, seeing them as a threat.'),
     )


