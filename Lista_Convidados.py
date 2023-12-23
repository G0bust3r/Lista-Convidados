'''
Exercicio: Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa;
Após isso o programa ira perguntar o nome de todas as pessoas e colocar numa lista de convidados;
Após isso irá imprimir todos os nomes da lista.
'''

import os

print('#################################')
print ('#### Controle de convidados: #### ')
print('#################################\n')

quant_convidados = int (input ('Qual a quantidade de convidados ? '))
print ('\nQuantidade de convidados: ', quant_convidados)
print('\n')

lista_de_convidados = []

contador = 1

while contador <= quant_convidados: # Se fosse com for: for contador in range(int(quant_convidados))
     name_convidado = input ('Qual nome do convidado ' + str (contador) + ': ')
     lista_de_convidados.append(name_convidado)
     contador += 1

contador_convidados = 1

# Limpar a tela (Windows)
os.system('cls')

print('\nQuantidade Convidados: ', quant_convidados )
print('\nLista de Convidados: ') 
for i, convidado in enumerate (lista_de_convidados, start=1):
 print (str(i), '-', (convidado)) 

# Mensagem final
print('\nPrograma concluído. \nObrigado por utilizar o Controle de Convidados!')




