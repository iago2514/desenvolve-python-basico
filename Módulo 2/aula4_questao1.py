# Solicitar ao usuário o valor do comprimento em metros do terreno (inteiro) 
comprimrnto = int(input("Digite o comprimento do terreno (em metros): "))
#solicitar ao usuario o valor da largura em metros do terreno (inteiro)
largura = int(input("Digite a largura do terreno (em metros): "))
#Solicitar ao usuário o valor do metro quadrado na região (numero com ponto flutuante) 
preço_metro_quadrado = float(input("Digite o preço do metro quadrado: "))
# Calculando a area do terreno em metros quadrado 
area_m2 = comprimrnto * largura
# Calculando o preço total do terreno 
preço_total = preço_metro_quadrado * area_m2
print (f"O terreno possui {area_m2}m2 e custa R${preço_total:,.2f}")