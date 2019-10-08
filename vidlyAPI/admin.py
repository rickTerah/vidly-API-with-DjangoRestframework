from django.contrib import admin
from .models import (
    Genre,
    Movie,
    Customer,
    Rental
)

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Customer)
admin.site.register(Rental)
