from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):


	class Meta:
		model = UserProfile
		Fields = ('likes_cheese', 'favourite_hamster_name')

