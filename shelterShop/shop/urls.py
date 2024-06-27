from django.urls import path
from . import views

urlpatterns = [
    path('', views.storage, name='storage'),
    path('cart', views.cart, name='cart'),
    path('delete_reservations/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]
