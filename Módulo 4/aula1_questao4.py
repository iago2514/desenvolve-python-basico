n = int(input('Digite um numero: '))
maior = 0 
while True:
    if n > 0:
        x = int(input('Digite um numero: '))
        if x > maior:
            maior = x
        n = n - 1 
print ('imprima maior')