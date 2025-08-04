import random
print("#######################")
print("# jogo de adivinhacao #")
print("#      Richard        #")
print("#######################")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("Qual níveis de dificuldade? ")
print("(1)- Fácil (2)- Médio (3)- Difícil ")

nível = int(input("Escolha um nível"))

if(nível == 1) :
    print("20 tentativas")
    totalTentativas = 20
elif(nível == 2) :
    print("10 tentativas")
    totalTentativas = 10
elif(nível == 3) :
    print("5 tentativas.")
    totalTentativas = 5


for rodada in range (1, totalTentativas +1) :
    print("Tentativa {} de {}".format(rodada, totalTentativas))
    chute_str = input ("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if(chute < 1 or > 100):
        print ("Número inválido")
        continue
    
    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto 
