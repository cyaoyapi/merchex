"""Module views for listings app."""
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def hello(request):
    """Say Hello Django!"""
    
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', { 'bands': bands })

def about(request):
    """Page to present us."""

    return render(request, 'listings/about.html', {})

def listings(request):
    """Show list of advertisement."""

    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', { 'listings': listings })

def contact(request):
    """Page to contact us."""

    return render(request, 'listings/contact.html', {})
