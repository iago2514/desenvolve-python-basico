x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
soma = x + y 
resultado = soma % 2
if resultado == 0:
    print ('A soma desses números é par')
else:
    print ('A soma desses números é impar')