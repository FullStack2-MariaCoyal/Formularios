from django.urls import path
from .views import DetalleListView, DetalleDetailView, notaCreateView, notaUpdateView, notaDeleteView

urlpatterns = [
    path('nota/<int:pk>/eliminar', notaDeleteView.as_view(), name='notaEliminar'),
    path('nota/<int:pk>/editar', notaUpdateView.as_view(), name='notaEditar'),
    path('nota/Nueva/', notaCreateView.as_view(), name='notaNueva'),
    path('nota/<int:pk>/', DetalleDetailView.as_view(), name='detalleDetalle'),
    path('', DetalleListView.as_view(), name='home')
]