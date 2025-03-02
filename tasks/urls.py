from django.urls import path
from . import views
urlpatterns = [
     path('', views.home, name='home'),
    path('tasks/', views.index, name='index'),
    path('tasks/about/', views.about, name='about'),
    path('tasks/login/', views.login, name='login'),
   
]