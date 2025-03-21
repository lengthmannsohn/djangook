from django.urls import path
from hospitales import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamentosBBDD, name='departamentos'),
    path('hospitales/', views.hospitalesBBDD, name='hospitales'),
    path('insertardept/', views.insertarDepartamento, name='insertardept'),
    path('eliminardept/', views.eliminarDepartamento, name="eliminardept"),
    path('modificardept/', views.modificarDepartamento, name="modificardept"),
    path('detallesdept/', views.detallesDepartamento, name="detallesdept"),
    path('empleadosdept/', views.empleadosDepartamento, name="empleadosdept")
]
