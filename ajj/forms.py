from .models import Registration
from django import forms

class RegistrationForm(forms.ModelForm):
    # first_name = forms.TextInput()
    # last_name = forms.TextInput()
    # phone = forms.IntegerField()
    # your_interest = forms.Select()
    email = forms.EmailField(label='Email ID')
    class Meta:
        model = Registration
        fields = ['first_name','last_name','email','phone','your_interest']
     