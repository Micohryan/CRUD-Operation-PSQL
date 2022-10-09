from socket import fromshare
from django import forms 
from CRUD.models import EmpModel

class empForms(forms.ModelForm):
    class Meta:
        model = EmpModel
        fields = "__all__"

