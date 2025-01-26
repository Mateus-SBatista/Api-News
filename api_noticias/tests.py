from rest_framework.test import APITestCase
from rest_framework import status
from .models import Noticia
from .memoria import banco, adicionar_noticia, listar_todas_noticias, listar_noticia


class NoticiaAPITestCase(APITestCase):
    def setUp(self):
        # Resetar o banco de memória antes de cada teste
        global banco
        banco.clear()

        # Configuração inicial para o banco SQL
        self.noticia_sql = Noticia.objects.create(
            titulo="Notícia SQL",
            conteudo="Conteúdo SQL",
            autor="Autor SQL",
            ativo=True
        )

        # Configuração inicial para o banco de memória
        self.noticia_memoria = adicionar_noticia(
            titulo="Notícia Memória",
            conteudo="Conteúdo Memória",
            publicado=True,
            autor="Autor Memória"
        )

        self.valid_data_sql = {
            "titulo": "Nova Notícia SQL",
            "conteudo": "Conteúdo da nova notícia SQL",
            "autor": "Novo Autor SQL"
        }

        self.valid_data_memoria = {
            "titulo": "Nova Notícia Memória",
            "conteudo": "Conteúdo da nova notícia Memória",
            "publicado": False,
            "autor": "Novo Autor Memória"
        }

    # Tests para o Banco SQL
    def test_listar_noticias_sql(self):
        response = self.client.get('/api/api_noticias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], self.noticia_sql.titulo)

    def test_criar_noticia_sql(self):
        response = self.client.post('/api/api_noticias/', data=self.valid_data_sql)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Noticia.objects.count(), 2)

    def test_obter_noticia_sql_por_id(self):
        response = self.client.get(f'/api/api_noticias/{self.noticia_sql.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.noticia_sql.titulo)

    def test_atualizar_noticia_sql(self):
        update_data = {"titulo": "Título SQL Atualizado"}
        response = self.client.patch(f'/api/api_noticias/{self.noticia_sql.id}/', data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.noticia_sql.refresh_from_db()
        self.assertEqual(self.noticia_sql.titulo, "Título SQL Atualizado")

    def test_deletar_noticia_sql(self):
        response = self.client.delete(f'/api/api_noticias/{self.noticia_sql.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Noticia.objects.filter(ativo=True).count(), 0)

    # Tests para o Banco de Memória
    def test_listar_noticias_memoria(self):
        response = self.client.get('/api/memoria/api_noticias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], self.noticia_memoria['titulo'])

    def test_criar_noticia_memoria(self):
        response = self.client.post('/api/memoria/api_noticias/', data=self.valid_data_memoria)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(listar_todas_noticias()), 2)

    def test_obter_noticia_memoria_por_id(self):
        response = self.client.get(f"/api/memoria/api_noticias/{self.noticia_memoria['id']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.noticia_memoria['titulo'])

    def test_atualizar_noticia_memoria(self):
        update_data = {"titulo": "Título Memória Atualizado", "conteudo": "Novo conteúdo", "publicado": True, "autor": "Autor Atualizado"}
        response = self.client.put(f"/api/memoria/api_noticias/{self.noticia_memoria['id']}/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        noticia_atualizada = listar_noticia(self.noticia_memoria['id'])
        self.assertEqual(noticia_atualizada['titulo'], "Título Memória Atualizado")

    def test_deletar_noticia_memoria(self):
        response = self.client.delete(f"/api/memoria/api_noticias/{self.noticia_memoria['id']}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(listar_todas_noticias()), 0)
