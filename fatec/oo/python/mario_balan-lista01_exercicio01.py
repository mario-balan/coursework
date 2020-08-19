### Objetos:

class Aluno:

    num_de_alunos = 0

    def __init__(self, matricula, nome, nota1, nota2, nota_trabalho):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota_trabalho = nota_trabalho

        Aluno.num_de_alunos += 1

    def media(self):
        return round((2.5 * self.nota1 + 2.5 * self.nota2 + 2 * self.nota_trabalho) / 7.0, 2)

    def final(self):
        nota_final = self.media()
        if (nota_final < 5):
            return 10 - nota_final
        else:
            return 0

### Instanciação:

aln_1 = Aluno(4001, 'Antígona', 10, 9, 5)
aln_2 = Aluno(4002, 'Boécio', 3, 8, 9)
aln_3 = Aluno(4003, 'Calístenes', 1, 0, 6)

### Testes:

print('Número de alunos: {}\n'.format(Aluno.num_de_alunos))

print('#{}\nAluno: {}'.format(aln_1.matricula, aln_1.nome))
print('Média: {:0.2f}'.format(aln_1.media()))
print('Nota mínima no Exame: {:0.2f}\n'.format(aln_1.final()))

print('#{}\nAluno: {}'.format(aln_2.matricula, aln_2.nome))
print('Média: {:0.2f}'.format(aln_2.media()))
print('Nota mínima no Exame: {:0.2f}\n'.format(aln_2.final()))

print('#{}\nAluno: {}'.format(aln_3.matricula, aln_3.nome))
print('Média: {:0.2f}'.format(aln_3.media()))
print('Nota mínima no Exame: {:0.2f}\n'.format(aln_3.final()))
