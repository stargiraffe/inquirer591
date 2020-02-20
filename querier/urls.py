from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='querier-home'),
    path('about/', views.about, name='querier-about'),
]
