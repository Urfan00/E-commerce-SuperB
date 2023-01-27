from django import forms
from .models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['created_at']
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'phone' : 'Phone number',
            'address' : 'Address',
            'message' : 'Message'
        }
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your first name",
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your last name"
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your phone number"
                }
            ),
            'address' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 1,
                    'placeholder' :"Write your address"
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 7,
                    'placeholder' :"Write your message"
                }
            ),
        }
