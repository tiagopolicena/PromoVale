from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Promocao

class PromocaoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["titulo"]}),
        ("Date information", {"fields": ["data_inicio"]}),
    ]


admin.site.register(Promocao)
