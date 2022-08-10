from django.contrib import admin
from .models import clients
from import_export.admin import ImportExportModelAdmin

@admin.register(clients)
class clientData(ImportExportModelAdmin):
    pass
