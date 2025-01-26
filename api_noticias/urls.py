from django.urls import path
from .views import NoticiaListCreateView, NoticiaDetailView, MemoriaNoticiaListCreateView, MemoriaNoticiaDetailView

urlpatterns = [
    # Endpoints para o banco SQLite
    path('noticias/', NoticiaListCreateView.as_view(), name='noticia-list-sqlite'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detail-sqlite'),

    # Endpoints para o banco de memória
    path('memoria/noticias/', MemoriaNoticiaListCreateView.as_view(), name='noticia-list-memoria'),
    path('memoria/noticias/<str:pk>/', MemoriaNoticiaDetailView.as_view(), name='noticia-detail-memoria'),
]
