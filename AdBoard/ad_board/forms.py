from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import admin

from .models import Ad


class AdForm(forms.ModelForm):

    content = RichTextUploadingFormField(config_name='default')

    class Meta:
        model = Ad
        fields = [
            'author',
            'adsCategory',
            'title',
            'content',
             ]

