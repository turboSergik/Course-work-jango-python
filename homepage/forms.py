# -*- coding: utf8 -*-

from django import forms
from .models import *


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        exclude = [""]
