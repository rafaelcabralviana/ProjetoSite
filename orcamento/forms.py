from django.forms import ModelForm
from orcamento.models import Orcamento
from areadeservicos.models import DadosPreAgenda



class Orcamentoform(ModelForm):
    class Meta:
        model = Orcamento
        fields = ['assunto', 'ser_contactado', 'telefone', 'tipo_pessoa', 'tipo_servico', 'outros_detalhes']

