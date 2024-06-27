from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('users_records', views.users_records, name='users_records'),
]
