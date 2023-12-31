from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateUsuario,PerfilUpdate
from django.urls import reverse_lazy

urlpatterns = [
    path(
        'login/', 
        auth_views.LoginView.as_view(template_name='usuarios/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'registrar/',
        CreateUsuario.as_view(),
        name='registrar'
    ),
    path(
        'atualizar-dados/',
        PerfilUpdate.as_view(),
        name='atualizar-dados'
    ),
]
