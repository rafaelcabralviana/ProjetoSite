from django.contrib import admin
from .models import DadosPreAgenda, CadastroConsultas, CadastroProfissional, CadastroEspecialidades, EspecialidadeAgenda, ProfissionalAgenda,ConsultaAgenda 

# Register your models here.



# CADASTRO PROFISSIONAIS E ESPECIALIDADES:
class ProfissionalInline(admin.TabularInline):
    model = CadastroProfissional   
    
class EspecialidadeInline(admin.StackedInline):
    model = CadastroEspecialidades

@admin.register(CadastroConsultas)
class TipoExameAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    inlines = [
        
        ProfissionalInline,
        
    ]

@admin.register(CadastroEspecialidades)
class TipoExameAdmin(admin.ModelAdmin):
    list_display = ["especialidade"]
    filter_horizontal = ["profissional_esp"]
    
#______________________________________


#RECEBIMENTO DE AGENDAMENTOS ______________
class EspecialidadeInline(admin.TabularInline):
    model = EspecialidadeAgenda
    max_num = 1
  

class ProfissionalInline(admin.TabularInline):
    model = ProfissionalAgenda
    max_num = 1

class ConsultaInline(admin.TabularInline):
    model = ConsultaAgenda
    max_num = 1


@admin.register(DadosPreAgenda)
class DadosPreAgendaAdmin(admin.ModelAdmin):
    list_dislay = ['nomecompleto']
    inlines = [
        ConsultaInline,
        ProfissionalInline,
        EspecialidadeInline,

      
    ]


