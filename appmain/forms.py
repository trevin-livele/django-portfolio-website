from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import MailingList



class MailingListForm(forms.ModelForm):
    class Meta:
        model = MailingList
        fields = ['email']