from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from Blog.models import Blog
from .models import FAQ, ContactUs, Logo
from .forms import ContactUsForm



class HomePageView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()[:2]
        context['logos'] = Logo.objects.all()
        return context


class ContactUsView(LoginRequiredMixin, CreateView):
    template_name = 'contact_us.html'
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your comment has been sent successfully!')
        return redirect('contact_us')


class FAQView(LoginRequiredMixin, ListView):
    template_name = 'faq.html'
    model = FAQ
    context_object_name = 'faqs'


def error(request):
    return render(request, "404error.html")

def about_us(request):
    return render(request, "about_us.html")
