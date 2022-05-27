import todasCaracteristicasAvatares

perguntasFormulario = [
    {
        #Nome
        "pergunta": "Qual o nome do seu Avatar?: ",
        "chave": "nome",
        "multi_escolha": False
    },
    {
        #Gênero
        "pergunta": "Qual o Gênero do seu Avatar?: ",
        "chave": "genero",
        "multi_escolha": False
    },
    {
        #raça
        "pergunta": "Qual a raça do seu Avatar?: ",
        "chave": "raca",
        "multi_escolha": True
    },
    {
        # função
        "pergunta": "Qual a função do seu Avatar?: ",
        "chave": "funcao",
        "multi_escolha": True
    },
    {
        # cor de pele
        "pergunta": "Qual a cor da pele do seu Avatar?: ",
        "chave": "cor_de_pele",
        "multi_escolha": True
    },
    {
        #Primeira habilidade.
        "pergunta": "Qual a primeira habilidade do seu Avatar?: ",
        "chave": "primeira_habilidade",
        "multi_escolha": True
    },
    {
        #Região Natal
        "pergunta": "Qual a região natal do seu Avatar?: ",
        "chave": "regiao_natal",
        "multi_escolha": True
    },
    {
        # Primeir Arma.
        "pergunta": "Qual a primeira arma do seu Avatar?: ",
        "chave": "primeira_arma",
        "multi_escolha": True
    },
    {
        # Primeiro Acessório Místico.
        "pergunta": "Qual o primeiro acessório místico do seu Avatar?: ",
        "chave": "primeiro_acessorio_mistico",
        "multi_escolha": True
    },
]

def perguntaNome(pergunta):
    nome = input(pergunta)

    return nome

def perguntaGenero(pergunta):
    print(pergunta)
    genero = input("Digite 'M' para masculino, 'F' para feminino e 'N' não informado: ")
    
    return genero.lower()

def perguntaRaca(pergunta):
    print(pergunta)
    racas = todasCaracteristicasAvatares.racas

    for n in range(len(racas)):
        print(f"{n} - {racas[n]}")
    print("\n")
    raca = input(pergunta)
    
    return raca

def perguntaFuncao(pergunta):
    funcoes = todasCaracteristicasAvatares.funcoes

    for n in range(len(funcoes)):
        print(f"{n} - {funcoes[n]}")
    print("\n")
    funcao = input(pergunta)
    
    return funcao

def perguntaCorDePele(pergunta):
    print(pergunta)
    cores = todasCaracteristicasAvatares.cor_de_pele

    for n in range(len(cores)):
        print(f"{n} - {cores[n]}")
    print("\n")
    cor = input(pergunta)
    
    return cor

def perguntaPrimeiraHabilidade(pergunta):
    print(pergunta)
    primeira_habilidade = todasCaracteristicasAvatares.primeira_habilidade

    for n in range(len(primeira_habilidade)):
        print(f"{n} - {primeira_habilidade[n]}")
    print("\n")
    habilidade = input(pergunta)
    
    return habilidade

def perguntaRegiaoNatal(pergunta):
    print(pergunta)
    regiao_natal = todasCaracteristicasAvatares.regiao_natal

    for n in range(len(regiao_natal)):
        print(f"{n} - {regiao_natal[n]}")
    print("\n")
    regiao = input(pergunta)
    
    return regiao

def perguntaAcessorioMistico(pergunta):
    print(pergunta)
    primeiro_acessorio_mistico = todasCaracteristicasAvatares.primeiro_acessorio_mistico

    for n in range(len(primeiro_acessorio_mistico)):
        print(f"{n} - {primeiro_acessorio_mistico[n]}")
    print("\n")
    acessorio = input(pergunta)
    
    return acessorio

def perguntaPrimeiraArma(pergunta):
    print(pergunta)
    primeira_arma = todasCaracteristicasAvatares.primeira_arma

    for n in range(len(primeira_arma)):
        print(f"{n} - {primeira_arma[n]}")
    print("\n")
    arma = input(pergunta)
    
    return arma
