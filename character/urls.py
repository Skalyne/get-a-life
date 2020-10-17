from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = "home"),
    path('create-character/', views.AddCharacterView.as_view(), name= 'create_character'),
    
]