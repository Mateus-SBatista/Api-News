from django.urls import path
from .views import NoticiaListCreateView, NoticiaDetailView, MemoriaNoticiaListCreateView, MemoriaNoticiaDetailView

urlpatterns = [
    # Endpoints para o banco SQLite
    path('api_noticias/', NoticiaListCreateView.as_view(), name='noticia-list-sqlite'),
    path('api_noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detail-sqlite'),

    # Endpoints para o banco de memória
    path('memoria/api_noticias/', MemoriaNoticiaListCreateView.as_view(), name='noticia-list-memoria'),
    path('memoria/api_noticias/<str:pk>/', MemoriaNoticiaDetailView.as_view(), name='noticia-detail-memoria'),
]
