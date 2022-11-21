from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)

class BannerGrandeInicio(TimeStampedModel):
    titulo = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to="banners/%Y/%m/%d", blank=False)
    descricao = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Banner Página inicial"
        verbose_name_plural = "Banners Página inicial"
    
    def __str__(self):
        return self.titulo

class SobreNos(TimeStampedModel):
    titulo_sobrenos = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="banners/%Y/%m/%d", blank=False)
    descricao = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Página Sobre"
        verbose_name_plural = "Informações Página Sobrenós"
    
    def __str__(self):
        return self.titulo_sobrenos
