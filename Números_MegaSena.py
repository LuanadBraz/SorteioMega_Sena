print('----------------------------------')
print('####### Sorteio Mega Sena ########')
print('----------------------------------')


from random import choices
import time

print('Carregando os Números...')
time.sleep(1.9)#Temporizador

qtd = 6 #qtd de numeros da mega

valores = range(1, 61) #aleatório de 1 a 61

loteria = []
for _ in range(qtd):
    loteria.append(choices(valores))

print('Seus números da Mega Sena são: ')
print(loteria)


print('----------------------------------')
print('####### Sorteio Mega Sena ########')
print('----------------------------------')