from django.urls import path, include
from . import views

urlpatterns = [
    path('post/<int:post_id>', views.post, name='post'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('', views.index, name='index')
]
