# funções de data
from datetime import *
agora = datetime.now()
print("Data Completa: ",agora)
print("Dia: ",agora.day)
print("Mês: ",agora.month)
print("Ano: ",agora.year)
print("Hora: ",agora.hour)
print("Minuto: ",agora.minute)
print("Segundo: ",agora.second)

data = datetime(2023,12,31,23,59,59)
print("Data Completa: ",data)
print("Dia da Semana: ",data.strftime("%A"))
print("Número da Semana: ",data.strftime("%U"))
print("Nome do mês: ",data.strftime("%B"))
diferenca = agora - data
print("Diferença entre datas: ",diferenca)
data30 = data + timedelta(days=30)
print("Soma 30 dias: ",data30)
