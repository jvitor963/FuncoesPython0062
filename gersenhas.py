# geração de senhas
from random import choice
caracteres = "0123456789!@#abcdeaBCDE"
algarismos = caracteres [:10]
senha_alfa = ""
senha_num = ""
for n in range(10):
    senha_num+=choice(algarismos)
    senha_alfa+=choice(caracteres)
print("Senha numérica: ",senha_num)
print("Senha alfanumérica: ",senha_alfa)

