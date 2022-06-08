"""Module views for listings app."""
from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def band_list(request):
    """Say Hello Django!"""
    
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', { 'bands': bands })

def band_detail(request, band_id):
    """Get a specific band by his given ID."""
    
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', { 'band': band })

def about(request):
    """Page to present us."""

    return render(request, 'listings/about.html', {})

def listing_list(request):
    """Show list of advertisement."""

    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', { 'listings': listings })

def listing_detail(request, listing_id):
    """Get a specific listing."""

    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html', { 'listing': listing })

def contact(request):
    """Page to contact us."""

    return render(request, 'listings/contact.html', {})

def handler500(request):
    """Handle error 500."""
    return render(request, 'listings/error500.html', {})
