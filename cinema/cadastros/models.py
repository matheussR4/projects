from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Genero(models.Model):
    nome=models.CharField(max_length=100,verbose_name='Nome')
    descricao=models.TextField(verbose_name="Descrição")
    def __str__(self):
        return "{}".format(self.nome)

class Filme(models.Model):
    titulo = models.CharField(max_length=100,verbose_name="Título")
    sinopse= models.TextField(verbose_name="Sinopse")
    classificacaoIndicativa = models.IntegerField(verbose_name='Classificação Indicativa')
    ano=models.CharField(max_length=100,verbose_name="Ano")
    diretor=models.CharField(max_length=100,verbose_name="Diretor")
    duracao=models.CharField(max_length=100,verbose_name="Duração")
    genero=models.ForeignKey(Genero,on_delete=models.PROTECT)
    poster=models.ImageField(upload_to='img/')

    def __str__(self):
        return "{}".format(self.titulo)

    def get_absolute_url(self):
        return reverse('detalhar-filme', args=[str(self.id)])


PROJECAO=[
    ('2D','2D'),
    ('3D','3D'),
]

class Sala(models.Model):
    numero = models.IntegerField()
    tipo=models.CharField(max_length=30,verbose_name='Tipo de sala')
    projecao = models.CharField(max_length=2,verbose_name='Projeção',choices=PROJECAO)

    def __str__(self):
        return "{}-{}".format(self.numero,self.projecao)

VERSAO=[
    ('Dublado','Dublado'),
    ('Legendado','Legendado'),
]

ENCERRADA=[
    (True,'Sim'),
    (False,'Não'),
]

class Sessao(models.Model):
    codigo=models.CharField(max_length=5,verbose_name="Codigo")
    data = models.DateField(verbose_name="Data")
    horario = models.TimeField(verbose_name='Horário')
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT)
    versao=models.CharField(max_length=20,verbose_name="Versão",choices=VERSAO)
    sala=models.ForeignKey(Sala, on_delete=models.PROTECT)
    projecao=models.CharField(max_length=2,verbose_name='Projeção',choices=PROJECAO)
    valor_inteira=models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Valor da Inteira")
    valor_meia=models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Valor da Meia")
    encerrada=models.BooleanField(verbose_name="Encerrada",choices=ENCERRADA)

    def __str__(self):
        return "{}-{}".format(self.codigo,self.horario)
   

class Cliente(models.Model):
    nome=models.CharField(max_length=100,verbose_name="Nome")
    idade=models.IntegerField(verbose_name="Idade")


TIPO=[
    ('Inteira','Inteira'),
    ('Meia-entrada','Meia-entrada'),
]

OCUPADO=[
    (True,"Sim"),
    (False,"Não")
]

""" class Assento(models.Model):
    numero=models.IntegerField()
    sala=models.ForeignKey(Sala,on_delete=models.PROTECT)
    sessao=models.ForeignKey(Sessao,on_delete=models.PROTECT)
    ocupado=models.BooleanField(verbose_name="Ocupado",choices=OCUPADO)
 """

class Ingresso(models.Model):
    sessao = models.ForeignKey(Sessao,on_delete=models.PROTECT)
    tipo=models.CharField(max_length=100,verbose_name='Tipo',choices=TIPO)
    comprador=models.ForeignKey(User,on_delete=models.PROTECT,default='')
    """ comprador=models.ForeignKey(Cliente,on_delete=models.PROTECT) """
    """ assento=models.ForeignKey(Assento,on_delete=models.PROTECT) """





