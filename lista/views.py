from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TerefaForm
from django.contrib import messages

# Create your views here.

# Página principal, listar todas as tarefas com a funçào de buscar

def lista(request):
    search = request.GET.get('search')

    if(search):
        tarefas = Tarefa.objects.filter(tarefa__icontains= search)
    else:
        tarefas = Tarefa.objects.all()
    return render(request, 'lista/index.html', {'tarefas' : tarefas})

# read
def tarefas(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'lista/tarefas.html', {'tarefa' : tarefa})

# criar
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


# update

def edittarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    form = TerefaForm(instance=tarefa)

    if(request.method == 'POST'):
        form = TerefaForm(request.POST, instance=tarefa)

        if(form.is_valid()):
            form.save()
            messages.info(request, 'Tarefa editada com sucesso!')
            form = TerefaForm()
            return redirect('/')
        else:
            return render (request, 'lista/edittarefa.html', {'form': form, 'tarefa': tarefa})

    else:
        return render (request, 'lista/edittarefa.html', {'form': form, 'tarefa': tarefa})


# delete
def deteletarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    tarefa.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/')
