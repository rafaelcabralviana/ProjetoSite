from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import BlogDetailView, BlogListView

app_name = "blog"

urlpatterns = [

   
    path("", BlogListView.as_view(), name="home"),
    #path("<slug>/", BlogDetailView.as_view(), name="artigo"),

    path("<slug:slug>/", BlogDetailView.as_view(), name="artigo"),
    path("blog/<slug:slug>/", BlogListView.as_view(), name="list_by_category"),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)