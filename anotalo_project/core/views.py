from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'core/home.html'

