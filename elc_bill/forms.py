
from django import forms
from django.forms import ModelForm
from .models import Details
class DateInput(forms.DateInput):
    input_type = 'date'
class ElcForm(forms.ModelForm):
    CHOICES=[('male','Male'),
         ('female','Female')]
    from_date = forms.DateField(
        widget=DateInput
        )

        
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Details
        fields = ['first_name','gender','address','from_date','state','download_pdf','no_units','price','image']