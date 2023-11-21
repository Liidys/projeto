from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa
from .forms import TerefaForm


# Create your views here.

def lista(request):
    tarefas = Tarefa.objects.all()
    context = {'tarefas' : tarefas}
    return render(request, 'index.html', context)


def newtarefa(request):
    if request.method == 'GET':
        form = TerefaForm()
        context = {'form' : form}
        return render(request, 'newtarefa.html', context)
    else:
        form = TerefaForm(request.POST)
        if form.is_valid():
            context = {'form' : form}
            form.save()
            form = TerefaForm()
            return redirect('/')
        else:
          context = {'form' : form}
          return render(request, 'index.html', context)
        

    
