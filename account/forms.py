from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "input100 mt-", "placeholder": "Enter your username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "input100", "placeholder": "Enter Your Email"}))
    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Enter Your Password"}))
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Enter َAgain Your Password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("This email already exists", code="email_exist")
        return email

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        if password_1 != password_2:
            raise ValidationError("this password not the same", code="password_same")
        return password_2




class LoginForm (forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "input100"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': "input100"}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get("username"), password=self.cleaned_data.get("password"))
        if user is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("this username or password are wrong", code="invalid_info")

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", 'last_name', "email")