from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.models import User,Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil
# Create your views here.


class CreateUsuario(CreateView):
    template_name='cadastros/form.html'
    form_class=UsuarioForm
    success_url=reverse_lazy('login')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Cadastrar Usuário'
        context["titulo"]='Registre-se'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Registrar'
        return context

    def form_valid(self, form):
        grupo=get_object_or_404(Group, name="Cliente")
        url=super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        Perfil.objects.create(usuario=self.object)
        return url

class PerfilUpdate(UpdateView):
    template_name='cadastros/form.html'
    model=Perfil
    fields=['nome_completo','telefone']
    success_url=reverse_lazy('catalogo')

    def get_object(self, queryset=None):
        self.object=get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["titulo"]='Meus Dados Pessoais'
        context["botao"]='Atualizar'
        return context