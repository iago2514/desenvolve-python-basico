gênero = input("Digite seu gênero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo_serviço = int(input("Digite o tempo de serviço (em anos): "))
# A: Para mulheres, ter mais de 60 anos. Para homens, 65. B: Ou ter trabalhado pelo menos 30 anos C: Ou ter 60 anos  e trabalhado pelo menos 25.
a = (gênero == 'F' and idade >= 60) or (gênero == 'M' and idade >= 65) 
b = tempo_serviço >= 30 
c = (idade >= 60) and (tempo_serviço >=25)
pode_aposentar = a or b or c 
print (pode_aposentar)