from datetime import datetime, timedelta
from time import strftime
from django import forms

from core.models import ImportCNAD


class ImportCNADForm(forms.ModelForm):
    class Meta:
        model = ImportCNAD
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ImportCNADForm, self).__init__(*args, **kwargs)
