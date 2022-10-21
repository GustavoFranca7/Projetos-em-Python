print('=-=-=-=-=-=-=-= Conversor de bases numéricas =-=-=-=-=-=-=-=')

num = int(input('Digíte um número inteiro: '))
print('Escolha uma das bases para fazer a conversão: \n'
      '[ 1 ] Converter para BINÁRIO \n'
      '[ 2 ] Converter para OCTAL \n'
      '[ 3 ] Converter para HEXADECIMAL')

opção = int(input('Sua opção: '))

if opção == 1:
    '''#print('O número {} convertido para Binário é igual a {:0b}'.format(num, num))'''
    print('O número {} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    '''print('O número {} convertido para OCTAL é igual a {:0o}'.format(num, num))'''
    print('O número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    '''print('O número {} convertido para HEXADECIMAL é igual a {:0x}'.format(num, num))'''
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, Tente novamente!')




