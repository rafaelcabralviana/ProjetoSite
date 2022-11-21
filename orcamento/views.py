from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from orcamento.forms import  Orcamentoform, DadosPreAgenda


# Create your views here.

def form_orcamentoform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Orcamentoform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            form = Orcamentoform()
            # ...
            # redirect to a new URL:
            return render(request, 'orcamento/formulario_orcamento.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Orcamentoform()

    return render(request, 'orcamento/formulario_orcamento.html', {'form': form})

