"""Module to define forms for the app listings."""

from django import forms

from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    """Contact us form."""

    name = forms.CharField(required=False)
    email = forms.EmailField()
    object = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class BandForm(forms.ModelForm):
    """Forms related to model Band."""

    class Meta:
        model = Band
        fields = '__all__'


class ListingForm(forms.ModelForm):
    """Forms related to model Listing."""

    class Meta:
        model = Listing
        exclude = ('sold', )
