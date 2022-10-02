from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Ad


class AdForm(forms.ModelForm):
   text = forms.TextInput()

   class Meta:
       model = Post
       fields = [
           'author',
           'adsCategory',
           'title',
           'text',
       ]

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       title = cleaned_data.get("title")

       if title == text:
           raise ValidationError(
               "Текст не должен быть идентичен заголовку."
           )

       return cleaned_data\