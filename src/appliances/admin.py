from django.contrib import admin
from .models import Appliance


@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacture_name', 'model_number', 'created_at', 'updated_at')
    search_fields = ('name', 'manufacture_name', 'model_number')
    list_filter = ('manufacture_name', 'created_at')