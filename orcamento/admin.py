from django.contrib import admin
from orcamento.models import Orcamento
# Register your models here.

class Orcamentos(admin.ModelAdmin):
    pass
admin.site.register(Orcamento)