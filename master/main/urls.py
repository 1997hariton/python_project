from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('price/', views.price, name = 'price'),
    path('work/', views.work, name = 'work'),
]

