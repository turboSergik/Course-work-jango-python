from django import forms
from .models import *


class EditForm(forms.ModelForm):

    class Meta:
        model = Edit
        exclude = [""]