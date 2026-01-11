num= (int(input('digite um numero pro favor....')),  int(input('digite outro numero pro favor....')), int(input('digite mais um numero pro favor....')), int(input('digite o ultimo numero pro favor....')))
print (f'voce digitou os valores {num}')
print ("o valor 9 apareceu {} vezes".format(num.count(9)))
print(f'o valor 3 apareceu na {num.index(3)+1}ª posição' if 3 in num else 'o valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 ==0:
        print (f'os valores pares digitados foram {n}', end=' ')

