idade = int(input("Digite sua idade: "))
Jogos_3_jogos = input ("Já jogou pelo menos 3 jogos de tabuleiro?(true/false) ")
jogos_ganhos = int(input("Quantos jogos já venceu? "))
qualificado = 16<= idade <=18 and Jogos_3_jogos == 'true' and jogos_ganhos >=1
print ("Apto para ingressar no clube de jogos de tabuleiro:", qualificado)
