from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='pro_index'),
    path('internal', views.internal, name='internal')
]