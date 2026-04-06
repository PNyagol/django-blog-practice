from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'atugi/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'atugi/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'atugi/article_form.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'atugi/article_form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'atugi/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
