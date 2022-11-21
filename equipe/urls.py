from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import EquipeDetailView, EquipeListView

app_name = "equipe"

urlpatterns = [

   
    path("", EquipeListView.as_view(), name="home"),
    #path("<slug>/", BlogDetailView.as_view(), name="artigo"),

    path("<slug:slug>/", EquipeDetailView.as_view(), name="pessoa"),
    path("equipe/<slug:slug>/", EquipeListView.as_view(), name="list_by_category"),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)