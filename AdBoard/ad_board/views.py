from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ad
# Create your views here.


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'


class AdsList(ListView):
    model = Ad
    template_name = 'ads.html'
        # Это имя списка, в котором будут лежать все объекты
        # для обращения к нему в html-шаблоне.
    context_object_name = 'ads'
        # Указываем количество записей на странице
    paginate_by = 10