"""Module for models of the app listings."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    """Represent a band, a group of music."""

    class Genre(models.TextChoices):
        """Represent a musical genre."""

        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.CharField("Nom", max_length=100)
    genre = models.CharField("Genre", choices=Genre.choices, max_length=5)
    biography = models.CharField("Biographie", max_length=1000)
    year_formed = models.IntegerField("Année de formation", 
        validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active = models.BooleanField("Toujours actif ?", default=True)
    official_homepage = models.URLField("Page officielle", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    """Represent an advertisement about an article of a group."""

    class TypeOfListing(models.TextChoices):
        """Represent a type of listing."""

        RECORD = 'RC'
        CLOTHING = 'CL'
        POSTER = 'PO'
        MISCELLANEOUS = 'MI'


    title = models.CharField("Titre", max_length=100)
    description = models.CharField("Description", max_length=1000)
    sold = models.BooleanField("Disponible ?", default=True)
    year = models.IntegerField("Année", null=True, blank=True)
    type = models.CharField("Type", choices=TypeOfListing.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
