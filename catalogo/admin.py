from django.contrib import admin

# Register your models here.


from .models import Category, Product

admin.site.site_header = 'PAINEL ADMIN - VIVER VIBES SAÚDE'
admin.site.site_title = 'VIVER VIBES SAÚDE'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id", "modified"]
    
    
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "image",
        "description",
        "modified",
                   
        

    ]
    #list_editable = ["is_available"]
    search_fields = ["name"]


