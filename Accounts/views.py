from django.shortcuts import render, redirect
from .models import User
from .forms import AccountInforrmationForm, ChangePasswordForm, CustomSetPasswordForm, LoginForm, RegistrationForm, ResetPasswordForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.contrib import messages
from SuperB.settings import EMAIL_HOST_USER



class CustomLogInView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            subject = 'Activate your account'
            current_site = get_current_site(request)
            message = render_to_string('email/confirmation_email.html', {
                'user' : user,
                'domain': current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user)
            })
            from_email = EMAIL_HOST_USER
            to_email = request.POST['email']
            send_mail(subject, message, from_email, [to_email, ])

            return redirect('login')
        return render(request, self.template_name, {'form':form})


def activate(requset, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(requset, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        messages.error(requset, 'Your session is expired')
        return redirect('/')


class ResetPasswordView(PasswordResetView):
    template_name = 'password/forgot_password.html'
    form_class = ResetPasswordForm
    email_template_name = 'password/reset_password_email.html'
    subject_template_name = 'password/reset_password_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      "If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='password/reset_password_confirm.html'
    form_class=CustomSetPasswordForm
    success_url = reverse_lazy('reset_password_complete')


class ChangePasswordView(PasswordChangeView):
    template_name='password/change_password.html'
    form_class= ChangePasswordForm
    success_url = reverse_lazy('login')



# *******************************************************************************

class AccountInformationView(LoginRequiredMixin, CreateView):
    template_name = 'account_information.html'

    def get(self, request, *args, **kwargs):
        form = AccountInforrmationForm(instance=request.user)
        return render(request, 'account_information.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AccountInforrmationForm(request.POST)

        if form.is_valid():
            user_account = User.objects.get(pk=request.user.pk)
            user_account.first_name = form.cleaned_data.get('first_name')
            user_account.last_name = form.cleaned_data.get('last_name')
            user_account.username = form.cleaned_data.get('username')
            user_account.email = form.cleaned_data.get('email')
            user_account.save()
            messages.success(request, 'Your profile is updated')
            return redirect('account_information')
        else:
            messages.error(request, 'Your profile is not updated')
            return redirect('account_information')
