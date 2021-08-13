import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from catalog.models import Review

class NewFilmForm(forms.Form):
    title = forms.CharField(max_length=200)

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['film', 'date_watched']
        widgets = {'film': forms.HiddenInput(), 'date_watched': forms.DateInput(attrs={'type': 'date'})}

    def clean_date_watched(self):
        data = self.cleaned_data['date_watched']

        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - in future'))

        return data

class UpdateReviewForm(forms.Form):
    new_date = forms.DateField(initial=datetime.date.today(), widget=widgets.DateInput(attrs={'type': 'date'}))
    review = forms.IntegerField(widget=widgets.HiddenInput)

    def clean_new_date(self):
        data = self.cleaned_data['new_date']

        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - in future'))

        return data