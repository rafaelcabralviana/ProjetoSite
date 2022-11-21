from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import BannerGrandeInicio
from django.shortcuts import render
from blog.models import Post
from equipe.models import Equipe
from django.http.response import HttpResponse
from areadeservicos.forms import ConsultaAgendaForm


def bannerView(request):


    banners = BannerGrandeInicio.objects.order_by('id')[:5]
    blogposts = Post.objects.order_by('?')[:9]
    equipes = Equipe.objects.order_by('?')[:9]
    #filtros dinamicoshome
    preagenda = ConsultaAgendaForm(request.GET)

    context = {

        'preagenda': preagenda,
        'banners': banners,
        'blogposts': blogposts,
        'equipes':equipes,
    }
    
    return render(request, 'pages/home.html', context)


class SobreNosPageView(TemplateView):
    template_name = "pages/sobre_nos.html"

#__________________________________________________________

