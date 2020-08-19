# -*- coding: utf-8 -*-
import numpy as np

A = np.array([[4, 10, 1, 0],
             [7, 9, 0, 1]])

b = np.array([150, 200])

c = -np.array([6, 11, 0, 0])


#largura da matriz tecnológica e da matriz slack:
tmn_tec = 2
tmn_slack = 2


#coeficientes da matriz tecnológica e da matriz slack:
ci = [i for i in range(0, len(c))]
cb = np.array(c[tmn_slack:])
cnb = np.array(c[:tmn_slack])


while True:

    # índices:
    cbi = ci[tmn_slack:]
    cni = ci[:tmn_slack]

    # matriz tecnológica:
    B = A[:, cbi]

    #matriz tecnológica inversa:
    Binv = np.linalg.inv(B)

    #matriz slack:
    N = A[:, cni]

    # cálculo base:
    solucao = np.dot(Binv, b)
    parcial = np.dot(cb, Binv)

    # determinar variável da nova base:
    baseA = cnb - np.dot(parcial, N)

    # valor para entrar na base:
    cniMin = np.argmin(baseA)

    # checar positividade e imprimir resultados:
    if(all(i>=0 for i in baseA)):
        solucao = solucao[::-1]
        cb = cb[::-1]
        print 'x1 =', solucao[0]
        print 'x2 =', solucao[1]
        print sum(-cb * solucao)
        break # gambiarra

    # checar razões:
    i = ci[cniMin]
    baseR = np.dot(Binv, A[:, i])
    razoes = []
    
    for i in range(0, len(solucao)):
        valA = baseR[i]
        valB = solucao[i]
        razoes.append(valB / valA)

    razaoiMin = np.argmin(razoes)

    #trocar variáveis usando índices e trocar o índice global
    cnb[cniMin], cb[razaoiMin] = cb[razaoiMin], cnb[cniMin]
    ci[cniMin], ci[razaoiMin + tmn_slack] = ci[razaoiMin + tmn_slack], ci[cniMin]
