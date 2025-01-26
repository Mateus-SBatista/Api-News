from datetime import datetime

banco = {}
contador_id = 1


def adicionar_noticia(titulo: str, conteudo: str, publicado: bool, autor: str):
    global contador_id
    identificador = contador_id 
    contador_id += 1  

    data_criacao = str(datetime.now())
    banco[identificador] = {
        'id': identificador,
        'titulo': titulo,
        'conteudo': conteudo,
        'autor': autor,
        'publicado': publicado,
        'data_criacao': data_criacao
    }
    return banco[identificador]


def editar_noticia(identificador: int, titulo: str, conteudo: str, publicado: bool, autor: str):
    if identificador in banco:
        data_criacao = banco[identificador]['data_criacao']
        banco[identificador] = {
            'id': identificador,
            'titulo': titulo,
            'conteudo': conteudo,
            'autor': autor,
            'publicado': publicado,
            'data_criacao': data_criacao
        }
        return banco[identificador]
    return None 


def listar_noticia(identificador: int):
    return banco.get(identificador)


def listar_todas_noticias():
    return list(banco.values())


def remover_noticia(identificador: int):
    return banco.pop(identificador, None)
