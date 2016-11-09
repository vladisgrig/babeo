from django import forms
from .models import Sertificate

class ActivateSertificateForm(forms.ModelForm):

    class Meta:
        model = Sertificate
        fields = ('number',)
        labels = {'number': ''}
