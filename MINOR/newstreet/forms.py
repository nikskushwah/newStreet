from django import forms
from django.contrib.auth.models import User
from newstreet.models import Category, Page, UserProfile,newws
from django.forms import ModelForm, Textarea

from django.core.exceptions import ValidationError

from django_password_strength.widgets import PasswordStrengthInput, PasswordConfirmationInput


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.", min_length = 6)
    """passphrase = forms.CharField(widget=PasswordStrengthInput(), help_text = "Please enter a password.")
    confirm_passphrase = forms.CharField(widget=PasswordConfirmationInput(), help_text = "Please enter a password.")"""
    """if len(password) < 6:
            raise forms.ValidationError("The new password must be at least 6 characters long." )"""
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class newsform(forms.ModelForm):
    news=forms.CharField(widget=forms.Textarea)
    longitude=forms.DecimalField()
    latitude=forms.DecimalField()
    class Meta:
        model = newws
        fields = ('news','longitude','latitude',)
