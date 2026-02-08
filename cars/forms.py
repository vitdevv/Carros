from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, label='Car Model')
    model_year = forms.IntegerField(label='Manufacturing Year')
    value = forms.DecimalField(max_digits=10, decimal_places=2, label='Price')
    brand = forms.ModelChoiceField(Brand.objects.all(), label='Brand')
    factory_year = forms.IntegerField(label='Factory Year')
    plate = forms.CharField(max_length=20, label='Plate Number')
    photo = forms.ImageField(label='Car Photo')