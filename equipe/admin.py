from django.contrib import admin
from .models import Especialidade, Equipe
# Register your models here.
# Register your models here.
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ["categoria"]
    
    
class EquipeAdmin(admin.ModelAdmin):
    list_display = ["nome", "especialidade", "image"]

    list_filter = ["especialidade"]

admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Equipe, EquipeAdmin)