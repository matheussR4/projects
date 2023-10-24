from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
      class Meta:
        model=User
        fields=['username','email','password1','password2']

      def clean_email(self):
         e=self.cleaned_data['email']
         if e:
            if User.objects.filter(email=e).exists():
               raise ValidationError( 'O email {} já possui cadastro.'.format(e))
            return e
