cont= ( 'zero', 'um' ,'dois' ,'tres' ,'quatro', 'cinco' ,' seis', 'oito', ' nove', 'dez', 'onze', ' doze', 'treze', 'catorze' ,'quinze' ,'dezesseis' ,'dezoito', 'dizenove' ,'vinte')
while True:
    num= int(input('digite um numero pro favor....'))
    if 0 <= num <=20:
        break
    print ('tente novamente ')
print (f'voce digitou numero {cont[num]}')