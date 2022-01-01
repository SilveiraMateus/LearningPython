from datetime import datetime

data_aniver = datetime.strptime(
    input("Qual sua data de aniversario?"), '%d/%m/%Y')
print(data_aniver)
data_atual = datetime.now()
dias_aniver = data_aniver - data_atual
#tempo_em_dias = dias_aniver.days
print(f'Faltam {dias_aniver.days} dias para o seu aniver')
