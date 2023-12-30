import test2
import functions

variavel_qualquer = 0.5
print(variavel_qualquer, type(variavel_qualquer))  # vai printar valor contido na variável e o tipo da variável

''' o python ja sabe o tipo sem que você precise typar a variável :) '''

total = variavel_qualquer + 0.5
print('valor de total é: ', total)  # aqui nesta variável total, a gente tá chamando variavel_qualquer e somando com 0.5

print('Função de soma:')
print('Valor de total é ', total, 'e valor de variavel opa é', test2.opa, 'somando dá: ',
      functions.soma(total, test2.opa))