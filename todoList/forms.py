from todoList.models import Atividade
from django import forms

class AtividadeForm(forms.ModelForm):
    # autor = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly': 'True'}))
    class Meta:
        model = Atividade
        fields = ['texto', 'prazo', 'privada']
