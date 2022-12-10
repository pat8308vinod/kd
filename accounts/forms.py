from dataclasses import fields
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):  
    email = forms.EmailField(label='Email',widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=('first_name','last_name','email','password1','password2'  )
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user( 
            self.cleaned_data['first_name'],  
            self.cleaned_data['last_name'],                              
            self.cleaned_data['email'],  
            self.cleaned_data['password1']          
        )  
        return user  
