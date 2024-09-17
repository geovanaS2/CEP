import requests

#busca de endereco com o cep
print("-----------------------------------------------")
print("Busca o endereço com o cep")
cep = "039.59.000"

cep = cep.replace(".", "").replace("/", "").replace(" ", "").replace("-", "")

if len(cep) == 8 :

  link = f'https://viacep.com.br/ws/{cep}/json/'

  requisicao = requests.get(link)

  print(requisicao)

  dic_requisacao = requisicao.json()

  uf = dic_requisacao ['uf']
  cidade = dic_requisacao ['localidade']
  bairro = dic_requisacao ['bairro']

  print(uf, cidade, bairro)

else:
  print("CEP inválido")
print("-----------------------------------------------")

#pesquisar cep por endereço
print("pesquisar cep por endereço")
uf = "sp"
cidade="são paulo"
endereco="luis botta"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/' 

requisicao = requests.get(link)
print (requisicao)

dic_requisacao = requisicao.json()
print(dic_requisacao)
print("-----------------------------------------------")

#imprime de forma mais "bonita"
print("imprime com o pprint")
import pprint
pprint.pprint(dic_requisacao)
print("-----------------------------------------------")

#imprime com o pandas
print("imprime com o pandas")
import pandas as pd
from tabulate import tabulate

print("-----------------------------------------------")
tabela = pd.DataFrame(dic_requisacao)
print (tabela)
print("-----------------------------------------------")

print("imprime com o pandas DATAFRAME")
tabela = pd.DataFrame(dic_requisacao)
for i in tabela.iterrows():
  print (tabulate(tabela, headers='keys', tablefmt='grid'))
  break
print("-----------------------------------------------")