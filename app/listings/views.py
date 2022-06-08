"""Module views for listings app."""
from django.http import HttpResponse
from django.shortcuts import render, redirect

from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm

def band_list(request):
    """Say Hello Django!"""
    
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', { 'bands': bands })

def band_detail(request, band_id):
    """Get a specific band by his given ID."""
    
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', { 'band': band })

def band_create(request):
    """Add new band."""
    
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', { 'form': form })

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

def listing_create(request):
    """Create new listing."""

    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', { 'form': form })

def contact(request):
    """Page to contact us."""

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(f"Message sent from {form.cleaned_data['name']}!")
            return redirect('sent-message')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', { 'form': form })

def handler500(request):
    """Handle error 500."""
    return render(request, 'listings/error500.html', {})

def sent_message(request):
    """Confirm the sending of a message."""

    return HttpResponse("<p>Votre message a bien été envoyé. Merci.</p>")

