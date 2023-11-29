from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Tarefa
from .forms import TerefaForm
from django.contrib import messages


# Create your views here.

def lista(request):
    tarefas = Tarefa.objects.all()
    context = {'tarefas' : tarefas}
    return render(request, 'lista/index.html', context)

def vertarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'lista/tarefas.html')


def newtarefa(request):
    if request.method == 'GET':
        form = TerefaForm()
        context = {'form' : form}
        return render(request, 'lista/newtarefa.html', context)
    else:
        form = TerefaForm(request.POST)
        if form.is_valid():
            context = {'form' : form}
            form.save()
            form = TerefaForm()
            return redirect('/')
        else:
          return render(request, 'lista/index.html', context)



def edittarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    form = TerefaForm(instance=tarefa)

    if(request.method == 'POST'):
        form = TerefaForm(request.POST, instance=tarefa)

        if(form.is_valid()):
            form.save()
            form = TerefaForm()
            return redirect('/')
        else:
            return render (request, 'lista/edittarefa.html', {'form': form, 'tarefa': tarefa})

    else:
        return render (request, 'lista/edittarefa.html', {'form': form, 'tarefa': tarefa})



def deteletarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/')
