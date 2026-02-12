from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=100, label='Model')
#     model_year = forms.IntegerField(label='Manufacturing Year')
#     value = forms.DecimalField(max_digits=10, decimal_places=2, label='Price')
#     brand = forms.ModelChoiceField(Brand.objects.all(), label='Brand')
#     factory_year = forms.IntegerField(label='Factory Year')
#     plate = forms.CharField(max_length=20, label='Plate Number')
#     image = forms.ImageField(label='Car Photo')
    
#     def save(self):
#         car = Car(
#             model=self.cleaned_data['model'],
#             brand=self.cleaned_data['brand'],
#             factory_year=self.cleaned_data['factory_year'],
#             model_year=self.cleaned_data['model_year'],
#             plate=self.cleaned_data['plate'],
#             value=self.cleaned_data['value'],
#             image=self.cleaned_data['image']
#         )
#         car.save()
#         return car
    
#Model Form
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__' #'__all__' para incluir todos os campos do modelo Car
        # fields = ['model', 'brand', 'factory_year', 'model_year', 'plate', 'value', 'image'] # para incluir campos específicos
        
    def clean_value(self): # Validação personalizada para o campo 'value'
        value = self.cleaned_data.get('value')
        if value <= 0:
            self.add_error('value', 'O valor deve ser maior que zero.')
        return value