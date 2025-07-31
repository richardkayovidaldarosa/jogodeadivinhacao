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