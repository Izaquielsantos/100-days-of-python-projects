import random 

print ('vamos comeca o jogo de advinhar ')
print ('por favor escolhar um numero de 1 a 10')

maquina= random.randint(1,10)
cont=0
acertou= False

while not acertou:
    chute= int(input('please digite um numero de 1 a 10...'))
    cont +=1
    if chute == maquina:
        print (F'parabens voce acertou em {cont} tentativas')
        acertou= True
    elif chute < maquina:
        print (f'tente um numero um pouco maior please')
    else:
        print(f'tente um numero um pouco menor please')