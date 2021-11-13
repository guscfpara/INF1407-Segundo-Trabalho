from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Atividade(models.Model):
    # nickname = models.CharField(max_length=30, help_text="entre com o seu nickname")
    autor = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    texto = models.CharField(max_length=200,help_text="digite o titulo da atividade")
    prazo = models.DateField(help_text="digite a data da entrega(YYYY-MM-DD)")
    privada = models.BooleanField(default=False)
