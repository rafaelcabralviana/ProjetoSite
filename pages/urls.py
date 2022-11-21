from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "pages"

urlpatterns = [
    
    path("", views.bannerView, name='home'),
    path("sobrenos/", views.SobreNosPageView.as_view(), name="sobre"),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)