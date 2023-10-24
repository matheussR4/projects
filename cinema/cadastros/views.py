from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.views.generic.list import ListView
from django.views import View
from django.views.generic import DetailView
from .models import Genero,Filme, Sessao, Sala,Ingresso,Cliente
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from .forms import IngressoForm
from django.template import RequestContext

# Create your views here.
class FilmeCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    model = Filme
    group_required=u'Administrador'
    fields = ['titulo', 'sinopse', 'classificacaoIndicativa','ano', 'diretor','duracao', 'genero','poster']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-filme')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Cadastrar Filme'
        context["titulo"]='Cadastrar Filme'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Cadastrar'
        return context
    

class GeneroCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    model = Genero
    group_required=u'Administrador'
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-genero')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Cadastrar Gênero'
        context["titulo"]='Cadastrar Gênero'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Cadastrar'
        return context

class SessaoCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    model = Sessao
    group_required=u'Administrador'
    fields = ['codigo','data', 'horario','filme', 'versao','sala','projecao', 'valor_inteira','valor_meia', 'encerrada']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-sessao')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Cadastrar Sessão'
        context["titulo"]='Cadastrar Sessão'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Cadastrar'
        return context

class SalaCreate(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    model = Sala
    group_required=u'Administrador'
    fields = ['numero', 'tipo','projecao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-sala')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Cadastrar Sala'
        context["titulo"]='Cadastrar Sala'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Cadastrar'
        return context


class IngressoCreate(LoginRequiredMixin,CreateView):
    model = Ingresso
    fields = ['sessao', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ingresso')

    def form_valid(self,form):
        form.instance.comprador=self.request.user
        url=super().form_valid(form)

        return url
    """ def get_queryset(self):
        filme=self.request.GET.get('nome')
        if filme:
            self.object_list=Sessao.objects.filter(filme__icontains=filme)
        else:
            self.object_list=Sessao.objects.all()
        return self.object_list """

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Cadastrar Sala'
        context["titulo"]='Cadastrar Sala'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Comprar'
        return context


class FilmeUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Filme
    group_required=u'Administrador'
    fields = ['titulo','sinopse', 'classificacaoIndicativa','ano', 'diretor','duracao', 'genero','poster']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-filme')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Editar Filme'
        context["titulo"]='Editar Filme'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Atualizar'
        return context


class GeneroUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Genero
    group_required=u'Administrador'
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-genero')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Editar Gênero'
        context["titulo"]='Editar Gênero'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Atualizar'
        return context

class SessaoUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Sessao
    group_required=u'Administrador'
    fields = ['codigo','data', 'horario','filme', 'versao','sala','projecao', 'valor_inteira','valor_meia', 'encerrada']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-sessao')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Editar Sessão'
        context["titulo"]='Editar Sessão'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Atualizar'
        return context

class SalaUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Sala
    group_required=u'Administrador'
    fields = ['numero', 'tipo','projecao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-sala')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Editar Sala'
        context["titulo"]='Editar Sala'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Atualizar'
        return context

class IngressoUpdate(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required=u'Administrador'
    model = Ingresso
    fields = ['sessao', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ingresso')

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context["title"]='Editar Ingresso'
        context["titulo"]='Editar Ingresso'
        context["subtitulo"]='Preencha todos os campos obrigatórios.'
        context["botao"]='Atualizar'
        return context

class FilmeDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Filme
    group_required=u'Administrador'
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-filme')

class GeneroDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Genero
    group_required=u'Administrador'
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-genero')

class SessaoDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Sessao
    group_required=u'Administrador'
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-sessao')

class SalaDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Sala
    group_required=u'Administrador'
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-sala')

class IngressoDelete(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Ingresso
    group_required=u'Administrador'
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-ingresso')

class FilmeList(ListView):
    model = Filme
    template_name = 'cadastros/listas/filme.html'
    success_url = reverse_lazy('login')
    paginate_by=4
    def get_queryset(self):
        titulo=self.request.GET.get('nome')
        if titulo:
            self.object_list=Filme.objects.filter(titulo__icontains=titulo)
        else:
            self.object_list=Filme.objects.all()
        return self.object_list

class FilmeListView(ListView):
    model = Filme
    template_name = 'cadastros/listas/filme.html'
    success_url = reverse_lazy('login')

    """ def get_queryset(self):
        self.object_list=Filme.objects.filter(id=3)
        return self.object_list """

    

class GeneroList(ListView):
    model = Genero
    template_name = 'cadastros/listas/genero.html'
    success_url = reverse_lazy('login')
    paginate_by=10
    def get_queryset(self):
        genero=self.request.GET.get('nome')
        if genero:
            self.object_list=Genero.objects.filter(nome__icontains=genero)
        else:
            self.object_list=Genero.objects.all()
        return self.object_list
class SessaoList(ListView):
    model = Sessao
    template_name = 'cadastros/listas/sessao.html'
    success_url = reverse_lazy('login')
    paginate_by=10
    def get_queryset(self):
        codigo=self.request.GET.get('nome')
        if codigo:
            self.object_list=Sessao.objects.filter(codigo__icontains=codigo)
        else:
            self.object_list=Sessao.objects.all()
        return self.object_list

class SessaoListCliente(ListView):
    model = Sessao
    template_name = 'cadastros/listas/sessoes-disponiveis.html'
    success_url = reverse_lazy('login')
    paginate_by=10
    def get_queryset(self):
        titulo=self.request.GET.get('nome')
        if titulo:
            self.object_list=Sessao.objects.filter(filme__titulo__icontains=titulo)
        else:
            self.object_list=Sessao.objects.all()
        return self.object_list

class SalaList(ListView):
    model = Sala
    template_name = 'cadastros/listas/sala.html'
    success_url = reverse_lazy('login')
    paginate_by=10
    def get_queryset(self):
        numero=self.request.GET.get('nome')
        if numero:
            self.object_list=Sala.objects.filter(numero__icontains=numero)
        else:
            self.object_list=Sala.objects.all()
        return self.object_list

    

class IngressoList(ListView):
    model = Ingresso
    template_name = 'cadastros/listas/ingresso.html'
    success_url = reverse_lazy('login')
    paginate_by=10

    def get_queryset(self):
        filme=self.request.GET.get('nome')
        if filme:
            self.object_list=Ingresso.objects.filter(sessao__filme__titulo__icontains=filme)
            self.object_list=self.object_list.filter(comprador=self.request.user)
        else:
            self.object_list=Ingresso.objects.filter(comprador=self.request.user)
        return self.object_list

class Catalogo(ListView):
    model = Filme
    template_name = 'cadastros/listas/catalogo.html'
    success_url = reverse_lazy('login')
    paginate_by=28

    def get_queryset(self):
        txt_nomefilme=self.request.GET.get('nome')
        if txt_nomefilme:
            self.object_list=Filme.objects.filter(titulo__icontains=txt_nomefilme)
        else:
            self.object_list=Filme.objects.all()
        return self.object_list

    


class FilmeDetail(DetailView):
    model=Filme
    template_name='cadastros/details/detalha-filme.html'

class IngressoDetail(DetailView):
    model=Ingresso
    template_name='cadastros/details/detalha-ingresso.html'