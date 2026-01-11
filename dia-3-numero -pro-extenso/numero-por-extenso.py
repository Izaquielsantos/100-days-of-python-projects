cont= ( 'zero', 'um' ,'dois' ,'tres' ,'quatro', 'cinco' ,' seis', 'oito', ' nove', 'dez', 'onze', ' doze', 'treze', 'catorze' ,'quinze' ,'dezesseis' ,'dezoito', 'dizenove' ,'vinte')
while True:
    num= int(input('digite um numero pro favor....'))
    if 0 <= num <=20:
        break
    print ('tente novamente ')
p=str(input('voce  quer continuar ? [s/n]'))
if p in 'nN':
    print('fim do programa')

print (f'voce digitou numero {cont[num]}')