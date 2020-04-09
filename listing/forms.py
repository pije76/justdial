from django import forms

from ajax_select.fields import AutoCompleteSelectMultipleField

import autocomplete_light

from .models import *


class CityForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=autocomplete.ModelSelect2(url='your_country_auto_url'),)
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=autocomplete.ModelSelect2(url='your_city_auto_url', forward=['country']))

    class Meta:
        model = Listing
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('city')
        widgets = {
            'city': autocomplete_light.TextWidget(CityAutocomplete, autocomplete_js_attributes={'placeholder': 'City, Country', 'minimum_characters': 4})
        }


class SettingsForm(SettingsFormBase):
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthdate = forms.DateField(widget=SelectDateWidget(years=range(1898, 2014)))
    sex = forms.ChoiceField(choices=AGE_CHOICES, widget=RadioSelect())
    city = forms.CharField()  # I think, I need improve this line, add custom widget or/and field


class DocumentForm(ModelForm):
    class Meta:
        model = Document

    tags = AutoCompleteSelectMultipleField('tags')
