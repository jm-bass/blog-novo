from django.urls import path, include
from . import views

urlpatterns = [
    path('post/<int:post_id>', views.post, name='post'),
    path('post/<int:post_id>/editar', views.editar_post, name='editar_post'),
    path('post/<int:post_id>/deletar', views.deletar_post, name='deletar_post'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('', views.index, name='index'),
    path('mensagem/', views.mensagem, name='mensagem'),
    path('mensagem/<int:mensagem_id>/editar', views.editar_mensagem, name='editar_mensagem'),
    path('mensagem/<int:mensagem_id>/deletar', views.deletar_mensagem, name='deletar_mensagem'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrarpost/', views.cadastrarpost, name='cadastrarpost'),
]