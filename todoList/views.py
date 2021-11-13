from django.shortcuts import render
from todoList.models import Atividade
from todoList.forms import AtividadeForm
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TodoListView(View):
    def get(self,request,*args, **kwargs):
        todos = Atividade.objects.filter(privada=False)
        context = {'todos': todos, 'minhasAtividades': False }
        return render(request, 'todoList/listaTodo.html', context)

@login_required()
def minhasAtividades(request):

    todosAutor = Atividade.objects.filter(autor=request.user).values()
    todosAutor = list(todosAutor)
    data = {
        'data': todosAutor,
    }
    return JsonResponse(data,)

class AuthorListView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        todosAutor = Atividade.objects.filter(autor=request.user)
        context = {'todos': todosAutor, 'minhasAtividades': True  }
        return render(request, 'todoList/listaTodo.html', context)

class TodoCreateView(LoginRequiredMixin, View):
    def get(self,request,*args, **kwargs):
        context = {'formulario': AtividadeForm, }
        return render(request, 'todoList/criaTodo.html', context)


    def post(self,request,*args, **kwargs):
        formulario = AtividadeForm(data=request.POST,initial={'autor': request.user.username})
        print(formulario,formulario.is_valid())
        #formulario = dados do POST
        if formulario.is_valid():

            todo = formulario.save()
            todo.autor = request.user
            #salvar no banco
            todo.save()
            #redirecionar para outro view
            return HttpResponseRedirect(reverse_lazy('todoList:lista-todo'))
        else:
            return HttpResponseRedirect(reverse_lazy('todoList:cria-todo'))

class TodoUpdateView(View):

    def get(self,request,pk,*args, **kwargs):
        todo = Atividade.objects.get(pk=pk)
        formulario = AtividadeForm(instance=todo)
        context = {'todo': formulario, }
        return render(request, 'todoList/atualizaTodo.html', context)

    def post(self,request,pk,*args, **kwargs):
        todo = get_object_or_404(Atividade, pk=pk)
        formulario = AtividadeForm(request.POST, instance=todo)

        if formulario.is_valid():
            print('form up')
            todo = formulario.save()
            todo.autor = request.user
            todo.save()
            return HttpResponseRedirect(reverse_lazy('todoList:lista-todo'))
        else:
            context = {'todo': formulario, }
            return render(request, 'todoList/atualizaTodo.html', context)


class TodoDeleteView(View):
    def get(self,request,pk,*args, **kwargs):
        todo = Atividade.objects.get(pk=pk)
        context = {'todo': todo, }
        return render(request, 'todoList/apagaTodo.html',context)

    def post (self,request,pk,*args, **kwargs):
        todo = Atividade.objects.get(pk=pk)
        todo.delete()
        print("Removendo o Todo", pk)
        return HttpResponseRedirect(reverse_lazy("todoList:lista-todo"))
