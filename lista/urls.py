from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('tarefas/<int:id>/', views.tarefas, name='vertarefas'),
    path('newtarefa/', views.newtarefa, name='newtarefa'),
    path('edittarefa/<int:id>/', views.edittarefa, name='edittarefa'),
    path('deletetarefa/<int:id>', views.deteletarefa, name='deletetarefa')
]