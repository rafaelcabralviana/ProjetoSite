from django.forms import ModelForm
from django import forms
from .models import ConsultaAgenda, ProfissionalAgenda, DadosPreAgenda, CadastroEspecialidades, CadastroConsultas, CadastroProfissional
from dynamic_forms import DynamicField, DynamicFormMixin

#FILTROS DINAMICOS
class ConsultaAgendaForm(DynamicFormMixin, forms.Form):
    def espec_choices(form):
        queryset = form["consulta"].value()
        
        return CadastroProfissional.objects.filter(consulta=queryset)
        
    #def initial_profissional(form):
        #queryset = form['consulta'].value()
        
        #return CadastroProfissional.objects.filter(consulta=queryset)

    def prof_spec_choices(form):
        queryset = form["profissional"].value()
        
        return CadastroEspecialidades.objects.filter(profissional_esp=queryset)


    consulta = forms.ModelChoiceField(
        queryset=CadastroConsultas.objects.all(),
        #initial=CadastroConsultas.objects.first(),
        
        
    )

    especialidade = forms.ModelChoiceField(
        queryset=CadastroEspecialidades.objects.all(),
        #initial=CadastroEspecialidades.objects.first(),
        
    )

    profissional = DynamicField(
        forms.ModelChoiceField,
        queryset=espec_choices,
        #initial=initial_profissional,
    )


    espec = DynamicField(
        forms.ModelChoiceField,
        queryset=prof_spec_choices,
        #initial=initial_profissional,
    )
##FILTROS DINAMICOS FIM___________________________________________

class DadosPreAgendaForm(ModelForm):
    class Meta:
        model = DadosPreAgenda
        fields = "__all__"
        