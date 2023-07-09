from django.urls import path
from . import views


urlpatterns = [
    path('', views.calc, name='calc'),
    path('calculations', views.calculations, name='process'),

]
