from django import forms
from systems.models import contact

class contactForm (forms.ModelForm):

    class Meta:
        model = contact
        fields = ['first_name','last_name','email','phone','message']
