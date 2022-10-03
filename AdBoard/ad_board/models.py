from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)              # поле автор со связью 1 to many c моделью User
    dateCreation = models.DateTimeField(auto_now_add=True)                  # поле даты создание с функцией автоматического добавления
    adsCategory = models.ForeignKey(Category, on_delete=models.CASCADE)     # поле автор со связью 1 to many c моделью Category
    title = models.CharField(max_length=128)                               # поле заголовок с ограничением 128 символов
    content = RichTextUploadingField(config_name='default')


    def __str__(self):
        return '{}'.format(self.title)


class Response(models.Model):
    adRespons = models.ForeignKey(Ad, on_delete=models.CASCADE)
    authorName = models.CharField(max_length=64, unique=True)
    text = models.TextField()  # поле основной статьи
    email = models.EmailField(max_length=64, help_text="Обязательно для заполнения")

