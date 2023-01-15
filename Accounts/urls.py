from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView
from .views import ChangePasswordView, CustomLogInView, RegisterView, ResetPasswordConfirmView, ResetPasswordView, account_information, activate, address_book, contact_information


urlpatterns = [
    path('login/', CustomLogInView.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(), name = 'logout'),

    path('register/', RegisterView.as_view(), name = "register"),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),

    path('reset_password/', ResetPasswordView.as_view(), name = 'reset_password'),
    path('reset_password_confirm/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='password/reset_password_complete.html'),name='reset_password_complete'),

    path('change_password/', ChangePasswordView.as_view(), name = 'change_password'),


    path('account_information/', account_information, name = "account_information"),
    path('address_book/', address_book, name = "address_book"),
    path('contact_information/', contact_information, name = "contact_information"),
]
