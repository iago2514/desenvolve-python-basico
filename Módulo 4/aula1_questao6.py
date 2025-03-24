total = int(input('Digite o total de experimetos: '))
s = int(input('Digite a quantidade de sapos: '))
r = int(input('Digite a quantidade de ratos: '))
c = int(input('Digite a quantidade de coelhos: '))
percentual_sapos = (s/total)*100
percentual_ratos = (r/total)*100
percentual_coelhos = (c/total)*100
print (f'Total: {total} cobaias ')
print (f'Total de coelhos: {c}')
print (f'Total de ratos {r}')
print (f'Total de sapos: {s}')
print (f'Percentual de coelhos: {percentual_coelhos:.2f}%')
print (f'Percentual de ratos: {percentual_ratos:.2f}%')
print (f'Percentual de sapos: {percentual_sapos:.2f}%')