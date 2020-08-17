### Objetos:

class Gabarito:

    def __init__(self, respostas):
        self.respostas = respostas

    @classmethod
    def from_csv(cls, gabarito_csv):
        gabarito = gabarito_csv.split(';')
        return cls(gabarito)

    def resposta_questao(self, numero_questao):
        return self.respostas[numero_questao - 1]



class Prova:

    def __init__(self, gabarito):
        self.gabarito = gabarito
        self.questao = 0
        self.correcao = []
        self.acertos = 0
        self.nota = 0

    def resposta_aluno(self, resposta):
        self.questao += 1
        if (resposta == self.gabarito.resposta_questao(self.questao)):
            self.correcao.append(True)
        else:
            self.correcao.append(False)

    def calcula_acertos(self):
        self.acertos = sum(self.correcao)
        return self.acertos

    def calcula_nota(self):
        peso_a = 0.5
        peso_b = 1
        pontos = 0
        total = 0
        for i in range(len(self.correcao)):
            if (i < 5):
                if (self.correcao[i] == True):
                    pontos += peso_a
                total += peso_a
            else:
                if (self.correcao[i] == True):
                    pontos += peso_b
                total += peso_b
        self.nota = round((pontos / total) * 10, 2)
        return self.nota

    def maior(self, outra_prova):
        if (self.acertos > outra_prova.acertos):
            return self.acertos
        elif (self.acertos == outra_prova.acertos):
            if (self.nota >= outra_prova.nota):
                return self.nota
            else:
                return outra_prova.nota
        else:
            return outra_prova.acertos

### Inicialização:


matematica_csv = 'A;A;A;A;A;A;A;A;A;A'
portugues_csv = 'A;B;C;D;E;A;B;C;D;E'

portugues = Gabarito.from_csv(portugues_csv)
matematica = Gabarito.from_csv(matematica_csv)

prova1 = Prova(matematica)
prova2 = Prova(matematica)
prova3 = Prova(matematica)
prova4 = Prova(matematica)

### Testes:

for i in ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']:
    prova1.resposta_aluno(i)

for i in ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']:
    prova2.resposta_aluno(i)

for i in ['B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A']:
    prova3.resposta_aluno(i)

for i in ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B']:
    prova4.resposta_aluno(i)

print ('\n1:', prova1.correcao)
print (prova1.calcula_acertos())
print (prova1.calcula_nota())

print ('\n2:', prova2.correcao)
print (prova2.calcula_acertos())
print (prova2.calcula_nota())

print ('\n3:', prova3.correcao)
print (prova3.calcula_acertos())
print (prova3.calcula_nota())

print ('\n4:', prova4.correcao)
print (prova4.calcula_acertos())
print (prova4.calcula_nota())

print ('\nmaior(): {}'.format(prova1.maior(prova4)))
print ('\nmaior(): {}'.format(prova3.maior(prova4)))
print ('\nmaior(): {}'.format(prova1.maior(prova2)))
