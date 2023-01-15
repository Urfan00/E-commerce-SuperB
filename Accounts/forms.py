from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : _('Enter your username')
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : _('Password')
            }
        )
    )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : _("Your password")
            }
        ),
        label=_('Password')
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : _("Confirm password")
            }
        ),
        label=_('Confirm Password')
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : _("Enter your first name"),
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : _("Enter your last name")
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : _("Username")
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
        }


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Your E-mail'
            }
        )
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your New Password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your New Password'
            }))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label='Old Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Old Password'
            }))
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your New Password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your New Password'
            }))
