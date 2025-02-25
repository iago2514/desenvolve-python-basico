distancia = int(input('Digite a distancia da entrega (em Km): '))
peso = int(input('Digite o peso da entrega (em Kg): ')) 
preço = 1 * peso 
if 101 <= distancia <= 300:
    preço = 1.5 * peso
if distancia > 300:
    preço = 2 * peso 
if peso > 10:
    preço = preço + 10
print (f"O preço da entrega sera de R${preço:.2f}")