from django.conf.urls import url, include
from calculadora import views

urlpatterns = [
    url(r'^calcular', views.calcular, name='calculadora/calcular'),
    url(r'^/', views.index, name='calculadora/index'),
]
