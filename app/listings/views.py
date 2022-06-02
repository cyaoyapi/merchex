"""Module views for listings app."""
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    """Say Hello Django!"""

    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    """Page to present us."""

    return HttpResponse('<h1>About Us</h1>')

def listings(request):
    """Show list of advertisement."""

    return HttpResponse('<h1>Listings</h1>')

def contact(request):
    """Page to contact us."""

    return HttpResponse('<h1>Contact Us</h1>')
