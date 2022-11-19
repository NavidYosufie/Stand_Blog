from mailbox import Message

from django import forms
from django.core.validators import ValidationError

class ContactUsForm(forms.Form):
    FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black")
    ]
    name = forms.CharField(max_length=10, min_length=6, label="your name:")
    text = forms.CharField(max_length=10, label="your message:")
    birth_year = forms.DateField(required=True, widget=forms.SelectDateWidget(attrs={"class": "form-control"}))
    colors = forms.ChoiceField(widget=forms.RadioSelect(), choices=FAVORITE_COLORS_CHOICES)

    def clean(self):
        name = self.cleaned_data.get("name")
        text = self.cleaned_data.get("text")
        if name == text:
            raise ValidationError("name and text are same", code="name_text_same")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "--__all__"

