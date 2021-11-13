from todoList.models import Tarefa
from django import forms

class TarefaForm(forms.ModelForm):
    # autor = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly': 'True'}))
    class Meta:
        model = Tarefa
        fields = ['texto', 'prazo', 'privada']
