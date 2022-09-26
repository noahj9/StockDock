from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Client(models.Model): #database table to hold all client names
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Contact(models.Model): #for contact names, each contact belongs to a client, each client can have >1 contact
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    client = models.ForeignKey(Client, null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Csr(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Rep(models.Model):
    name = models.CharField(max_length=100)
    csr = models.ForeignKey(Csr, null = True, on_delete=models.SET_NULL) #foreign key means each rep can have a CSR, null means it isnt mandatory, on delete will set value to null instead of deletion
    def __str__(self):
        return self.name    


class Docket(models.Model): #contains all the data for a docket to be stored in the database
    customer_name = models.ForeignKey(Client, null = True, on_delete=models.SET_NULL)
    date = models.DateField(default=datetime.date.today) #custom field form widgets
    date_required = models.DateField()
    contact = models.ForeignKey(Contact, null = True, on_delete=models.SET_NULL)
    account = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    terms = models.CharField(max_length = 100)
    customer_PO = models.CharField(max_length = 100)
    quote = models.CharField(max_length=100, null=True)
    deposit = models.CharField(max_length = 100)
    deposit_amount = models.CharField(max_length=100, blank=True, null=True)
    rep = models.ForeignKey(Rep, null = True, on_delete=models.SET_NULL)
    csr = models.ForeignKey(Csr, null = True, on_delete=models.SET_NULL)
    quantity_1 = models.CharField(max_length = 100)
    description_1 = models.CharField(max_length = 100)
    finished_size_1 = models.CharField(max_length = 100)
    stock_1 = models.CharField(max_length = 100)
    machine_1 = models.CharField(max_length = 100)
    run_quantity_1 = models.CharField(max_length = 100)
    sheet_size_1 = models.CharField(max_length = 100)
    run_size_1 = models.CharField(max_length = 100)
    proof_1 = models.CharField(max_length = 100)
    inks_1 = models.CharField(max_length = 100)
    instructions_1 = models.TextField(blank=True)
    bindery_1 = models.CharField(max_length = 100)
    file_1 = models.CharField(max_length = 100)
    price_comission_1 = models.CharField(max_length = 100)
    shipping_1 = models.CharField(max_length = 100)

    def __int__(self):
        return self.id


class Machine(models.Model):
    name = models.CharField(max_length=100)
    ink = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Ink(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Proof(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
