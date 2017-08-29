from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=60,required=False,help_text="optional")
    last_name=forms.CharField(max_length=60,required=False,help_text="optional")
    email=forms.EmailField(max_length=150,help_text="Required")

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2',)