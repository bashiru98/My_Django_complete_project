from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=500, label="name")
#     email = forms.EmailField(max_length=500, label="email")
#     password1 =forms.CharField(max_length=20)
#     password2 =forms.CharField(max_length=20)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1','password2']

#     def save(self, commit=True):
#         user = super(UserRegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()

#         return user


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, label="Name")
    email = forms.EmailField(max_length=500, label="Email")
    comment = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Enter your comment here'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
