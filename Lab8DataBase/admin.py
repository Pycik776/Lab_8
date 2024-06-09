from django.contrib import admin
from .models import Medicines, Suppliers, Supplies

admin.site.register(Medicines)
admin.site.register(Suppliers)
admin.site.register(Supplies)