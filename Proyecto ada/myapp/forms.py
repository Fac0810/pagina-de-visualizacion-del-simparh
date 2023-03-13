from django import forms
from models import Asunto
from phonenumber_field.formfields import PhoneNumberField

class formularioContacto(forms.Form):

    asunto = forms.ModelChoiceField(queryset=None)
    nombre = forms.CharField()
    localidad = forms.CharField()
    partido = forms.CharField()
    email = forms.EmailField()
    telefono = PhoneNumberField()
    mensaje =forms.TextInput()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asunto'].queryset = Asunto.objects.all()