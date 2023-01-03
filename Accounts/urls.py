from django.urls import path
from .views import account_information, address_book, contact_information, forgot_password, login, register


urlpatterns = [
    path('account_information/', account_information, name = "account_information"),
    path('address_book/', address_book, name = "address_book"),
    path('contact_information/', contact_information, name = "contact_information"),
    path('forgot_password/', forgot_password, name = "forgot_password"),
    path('login/', login, name = "login"),
    path('register/', register, name = "register"),
]
