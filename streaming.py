import random

listaHorasMes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

acao = ["ação",]
aventura = ["aventura",]
comedia = ["comédia",]
drama = ["drama",]
ficcao = ["ficção",]
terror = ["terror",]
romance = ["romance",]
suspense = ["suspense",]
fantasia = ["fantasia",]
musical = ["musical",]
documentario = ["documentário",]
policial = ["policial"]

listaHorasGeneroMes = []
for i in range(12):
    horas = random.randint(0, 5)
    listaHorasGeneroMes.append(horas)


for i in range(12):
    acao.append(listaHorasGeneroMes[i])


print(acao)


loop = True
while loop == True:

    # Gêneros assistidos
    listaGeneros = ["ação", "aventura", "comédia", "drama", "ficção científica",
                    "terror", "romance", "suspense", "fantasia", "musical", "documentário", "policial"]

    # Mêses do ano
    listaMeses = ["jan", "fev", "mar", "abr", "mai",
                  "jun", "jul", "ago", "set", "out", "nov", "dez"]

    # Horas assistidas por mês
    # listaHorasFilme  # Ta ali em cima

    # FUNÇÃO DESCOBRIR GÊNERO PREFERIDO

    # def generoFav():

    # FUNÇÃO CALCULAR TEMPO

    # def calcTempo(listaHorasMes):

    # Mensagem de bem vindo e escolha da função
    print("Bem vindo ao nosso programa de streaming\n")
    print("\ndigite o numero para a função escolhida")

    print("\n(1) | Total de horas assistidas ")
    print("(2) | Qual é o meu genero preferido ")

    escolha = int(input("\nDigite aqui: "))

    '''
    Criação da matriz 
    NÃO ALTERAR
    '''
# ;favInput
