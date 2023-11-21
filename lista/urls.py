from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('newtarefa/', views.newtarefa, name='newtarefa')

]