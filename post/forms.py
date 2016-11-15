from django import forms


class SimpleForm(forms.Form):

    name = forms.CharField()
