from django.contrib import admin
from .models import CategoriaPost, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome", "criado_em", "editado_em", "slug"]
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "categoria", "user", "editado_em", "imagem_post"]
    readonly_fields = ['imagem_post']
    list_filter = ["categoria"]

admin.site.register(CategoriaPost, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
     