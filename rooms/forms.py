from django import forms
from . import models
from django_countries.fields import CountryField


class SearchForm(forms.Form):

    """form to filter rooms"""

    city = forms.CharField(initial="Anywhere")
    country = CountryField(
        default="PL"
    ).formfield()  # ModelChoiceField can be used as well
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(
        required=False,
        empty_label="Any",
        queryset=models.RoomType.objects.all(),
    )  # not Select!!!

    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)

    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
