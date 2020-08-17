### Objetos:

class Vetor:

    lista = []

    def __init__(self, tamanho):
        self.lista = [''] * tamanho
        self.i = 0

    def insert(self, string):
        if (self.i < len(self.lista)):
            self.lista[self.i] = string
            self.i += 1
        else:
            self.lista.append(string)
            self.i += 1

    def get(self, posicao):
        try:
            return self.lista[posicao]
        except:
            return None

    def size(self):
        return self.i

### Inicialização:

vetor_1 = Vetor(5)
vetor_2 = Vetor(10)

### Testes:

for string in ['A','B','C']:
    vetor_1.insert(string)

for string in ['A','C','B','K','I','J','D','F','G','E','H']:
    vetor_2.insert(string)

print('\nVetor 1:')
print(vetor_1.get(0))
print(vetor_1.size())

print('\nVetor 2:')
print(vetor_2.get(10))
print(vetor_2.get(11))
print(vetor_2.size())
