from django.db import models


# Create your models here.
class Tarefa(models.Model):
    tarefa = models.CharField(max_length=200)
    data = models.DateField(null=True, blank= True)
    hora = models.TimeField(null=True, blank= True)


    def __str__(self):
        return self.tarefa