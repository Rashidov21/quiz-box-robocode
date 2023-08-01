from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Quiz


class HomePageView(ListView):
    template_name = "index.html"
    model = Quiz