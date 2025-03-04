from django.urls import path
from . import views

urlpatterns = [   
    path('', views.index, name='index'), # website home page
    path('about/', views.about, name='about'), # falcon about page
    path('portal/', views.home, name='home'), # portal home page
    
]