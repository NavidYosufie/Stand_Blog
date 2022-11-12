from django import forms


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=200, label="your message")