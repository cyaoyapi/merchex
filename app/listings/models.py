"""Module for models of the app listings."""
from django.db import models

class Band(models.Model):
    """Represent a band, a group of music."""

    name = models.CharField("Nom", max_length=100)


class Listing(models.Model):
    """Represent an advertisement about an article of a group."""

    title = models.CharField("Titre", max_length=100)
