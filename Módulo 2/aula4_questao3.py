nome_produto1 = input("Digite o nome do produot 1: ")
preço_produto1 = float(input("Digite o preço unitário do produto 1: "))
quantidade_produto1 = int(input("Digite a quantidade do produto 1: "))
nome_produto2 = input("Digite o nome do produot 2: ")
preço_produto2 = float(input("Digite o preço unitário do produto 2: "))
quantidade_produto2 = int(input("Digite a quantidade do produto 2: "))
nome_produto3 = input("Digite o nome do produot 3: ")
preço_produto3 = float(input("Digite o preço unitário do produto 3: "))
quantidade_produto3 = int(input("Digite a quantidade do produto 3: "))
total_produto1 = preço_produto1 * quantidade_produto1
total_produto2 =preço_produto2 * quantidade_produto2
total_produto3 = preço_produto3 * quantidade_produto3
total_da_compra = total_produto1 + total_produto2 + total_produto3
print (f"Total: R$ {total_da_compra:,.2f}")