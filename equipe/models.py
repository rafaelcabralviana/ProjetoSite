from django.db import models
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.

class Especialidade(models.Model):
    categoria = models.CharField(max_length=200, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="categoria")

    class Meta:
        verbose_name = "CRIAR - Especialidade"
        verbose_name_plural = "CRIAR - Especialidade"
    
    def __str__(self):
        return self.categoria
    def get_absolute_url(self):
        return reverse("equipe:list_by_category", kwargs={"slug": self.slug})



class Equipe(models.Model):
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, null=False)
    nome = models.CharField(max_length=200, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    frase = models.CharField(max_length=500, null=False, blank=True)
    descricao = RichTextUploadingField(null=False, blank=True)

    image = models.ImageField(upload_to="equipe/%Y/%m/%d", blank=False)

    def imagem_equipe(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>Sem imagem</p>')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "CRIAR - Membro da Equipe"
        verbose_name_plural = "CRIAR - Membro da Equipe"

    def get_absolute_url(self):
        return reverse("equipe:pessoa", kwargs={"slug": self.slug})
# Create your models here.
