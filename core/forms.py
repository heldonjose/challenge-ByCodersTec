from datetime import datetime, timedelta
from time import strftime
from django import forms

from core.models import ImportCNAB


class ImportCNABForm(forms.ModelForm):
    class Meta:
        model = ImportCNAB
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ImportCNABForm, self).__init__(*args, **kwargs)
