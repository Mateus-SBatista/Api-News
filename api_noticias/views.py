from rest_framework import generics
from .models import Noticia
from .serializers import NoticiaSerializer, MemoriaNoticiaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from django.http import Http404
from .memoria import (
    adicionar_noticia,
    editar_noticia,
    listar_noticia,
    listar_todas_noticias,
    remover_noticia
)

class NoticiaListCreateView(generics.ListCreateAPIView):
    queryset = Noticia.objects.filter(ativo=True)  # Apenas notícias ativas
    serializer_class = NoticiaSerializer

class NoticiaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()  # Para incluir todas as notícias, ativas ou inativas
    serializer_class = NoticiaSerializer

    # Sobrescreve o método delete
    def delete(self, request, pk=None):
        noticia = self.get_object()

        # Exclui permanentemente a notícia
        noticia.delete()
        return Response(
            {"detail": "Notícia excluída permanentemente."},
            status=status.HTTP_204_NO_CONTENT
        )

    # Sobrescreve o método de atualização
    def update(self, request, *args, **kwargs):
        noticia = self.get_object()

        # Atualiza a notícia, se o campo ativo for False, não exclui, apenas marca como inativa
        if 'ativo' in request.data and request.data['ativo'] is False:
            # Apenas marca como inativa, sem excluir do banco de dados
            noticia.ativo = False
            noticia.save()
            return Response(
                {"detail": "Notícia marcada como inativa."},
                status=status.HTTP_200_OK
            )

        # Caso contrário, aplica a atualização normal
        return super().update(request, *args, **kwargs)

    

class MemoriaNoticiaListCreateView(ListCreateAPIView):
    serializer_class = MemoriaNoticiaSerializer

    def get_queryset(self):
        # Retorna apenas as notícias ativas do banco de memória
        todas_noticias = listar_todas_noticias()
        noticias_ativas = [noticia for noticia in todas_noticias if noticia.get('publicado', True)]
        return noticias_ativas

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Cria notícia no banco de memória
        noticia = adicionar_noticia(
            titulo=serializer.validated_data['titulo'],
            conteudo=serializer.validated_data['conteudo'],
            publicado=serializer.validated_data.get('publicado', True),
            autor=serializer.validated_data['autor'],
        )

        return Response(noticia, status=status.HTTP_201_CREATED)



class MemoriaNoticiaDetailView(RetrieveUpdateAPIView):
    serializer_class = MemoriaNoticiaSerializer

    def get_object(self):
        pk = int(self.kwargs['pk'])
        noticia = listar_noticia(pk)
        if not noticia:
            raise Http404("Notícia não encontrada.")
        return noticia

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Atualiza a notícia no banco de memória
        if 'ativo' in request.data and request.data['ativo'] is False:
            # Marca como inativa no banco de memória (não exclui)
            noticia_atualizada = editar_noticia(
                identificador=instance['id'],
                titulo=serializer.validated_data['titulo'],
                conteudo=serializer.validated_data['conteudo'],
                publicado=serializer.validated_data.get('publicado', False),
                autor=serializer.validated_data['autor']
            )

            if not noticia_atualizada:
                raise Http404("Erro ao atualizar: Notícia não encontrada.")

            return Response(noticia_atualizada, status=status.HTTP_200_OK)

        # Atualiza normalmente caso não esteja marcando como inativa
        noticia_atualizada = editar_noticia(
            identificador=instance['id'],
            titulo=serializer.validated_data['titulo'],
            conteudo=serializer.validated_data['conteudo'],
            publicado=serializer.validated_data.get('publicado', False),
            autor=serializer.validated_data['autor']
        )

        if not noticia_atualizada:
            raise Http404("Erro ao atualizar: Notícia não encontrada.")

        return Response(noticia_atualizada, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        pk = int(pk)
        noticia = remover_noticia(pk)  # Exclui permanentemente da memória

        if not noticia:
            return Response({'detail': 'Notícia não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'detail': 'Notícia removida permanentemente da memória.'}, status=status.HTTP_204_NO_CONTENT)


