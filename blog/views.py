from django.shortcuts import  render, get_object_or_404, redirect
from .models import Post, CategoriaPost
from django.views.generic import DetailView, ListView
from django.http import Http404
# Create your views here.


#________________________________________________________________________

class BlogListView(ListView):

    category = None


    def get_queryset(self):
        queryset = Post.objects.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(CategoriaPost, slug=category_slug)
            queryset = queryset.filter(categoria=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = CategoriaPost.objects.all()
        return context



#________________________________________________________________________


class BlogDetailView(DetailView):
    queryset = Post.objects.all()
    
