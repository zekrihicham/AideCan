from django.forms import ModelForm
from collection_donnees.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#DOCTOR FORM (signup , first page)

class DoctorFrom(ModelForm):

    class Meta:
        model=Doctor
        fields=('specialty','establishment',)
        exclude=('user','photo',)
        widgets = {
            'specialty' : forms.TextInput(attrs={
                'placeholder' : 'Votre Spécialité',

            }),
            'establishment' : forms.TextInput(attrs={
                'placeholder': 'Votre Etablisement',

            })

        }


#SIGNUP FORM (signup , first page)

class signupForm(UserCreationForm):

    class Meta:
        model=User
        fields = ('first_name','last_name','username','email','password1','password2')

        labels={
            'username': 'username',
            'email' : 'email',
            'password1':'password',
            'password2': 'confirm password',
        }
        widgets = {
            'first_name':forms.TextInput(attrs={
                'type': 'text',
                'name': 'first_name',
                'placeholder': 'Votre Nom',

            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'name': 'last_name',
                    'placeholder': 'Votre Prénom',

            }),
            'username': forms.TextInput(attrs={
                'type': 'text',
                'name': 'name',
                'placeholder': 'Choisir un nom d\'utlisateur',

            }),

            'email': forms.EmailInput(attrs={
                'type': 'email',
                'name': 'email',
                'placeholder': 'Votre Email',
            }),
            'password1': forms.PasswordInput(attrs={
                'type': 'password',
                'name': 'psw',
                'placeholder': 'Votre Mot de passe',
            }),
            'password2': forms.PasswordInput(attrs={
                'type': 'password',
                'name': 'psw',
                'placeholder': 'Confirmer votre Mot de passe',

            }),

        }

    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'name': 'psw', 'placeholder': 'Votre Mot de passe'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'name': 'psw', 'placeholder': 'Confirmer votre Mot de passe'})

#DIAGNOSTIC FORM

#TODO:: Model form

#MAMMOGRAFY FORM

#TODO:: Model form







