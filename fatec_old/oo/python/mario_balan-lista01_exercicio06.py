### Objetos:

class Vetor:

    def __init__(self):
        self.lista = []

    def insert(self, string):
        i = 0
        if not self.lista or string > self.lista[-1]:
            self.lista.append(string)
        else:
            while string > self.lista[i]:
                i += 1
            self.lista.insert(i, string)

    def get(self, i):
        try:
            return self.lista[i]
        except:
            return None

    def size(self):
        return len(self.lista)

    def merge(self, outro_vetor):
        novo_vetor = Vetor()
        novo_vetor.lista = sorted(self.lista + outro_vetor.lista)
        return novo_vetor

### Inicialização:

vetor_1 = Vetor()
vetor_2 = Vetor()

### Testes:

for string in ['L','M','N']:
    vetor_1.insert(string)

for string in ['C','B','K','I','J','D','F','G','E','H','A']:
    vetor_2.insert(string)

print('\nVetor 1:')
print(vetor_1.lista)
print(vetor_1.get(2))
print(vetor_1.get(3))
print(vetor_1.size())

print('\nVetor 2:')
print(vetor_2.lista)
print(vetor_2.get(10))
print(vetor_2.get(11))
print(vetor_2.size())

print('\nVetor 3:')
vetor_3 = vetor_1.merge(vetor_2)
print(vetor_3.lista)
