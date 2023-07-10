from django.urls import path
from . import views


urlpatterns = [
    path('', views.calc, name='calc'),
    path('', views.calculations, name='calculations'),

]
