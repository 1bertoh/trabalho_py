import todasCaracteristicasAvatares
import crudAvatar
import formulario

def main(): #acoes = visualizar, editar, excluir
    print()
    avatares = crudAvatar.lerAvatares()
    visualizarTodos(avatares)

def visualizarTodos(avatares):
    print()
    for n in range(len(avatares)):
        print(f"{n} - {avatares[n]['nome']}")
    index = int(input("Qual avatar você quer visualizar?: "))

    visualizar(index, avatares)

def visualizar(index, avatares):
    print(f"Nome: {avatares[index]['nome']}")
    print(f"Genêro: {avatares[index]['genero']}")
    print(f"Raça: {pegarResposta(todasCaracteristicasAvatares.racas,int(avatares[index]['raca'])) }")
    print(f"Função: {pegarResposta(todasCaracteristicasAvatares.funcoes, int(avatares[index]['funcao'])) }")
    print(f"Cor de pele: {pegarResposta(todasCaracteristicasAvatares.cor_de_pele, int(avatares[index]['cor_de_pele']))}")
    print(f"Primeira habilidade: {pegarResposta(todasCaracteristicasAvatares.primeira_habilidade, int(avatares[index]['primeira_habilidade']))}")
    print(f"Região natal: {pegarResposta(todasCaracteristicasAvatares.regiao_natal, int(avatares[index]['regiao_natal']))}")
    print(f"Primeira arma: {pegarResposta(todasCaracteristicasAvatares.primeira_arma, int(avatares[index]['primeira_arma']))}")
    print(f"Primeiro acessrio mistico: {pegarResposta(todasCaracteristicasAvatares.primeiro_acessorio_mistico, int(avatares[index]['primeiro_acessorio_mistico']))}")
    
    acao = input("Digite 'D' para deletar ou 'E' para editar ou 'V' para voltar: ")

    if acao == "d":
        excluir(avatares, index)
    elif acao == "e":
        editar(avatares, index)
    elif acao == "v":
        voltar(avatares)

def editar(avatares, index):
    avatar = formulario.formulario()
    avatares[index] = avatar
    crudAvatar.editar(avatares)
    print()

def excluir(avatares: list, index):
    crudAvatar.excluir(avatares, index)
    main()

def voltar(avatares):
    visualizarTodos(avatares)

def pegarResposta (lista, indice):
    # print(lista, indice, len(lista))
    tamanho = len(lista)

    if indice >= 0 and indice < tamanho:
        return lista[indice]
    elif indice >= tamanho:
        return "N/A"
    else:
        return "N/A"

# main()