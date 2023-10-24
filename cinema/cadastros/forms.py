from django.forms import Form
from .models import Ingresso

class IngressoForm(Form):
     class Meta:
        model=Ingresso
        fields=['sessao','tipo']