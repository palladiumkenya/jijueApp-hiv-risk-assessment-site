from django import forms
from .models import PredResults, Message


class DataForm(forms.ModelForm):
    class Meta:
        model = PredResults
        fields = ['age', 'gender', 'county','maritalStatus','coupleDiscordant', 'SexWithWoman', 'SexWithMan', 'condom_use',
     'sw', 'pwid', 'testedBefore', 'presumedTB', 'treatmentTB', 'sti', 'rapevictim', 'HIVPrEP']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'phonenumber']