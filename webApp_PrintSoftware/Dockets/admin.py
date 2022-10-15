from django.contrib import admin
from .models import Client, Contact, Csr, Rep, Docket, Machine, Ink, Proof, Stock, Deposit, Terms
from import_export.admin import ImportExportModelAdmin

@admin.register(Client)
@admin.register(Contact)
@admin.register(Csr)
@admin.register(Rep)
@admin.register(Docket)
@admin.register(Machine)
@admin.register(Ink)
@admin.register(Proof)
@admin.register(Stock)
@admin.register(Deposit)
@admin.register(Terms)
class clientData(ImportExportModelAdmin):
    pass
