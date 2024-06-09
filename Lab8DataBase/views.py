from django.shortcuts import render
from .models import Medicines, Suppliers, Supplies

def all_tables(request):
    medicines = Medicines.objects.all()
    suppliers = Suppliers.objects.all()
    supplies = Supplies.objects.all()
    return render(request, 'all_tables.html', {'medicines': medicines, 'suppliers': suppliers, 'supplies': supplies})
