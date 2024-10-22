from django.urls import path
from materia_app import views
urlpatterns = [
    path("",views.inicio_vistia,name="views.inicio_vistia")
]
