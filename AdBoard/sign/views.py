from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from .forms import BaseRegisterForm, UserForm



class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


# Добавляем представление для изменения пользователя.
class UserUpdate(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User
    template_name = 'user_edit.html'

    def my_view(request):
        if not request.user.email.endswith('@example.com'):
            return redirect('/login/?next=%s' % request.path)


