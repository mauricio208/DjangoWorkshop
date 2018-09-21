from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'graphmaker'
urlpatterns = [
    path('', views.Graph.as_view(), name='graph'),
    path('add-node', views.addNode, name="add-node"),
    path('move-node', views.moveNode, name="move-node"),
]