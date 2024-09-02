from django import forms


class PublicKeyForm(forms.Form):
    key = forms.CharField(max_length=50)
