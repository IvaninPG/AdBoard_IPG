from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)              # поле автор со связью 1 to many c моделью User
    dateCreation = models.DateTimeField(auto_now_add=True)                  # поле даты создание с функцией автоматического добавления
    adsCategory = models.ForeignKey(Category, on_delete=models.CASCADE)     # поле автор со связью 1 to many c моделью Category
    title = models.CharField(max_length=128)                                # поле заголовок с ограничением 128 символов
    text = models.TextField()                                               # поле основной статьи

    def __str__(self):
        return '{}. Preview: {}'.format(self.title, str(self.text[0:34]))

class Response(models.Model):
    authorName = models.CharField(max_length=64, unique=True)
    text = models.TextField()  # поле основной статьи
    email = models.EmailField(max_length=64, help_text="Обязательно для заполнения")

