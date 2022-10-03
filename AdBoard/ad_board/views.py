from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Ad
from .forms import AdForm
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


class AdCreate(CreateView):
        # Указываем нашу разработанную форму
    form_class = AdForm
        # модель постов
    model = Ad
        # и новый шаблон, в котором используется форма.
    template_name = 'ad_edit.html'
