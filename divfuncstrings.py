# diversas funções relacionadas a string
frase = input("Digite uma frase: ")
print(frase) # frase digitada
print(frase.upper()) # frase em maiúsculas
print(frase.lower()) # frase em minúsculas
print(frase.capitalize())
print(len(frase)) # quantidade de caracteres
print(frase.count('a'))
print(frase.find('r'))
print(frase.isdigit())
print(frase[3]) # caractere da posição 3
print(frase[2:5]) # caracteres entre 2 e 5
palavras = frase.split()
print(palavras)
frase=frase.replace(" ","_")
print(frase)