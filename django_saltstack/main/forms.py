# coding=utf-8

from django import forms


class KeyForm(forms.Form):
    key = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
