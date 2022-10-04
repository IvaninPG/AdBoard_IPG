from django.urls import path, include

# Импортируем созданное нами представление

from .views import AdsList, AdDetail, AdCreate, AdUpdate, AdDelete

urlpatterns = [

    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.

    path('', AdsList.as_view()),
    path('<int:pk>/', AdDetail.as_view(), name='ad_detail'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/update/', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete')

]