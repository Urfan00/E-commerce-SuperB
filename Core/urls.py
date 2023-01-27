from django.urls import path
from .views import ContactUsView, FAQView, HomePageView, about_us, error


urlpatterns = [
    path('error/', error, name="error"),
    path('about_us/', about_us, name = "about_us"),
    path('faq/', FAQView.as_view(), name = "faq"),
    path('contact_us/', ContactUsView.as_view(), name = "contact_us"),
    path('', HomePageView.as_view(), name = "index")
]
