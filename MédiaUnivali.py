print('Calculadora de média da Univali!')
nota1 = float(input('Escreva a nota da trilha: '))
nota2 = float(input('Escreva a nota do forúm: '))
nota3 = float(input('Escreva a nota da Prova: '))
res = ((nota1 * 2) + (nota2 * 2) + (nota3 * 6)) / 10
print('Análisando suas notas...')
print('Sua média do período é {:.2f}'.format(res))
