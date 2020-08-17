### Objetos:

class Equipamento:

    def __init__(self, total):
        self.equipamentos = [0] * total

    @property
    def total(self):
        return len(self.equipamentos)

    def get_valor(self, cod):
        return self.equipamentos[cod]

    def set_valor(self, cod, valor):
        self.equipamentos[cod] = valor


class EquipamentoCorrigido(Equipamento):

    def __init__(self, lista):
        super(Equipamento).__init__()
        self.mes_atual = 1
        self.equipamentos = []
        for i in range(len(lista.equipamentos)):
            self.equipamentos.append({'valor':lista.equipamentos[i],'mes': self.mes_atual})

    def get_mes(self, cod):
        return self.equipamentos[cod]['mes']

    def set_mes(self, cod, mes):
        self.equipamentos[cod]['mes'] = mes

    def corrige(self, percentual):
        for i in range(len(self.equipamentos)):
            if (self.equipamentos[i]['mes'] == self.mes_atual):
                self.equipamentos[i]['valor'] += self.equipamentos[i]['valor'] * (percentual/100)
        if (self.mes_atual == 12):
            self.mes_atual = 1
        else:
            self.mes_atual += 1

    def substitui(self, outra_lista):
        if (len(self.equipamentos) == len(outra_lista.equipamentos)):
            for i in range(len(self.equipamentos)):
                self.equipamentos[i]['valor'] = outra_lista.equipamentos[i]['valor']
                self.equipamentos[i]['mes'] = outra_lista.equipamentos[i]['mes']

### Inicialização classe Equipamento:
lista_equip_1 = Equipamento(4)
lista_equip_1.set_valor(0, 2000)
lista_equip_1.set_valor(1, 3000)
lista_equip_1.set_valor(2, 4000)
lista_equip_1.set_valor(3, 5000)
lista_equip_2 = Equipamento(1)
lista_equip_1.set_valor(0, 5000)

### Testes classe Equipamento:
print(lista_equip_1.equipamentos)
print(lista_equip_1.total)
print(lista_equip_1.get_valor(0))
print(lista_equip_1.get_valor(1))

### Inicialização classe EquipamentoCorrigido:
lista_equip_1_corrigido = EquipamentoCorrigido(lista_equip_1)
lista_equip_2_corrigido = EquipamentoCorrigido(lista_equip_1)
lista_equip_3_corrigido = EquipamentoCorrigido(lista_equip_2)

### Inicialização classe EquipamentoCorrigido:
print('\n')
print(lista_equip_1_corrigido.equipamentos)
print(lista_equip_2_corrigido.equipamentos)
print(lista_equip_3_corrigido.equipamentos)

print('\n')
print(lista_equip_1_corrigido.get_mes(2))
lista_equip_1_corrigido.set_mes(2, 7)
print(lista_equip_1_corrigido.get_mes(2))

print('\n')
lista_equip_1_corrigido.corrige(10)
print(lista_equip_1_corrigido.equipamentos)
for i in range(30):
    lista_equip_1_corrigido.corrige(10)
print(lista_equip_1_corrigido.equipamentos)

print('\n')
lista_equip_1_corrigido.substitui(lista_equip_2_corrigido)
print(lista_equip_1_corrigido.equipamentos)

print('\n')
lista_equip_1_corrigido.substitui(lista_equip_3_corrigido)
print(lista_equip_1_corrigido.equipamentos)
