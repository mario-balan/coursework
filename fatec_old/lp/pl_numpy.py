# encoding: utf-8

import numpy as np

# Função para o cálculo das intersecções entre Restrições:

def linear(a, b):
    A = np.array([a[0:2], b[0:2]])
    B = np.array([a[-1],b[-1]])
    return np.array(np.linalg.solve(A, B)).tolist()

# Função para o cálculo do corte no eixo X1:

def zero_x1(a):
    if(a[0] != 0):
        return [float(a[2] / a[0]), 0]

# Função para o cálculo do corte no eixo X2:

def zero_x2(a):
    if(a[1] != 0):
        return [0, float(a[2] / a[1])]

# Restrições:

R1 = [7, 9, 63]
R2 = [11, 5, 55]
R3 = [1, 0, 4]

pontos = []
pontos_validos = []

pontos.append(linear(R1, R2))
pontos.append(linear(R1, R3))
pontos.append(linear(R2, R3))
pontos.append(zero_x1(R1))
pontos.append(zero_x2(R1))
pontos.append(zero_x1(R2))
pontos.append(zero_x2(R2))
pontos.append(zero_x1(R3))
pontos.append(zero_x2(R3))

#Pontos de intersecção:

pontos = [x for x in pontos if x is not None]


#Verificação dos pontos de intersecção pertencentes ao poliedro:

for x in pontos:
    if (x[0]*R1[0] + x[1]*R1[1] <= R1[2]):
        if (x[0]*R2[0] + x[1]*R2[1] <= R2[2]):
            if (x[0]*R3[0] + x[1]*R3[1] <= R3[2]):
                pontos_validos.append(x)

				
#Verificação de MaxZ:

maxz = 0
pontos_otimos = []

for x in pontos_validos:
    if (maxz < (x[0] + x[1]*2)):
        maxz = (x[0] + x[1]*2)
        pontos_otimos = x

print 'Pontos Ótimos:'
print 'x1 =', pontos_otimos[0]
print 'x2 =', pontos_otimos[1], '\n'
print 'Lucro Máximo:',maxz
