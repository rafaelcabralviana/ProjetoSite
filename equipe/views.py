from django.shortcuts import  render, get_object_or_404, redirect
from .models import Equipe, Especialidade
from django.views.generic import DetailView, ListView
# Create your views here.

class EquipeListView(ListView):

    category = None


    def get_queryset(self):
        queryset = Equipe.objects.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Especialidade, slug=category_slug)
            queryset = queryset.filter(categoria=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Especialidade.objects.all()
        return context


class EquipeDetailView(DetailView):
    queryset = Equipe.objects.all()
    
