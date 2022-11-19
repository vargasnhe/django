#definir rutas q tendra acceso la app


from django.urls import path
from .views import saludar, parametros, PruebaApiView, DepartamentosApiView, DepartamentoDetalleApiView

urlpatterns = [
    path('inicio/', saludar),
    path('parametros/<str:nombre>/', parametros),
    path ('prueba/', PruebaApiView.as_view()),
    path ('departamentos/', DepartamentosApiView.as_view()),
    path ('departamento/<int:pk>/', DepartamentoDetalleApiView.as_view())
]
