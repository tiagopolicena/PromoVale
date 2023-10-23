from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('registro/', views.cadastro, name='registro'),
    path('registrar/', views.cadastrar, name='registrar'),
    path('perfil/', views.perfil, name='perfil'),    
    path('login/', views.fazer_login, name='login'),   
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
    

    ]
urlpatterns += staticfiles_urlpatterns()
