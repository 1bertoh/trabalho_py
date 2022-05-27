import interacoesAvatares
from todasPerguntasForm import *
from clear import clear

def formulario():
    clear()
    # perguntaNome(pergunta), perguntaGenero(pergunta), perguntaRaca(pergunta)]
    # O form vai aqui
    #Criar um array de func para cada iteração das perguntas
    # Nome, Gênero,  raça, função, cor de pele, Primeira habilidade, Região Natal, Primeira Arma, Primeiro Acessório Místico.
    # nome = input(input("Digite o nome do seu Avatar: "))
    perguntas = perguntasFormulario
    contador = 0
    avatar_form = {
    "nome": "",
    "genero": "",
    "raca": "",
    "funcao": "",
    "cor_de_pele": "",
    "primeira_habilidade": "",
    "regiao_natal": "",
    "primeira_arma": "",
    "primeiro_acessorio_mistico": ""
}

    while contador <= 9:
        clear()
        print("-"*50)
        if contador == 0:
            pergunta = perguntas[0]
            nome = perguntaNome(pergunta["pergunta"])
            contador += 1
            avatar_form[pergunta["chave"]] = nome
            
        elif contador == 1:
            pergunta = perguntas[1]
            genero = perguntaGenero(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = genero
            contador += 1

        elif contador == 2:
            pergunta = perguntas[2]
            raca = perguntaRaca(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = raca
            contador += 1
            
        elif contador == 3:
            pergunta = perguntas[3]
            funcao = perguntaFuncao(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = funcao
            contador += 1

        elif contador == 4:
            pergunta = perguntas[4]
            cor_de_pele = perguntaCorDePele(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = cor_de_pele
            contador += 1

        elif contador == 5:
            pergunta = perguntas[5]
            primeira_habilidade = perguntaPrimeiraHabilidade(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] =primeira_habilidade
            contador += 1

        elif contador == 6:
            pergunta = perguntas[6]
            regiao_natal = perguntaRegiaoNatal(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = regiao_natal
            contador += 1

        elif contador == 7:
            pergunta = perguntas[7]
            acessorio_mistico = perguntaAcessorioMistico(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = acessorio_mistico
            contador += 1

        elif contador == 8:
            pergunta = perguntas[8]
            primeira_arma = perguntaPrimeiraArma(pergunta["pergunta"])
            avatar_form[pergunta["chave"]] = primeira_arma
            contador += 1
            
        else:
            contador = len(perguntas) + 1
            
            return avatar_form
        
    

def iniciarForm(avatares:list) -> list: #para mostrar a pessoa a opção de ver os avatares criados ou assim abrir novas possibilidades
    temAvatares = len(avatares)

    if temAvatares:
        print("-"*20)
        opcao = input("Há Avatares criados, você deseja vê-los? Y\n ou \nvocê deseja criar um novo Avatar? C:\n ")

        if opcao.lower() == "y":
            interacoesAvatares.main()
        elif opcao.lower() == "c":
            return formulario()
        else:
            print("Comando não inválido") #rever esse trecho para fazer um loop para epetir a pergunta até uma respota descente
    else:
        opcao = input("não há Avatares criados, você deseja criar um novo Avatar? C \n")
        if(opcao.lower() == "c"):
            return formulario()

        else: 
            print("Comando não inválido") #rever esse trecho para fazer um loop para epetir a pergunta até uma respota descente




# formulario()