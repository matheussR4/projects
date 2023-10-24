from django.contrib import admin
from .models import Genero,Filme, Sessao, Sala,Ingresso,Cliente

# Register your models here.
admin.site.register(Genero)
admin.site.register(Filme)
admin.site.register(Sessao)
admin.site.register(Sala)
admin.site.register(Ingresso)
admin.site.register(Cliente)