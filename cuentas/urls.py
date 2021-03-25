from django.urls import path
from .views import ResgistrarView

urlpatterns = [
  path('registrar/', ResgistrarView.as_view(), name='registrar'),
]