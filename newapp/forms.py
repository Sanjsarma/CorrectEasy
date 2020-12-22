from django import forms

class NameForm(forms.Form):
    marks = forms.IntegerField(label='mark')