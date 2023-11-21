from django import forms
from lista.models import Tarefa

class TerefaForm(forms.ModelForm):
    
    class Meta:
        model = Tarefa
        fields = "__all__"
