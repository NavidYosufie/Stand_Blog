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
        if User.objects.filter(username__iexact=self.cleaned_data.get("username")).exists():
            raise ValidationError("This username already exists", code="username_exists")
        return self.cleaned_data.get("username")

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data.get("email")).exists():
            raise ValidationError("This email already exists", code="email_exists")
        return self.cleaned_data.get('email')

    def clean_password_1(self):
        if self.cleaned_data.get("password_1") != self.cleaned_data.get("password_2"):
            raise ValidationError("Passwords are not same", code="password_not_same")
        return self.cleaned_data.get("password_1")



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "input100", "placeholder": "Username"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Password"}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get("username"), password=self.cleaned_data.get("password"))
        if user is None:
            raise ValidationError("This username or password are wrong", code="username_or_password_wrong")
        return self.cleaned_data.get("password")



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", 'last_name', "email")