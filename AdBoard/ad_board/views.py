from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Ad, Response
from .forms import AdForm, ResponseForm


# Create your views here.


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'


class AdsList(ListView):
    model = Ad
    template_name = 'ad_list.html'
        # Это имя списка, в котором будут лежать все объекты
        # для обращения к нему в html-шаблоне.
    context_object_name = 'ad_list'
        # Указываем количество записей на странице
    paginate_by = 10


class AdCreate(LoginRequiredMixin, CreateView):
        # Указываем нашу разработанную форму
    form_class = AdForm
        # модель постов
    model = Ad
        # и новый шаблон, в котором используется форма.
    template_name = 'ad_edit.html'

    def form_valid(self, form):
            # Этот метод вызывается, когда действительные данные формы были отправлены.
            # Он должен вернуть HttpResponse.
        ad = form.save(commit=False)

        form.save()
             # переопределяем файл success_url с путем куда перенаправить запрос после создания
        self.success_url = f"../{str(ad.id)}"


        return super().form_valid(form)


class AdUpdate(LoginRequiredMixin, UpdateView):

    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'
    success_url = '../'


class AdDelete(LoginRequiredMixin, DeleteView):

    model = Ad
    template_name = 'ad_delete.html'

        # прописываем путь в  success_url взяв из пути news или articls
    def dispatch(self, request, *args, **kwargs):
        self.success_url = f"/ads/"
        return super().dispatch(request, *args, **kwargs)

class ResponseCreate(CreateView):

    # Указываем нашу разработанную форму
    form_class = ResponseForm
    # модель постов
    model = Response
    # и новый шаблон, в котором используется форма.
    template_name = 'Response_edit.html'

    def form_valid(self, form):
            # Этот метод вызывается, когда действительные данные формы были отправлены.
            # Он должен вернуть HttpResponse.
        response = form.save(commit=False)
            # устанавливает связ 1 ко многим беря из URL pk Ad.
        response.adRespons = Ad.objects.get(pk=self.kwargs["pk"])

        response.save()
        # переопределяем файл success_url с путем куда перенаправить запрос после создания
        self.success_url = f"/responsesend/"

        return super().form_valid(form)


class ResponseList(ListView):
    model = Response
    template_name = 'response_list.html'
        # Это имя списка, в котором будут лежать все объекты
        # для обращения к нему в html-шаблоне.
    context_object_name = 'response_list'
        # Указываем количество записей на странице
    paginate_by = 10