from django.db import models


class Medicines(models.Model):
    medicine_registration_number = models.IntegerField(primary_key=True)
    medicine_name = models.CharField(max_length=255)
    manufacture_date = models.DateField()
    shelf_life_days = models.IntegerField()
    medicine_group = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prescription_required = models.BooleanField()


class Suppliers(models.Model):
    supplier_code = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.CharField(max_length=255)
    supplier_phone = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=255)
    location = models.CharField(max_length=50)


class Supplies(models.Model):
    supply_code = models.IntegerField(primary_key=True)
    supply_date = models.DateField()
    medicine_registration_number = models.IntegerField()
    quantity_supplied = models.IntegerField()
    supplier_code = models.IntegerField()

    # Определяем внешние ключи
    medicine = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
