from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register', views.register, name='register'),
    path('changePassword', views.change_password, name='changePassword'),
    path('user_payment', views.user_payment, name='userPayment'),
    path('payment_succed', views.payment_succed),
]
