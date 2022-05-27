import json
import crudAvatar
from formulario import iniciarForm
from clear import clear

def main():
    clear()

    with open('data.json', 'r') as arquivo:
        lista = json.load(arquivo)
        # manipular o lista ...

    avatares = crudAvatar.lerAvatares()
    registro = iniciarForm(avatares)
    #aplicar o comando de limpar o cmd a cada pergunta
    # print(registro)
    if registro:
        crudAvatar.cadastrar(registro, lista)

    # print(avatares)

main()