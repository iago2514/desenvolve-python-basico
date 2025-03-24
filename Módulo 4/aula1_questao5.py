n = int(input('Digite quantas respostas foram: '))
idade = 0
soma = 0
for i in range (n):
    idade= int(input('Qual é a idade: '))
    soma += idade 
media = soma /n
print(f'A média das idades é: {media:.0f}')