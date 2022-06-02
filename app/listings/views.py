"""Module views for listings app."""
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def hello(request):
    """Say Hello Django!"""
    
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <h2>List of bands</h2>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    """Page to present us."""

    return HttpResponse('<h1>About Us</h1>')

def listings(request):
    """Show list of advertisement."""

    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Listings</h1>
        <h2>List of listings</h2>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
        </ul>
    """)

def contact(request):
    """Page to contact us."""

    return HttpResponse('<h1>Contact Us</h1>')
