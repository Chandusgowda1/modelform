from django import forms
from app.models import emp

class empform(forms.ModelForm):
    class Meta:
        model=emp
        fields='__all__'