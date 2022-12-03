from django import forms
from django.core.validators import ValidationError
from . import models
from django.contrib.auth.models import User

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
        model = models.Messege
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Your Title"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter Your Message",
                "style": "max-left: 700px;"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Your Email"
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Your Age"
            }),
            "date": forms.DateTimeInput(attrs={
                "class": "form-control",
            })
        }

