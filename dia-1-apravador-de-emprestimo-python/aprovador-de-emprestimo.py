casa= float(input('qual e valo da casa por favor'))
salario=float(input('qual e valo do seu salario por favo'))
anos=int(input('EM quantos anos voce vai paga'))
prestacao= casa/(anos*12)
pos=salario*30/100
print(f'para pagar a casa de {casa} ')
print(f'A sua prestacao foi de {prestacao}')
if prestacao<=pos:
    print ('O seu emprestimo foi aprovado , agora e so curti o seu emprestimo')
else:
    print ('min descupe o seu Emprestimo foi recusado, nao deu volte sempre ')
print ('tchau, OBRIGADO')
