from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "orcamento"

urlpatterns = [
    path("", views.form_orcamentoform, name="form_orcamentoform"),


] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
