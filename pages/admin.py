from django.contrib import admin
from .models import BannerGrandeInicio, SobreNos

# Register your models here.
@admin.register(BannerGrandeInicio)
class BannerGrandeInicio(admin.ModelAdmin):
    list_display = ["titulo", "image", "descricao", "is_available"]

@admin.register(SobreNos)
class SobreNos(admin.ModelAdmin):
    list_display = ["titulo_sobrenos", "image", "descricao", "is_available"]
    