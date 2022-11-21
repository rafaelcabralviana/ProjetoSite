from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator



class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    

    class Meta:
        ordering = ("name",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "CRIAR - Categoria Serviço - Detalhes Site"
        verbose_name_plural = "CRIAR - Categoria Serviço - Detalhes Site"

    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    
    name = models.CharField(max_length=1000)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    

    objects = models.Manager()
    available = AvailableManager()


    class Meta:
        ordering = ("name",)
        verbose_name = "CRIAR - Serviço - Detalhes Site"
        verbose_name_plural = "CRIAR - Serviço - Detalhes Site"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

Product.objects.last
