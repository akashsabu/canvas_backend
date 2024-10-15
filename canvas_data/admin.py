from django.contrib import admin
from .models import CanvasData

# Register your models here.
class CanvasDataAdmin(admin.ModelAdmin):
    list_display = ["title"]

admin.site.register(CanvasData, CanvasDataAdmin)
