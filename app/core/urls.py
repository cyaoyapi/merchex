"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import listings.views as listings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', listings_views.band_list, name='band-list'),
    path('bands/<int:band_id>/', listings_views.band_detail, name='band-detail'),
    path('bands/add/', listings_views.band_create, name='band-create'),
    path('bands/<int:band_id>/change/', listings_views.band_update, name='band-update'),
    path('bands/<int:band_id>/delete/', listings_views.band_delete, name='band-delete'),
    path('listings/', listings_views.listing_list, name='listing-list'),
    path('listings/<int:listing_id>/', listings_views.listing_detail, name='listing-detail'),
    path('listings/add/', listings_views.listing_create, name='listing-create'),
    path('listings/<int:listing_id>/change/', listings_views.listing_update, name='listing-update'),
    path('listings/<int:listing_id>/delete/', listings_views.listing_delete, name='listing-delete'),
    path('about-us/', listings_views.about, name='about'),
    path('contact-us/', listings_views.contact, name='contact'),
    path('sent-message/', listings_views.sent_message, name='sent-message'),
]

# Customised errors pages

handler500 = 'listings.views.handler500'