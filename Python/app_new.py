"""
#datetime_manipulation
from datetime import datetime

data_aniver = datetime.strptime(
    input("Qual sua data de aniversario?"), '%d/%m/%Y')
print(data_aniver)
data_atual = datetime.now()
dias_aniver = data_aniver - data_atual
#tempo_em_dias = dias_aniver.days
print(f'Faltam {dias_aniver.days} dias para o seu aniver')
"""
# generating random values
# gerador de cara ou coroa
import random
cara_ou_coroa = ['cara', 'coroa']
print(random.choices(cara_ou_coroa))

# sortear um nome entre cinco em uma lista
nomes = ['Mateus', 'Rafa', 'Conrado', 'Cecilia', 'Meredith']
print(random.choices(nomes))

# escolher aleatóriamente um número de 10 a 100
print(random.rad)
