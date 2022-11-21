from django.db import models
from autoslug import AutoSlugField
# Create your models here.

#cadastro consultas/ especialidades /profissionais
class CadastroConsultas(models.Model):
    consulta = models.CharField(max_length=100)

    def __str__(self):
        return str(self.consulta)
    class Meta:
        verbose_name = "CRIAR Especialidades e Profissionais - PréAgendamento"
        verbose_name_plural = "CRIAR Especialidade e Profissionais - PréAgendamento"

class CadastroProfissional(models.Model):
    profissional = models.CharField(max_length=100)
    consulta = models.ForeignKey(CadastroConsultas, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return str(self.profissional)

class CadastroEspecialidades(models.Model):
    especialidade = models.CharField(max_length=100)
    profissional_esp = models.ManyToManyField(CadastroProfissional, blank=True)
    
    def __str__(self):
        return str(self.especialidade)

    class Meta:
        verbose_name = "CRIAR Tipo de Atendimento - PréAgendamento"
        verbose_name_plural = "CRIAR Tipos de Atendimentos - PréAgendamento"
# _______

#Formularios DADOS de préagendamento :
class TipoPreAgenda(models.Model):
    pass

class DadosPreAgenda(models.Model):
    nomecompleto = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nomecompleto")
    email = models.EmailField(null=False)
    tel = models.CharField(max_length=11, null=False)
    dtnascimento = models.DateField(null=False)
    obs = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.nomecompleto)
    
    class Meta:
        verbose_name = "CAIXA DE ENTRADA - PréAgendamento"
        verbose_name_plural = "CAIXA DE ENTRADA - Pré-Agendamento"
    
#________________________________________________

#Formularios CONSULTAS de préagendamento :
class ConsultaAgenda(models.Model):
    
    dadosagenda = models.ForeignKey(DadosPreAgenda, on_delete=models.CASCADE, null=False)
    agenda_consulta = models.ForeignKey(CadastroConsultas, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return str(self.dadosagenda)

class ProfissionalAgenda(models.Model):
    dadosagenda = models.ForeignKey(DadosPreAgenda, on_delete=models.CASCADE, null=False)
    agenda_profissional = models.ForeignKey(CadastroProfissional, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.agenda_profissional)


class EspecialidadeAgenda(models.Model):
    dadosagenda = models.ForeignKey(DadosPreAgenda, on_delete=models.CASCADE, null=False)
    agenda_especialidade = models.ForeignKey(CadastroEspecialidades, on_delete=models.CASCADE, null=False)
    anexo = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return str(self.agenda_especialidade)

#________________________________________________