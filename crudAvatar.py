import json
import interacoesAvatares

def lerAvatares():
    # obj = None
    with open('data.json', 'r') as raca:
        obj = json.load(raca)
        
        return obj
        # manipular o obj ...


def editar( obj: list):
    # gravar registro em outro arquivo
    with open('data.json', 'w') as arq:
        json.dump(obj, arq, indent=2)

def cadastrar(registro, obj: list):
    obj.append(registro)
    # gravar registro em outro arquivo
    with open('data.json', 'w') as arq:
        json.dump(obj, arq, indent=2)

def excluir(obj: list, index: int):
    teste = obj.pop(index)
    # gravar registro em outro arquivo
    with open('data.json', 'w') as arq:
        json.dump(obj, arq, indent=2)
    interacoesAvatares.visualizarTodos(obj)
    