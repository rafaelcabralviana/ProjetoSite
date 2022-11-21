from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "areadeservicos"

urlpatterns = [
    
    path("", views.preagenda_consulta, name="area_home"),
    path("consulta/", views.preagenda_profissional, name="consulta"),
    path("profissional/", views.preagenda_especialidade, name="especialidade"),
    

    
    
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
