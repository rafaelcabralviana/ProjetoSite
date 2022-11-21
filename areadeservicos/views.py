from django.views.generic import TemplateView
from django.shortcuts import render
from django.http.response import HttpResponse
from areadeservicos.forms import ConsultaAgendaForm, DadosPreAgendaForm




#VIEWS FILTROS DINAMICOS
def preagenda_consulta(request):

    form = ConsultaAgendaForm(request.GET)

    #dados pessoais pré agenda:
    dados = DadosPreAgendaForm()
    

    context = {
        "form": form,
        "dados": dados,
    }
    return render(request, "areadeservicos/area_home.html", context)


def preagenda_profissional(request):
    form = ConsultaAgendaForm(request.GET)
    
    return HttpResponse(form["profissional"])


def preagenda_especialidade(request):
    form = ConsultaAgendaForm(request.GET)
    
    return HttpResponse(form["espec"])

#________________________________________________________

