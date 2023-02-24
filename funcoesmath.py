# diversas funções do módulo math
from math import *
raio=float(input("Forneça o raio do círclo: "))
print("Valor do raio: ",raio)
print("Área: ",pi * pow(raio,2))
print("-" * 50)

n=int(input("Forneça um valor inteiro: "))
print("Valor Fornecido: ",n)
print("Raiz Quadrada: ",sqrt(n))
print("-" * 50)

v1 = int(input("Forneça o primeiro valor: "))
v2 = int(input("Forneça o segundo valor: "))
if(v1==v2):
    print("Os valores são iguais!!")
else:
    print("O menor valor é: ",min(v1,v2))
    print("o valor maior é ", max(v1,v2))
    