# Generated by Django 4.0.2 on 2022-11-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=50)),
                ('ser_contactado', models.BooleanField(default=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Whatsap')),
                ('tipo_pessoa', models.CharField(choices=[('CC', 'Cognitivo Comportamental'), ('CC2', 'Cognitivo Construtivista'), ('GT', 'Gestalt Terapia'), ('P', 'Psicanálise'), ('PA', 'Psicologia Analítica')], max_length=200)),
                ('tipo_servico', models.CharField(choices=[('SC', 'Solcitar Contato'), ('SO', 'Solicitar Orçamento'), ('MEI', 'Abertura Micro empreendedor individual')], max_length=200)),
                ('outros_detalhes', models.TextField(help_text='Detalhar o que não se enquadra nas opções acima.', max_length=1000)),
            ],
        ),
    ]
