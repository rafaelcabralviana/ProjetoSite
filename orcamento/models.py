from django.db import models

# Create your models here.

TIPO_PESSOA_CHOICES = (
    ('CC', 'Cognitivo Comportamental'),
    ('CC2', 'Cognitivo Construtivista'),
    ('GT', 'Gestalt Terapia'),
    ('P', 'Psicanálise'),
    ('PA', 'Psicologia Analítica')
)
TIPO_SERVICOS_CHOICES = (
    ('SC', 'Solcitar Contato'),
    ('SO', 'Solicitar Orçamento'),
    ('MEI', 'Abertura Micro empreendedor individual')

)


class Orcamento(models.Model):
    assunto = models.CharField(max_length=50, null=False)
    ser_contactado = models.BooleanField(default=True)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Whatsap')
    tipo_pessoa = models.CharField(max_length= 200, choices=TIPO_PESSOA_CHOICES)
    tipo_servico = models.CharField(max_length=200, choices=TIPO_SERVICOS_CHOICES)
    outros_detalhes = models.TextField(max_length=1000, help_text='Detalhar o que não se enquadra nas opções acima.')


    def __str__(self):
        return self.assunto