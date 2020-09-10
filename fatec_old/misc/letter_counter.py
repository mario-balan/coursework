# a letter counter (an example of using a dictionary):

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

x = input("Escreva uma frase: ").lower()

letras = {}

for char in x:
    if char in alfabeto:
        if char in letras:
            letras[char] = letras[char] + 1
        else:
            letras[char] = 1

keys = letras.keys()
for char in sorted(keys):
    print(char, ':', letras[char])

