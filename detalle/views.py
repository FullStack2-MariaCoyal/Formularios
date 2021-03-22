from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
class DetalleListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'Blogs'

class DetalleDetailView(DetailView):
    model = Post
    template_name = "detalleDetalle.html"
    context_object_name = 'Blogs'

class notaCreateView(CreateView): 
    model = Post
    template_name = 'notaNueva.html'
    fields = '__all__'

class notaUpdateView(UpdateView):
    model = Post
    template_name = 'notaEditar.html'
    fields = ['titulo', 'Resumen']

class notaDeleteView(DeleteView):
    model = Post
    template_name = 'notaEliminar.html'
    context_object_name = 'Blogs'
    success_url = reverse_lazy('home')