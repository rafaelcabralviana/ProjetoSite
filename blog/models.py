from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.
class CategoriaPost(models.Model):
    nome = models.CharField(max_length=200, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("blog:list_by_category", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "CRIAR - Categoria Artigo"
        verbose_name_plural = "CRIAR - Categoria Artigo"
    

class Post(models.Model):
    categoria = models.ForeignKey(CategoriaPost, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    titulo = models.CharField(max_length=200, null=False)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="titulo")
    subtitulo = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="blog/%Y/%m/%d", blank=False)
    texto = RichTextUploadingField()

    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
        
    def imagem_post(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>Sem imagem</p>')

    
    def get_absolute_url(self):
        return reverse("blog:artigo", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "CRIAR - Artigo"
        verbose_name_plural = "CRIAR - Artigo"