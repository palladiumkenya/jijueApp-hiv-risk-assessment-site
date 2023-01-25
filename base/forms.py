from django import forms
from .models import PredictedResult


class DataForm(forms.ModelForm):
    class Meta:
        model = PredictedResult
        fields = ['age', 'gender', 'county', 'maritalStatus', 'coupleDiscordant', 'SexWithWoman', 'SexWithMan', 'condom_use',
                  'sw', 'pwid', 'testedBefore', 'presumedTB', 'treatmentTB', 'sti', 'rapevictim', 'HIVPrEP']
