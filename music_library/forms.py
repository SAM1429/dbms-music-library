from django import forms
from django.contrib.auth.forms import UserChangeForm, User

class UpdateProfileForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), required=False)
    password_confirm = forms.CharField(max_length=128, widget=forms.PasswordInput(), required=False)