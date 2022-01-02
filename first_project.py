'''
First project is about to create a database with employee records

Steps:
#First Module:
1-Get the user name
2-Get the user age
3-Get the date of register (automatic)
4-Randomly sort a card ('R$50,00', 'R$250,00', 'R$120,00')
5-Get the user birthday 

#2 Second Module:
Print all information organized by a specific phrase.
'''
from datetime import datetime
import random

name = input('Whats your name?')
age = input('Whats your age?')
birthday = datetime.strptime(input('Whats your birthday?'), '%d/%m/%Y')
date = datetime.now()
cards = ['R$50,00', 'R$250,00', 'R$120,00']
employee_card = random.choices(cards)
print(f'Olá {name}, seu registro foi concluído com sucesso no dia {date}. \n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {employee_card}')
