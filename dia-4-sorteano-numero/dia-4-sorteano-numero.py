from random import randint
n= (randint (0,10), randint (0,10), randint (0,10), randint (0,10), randint (0,10))
print (f'os valores sorteados foram:{n} ', end='')
print (f'o maior valor sorteado foi {max(n)}')
print (f'o menor valor sorteado foi {min(n)}')
print('fim do programa')