from django.contrib import admin
from .models import Shelters, Reservation, Purchase

admin.site.register(Shelters)
admin.site.register(Reservation)
admin.site.register(Purchase)
