from django.urls import path
from .views import about_us, contact_us, error, faq, index


urlpatterns = [
    path('error/', error, name="error"),
    path('about_us/', about_us, name = "about_us"),
    path('contact_us/', contact_us, name = "contact_us"),
    path('faq/', faq, name = "faq"),
    path('', index, name = "index")
]