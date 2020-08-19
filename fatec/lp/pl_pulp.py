from pulp import *
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
problem = pulp.LpProblem("Lista 2, Exercício 3:", pulp.LpMaximize)
problem += x + 2*y, "Função Objetivo:"
problem += 7*x + 9*y <= 63, "Restrição 1:"
problem += 11*x + 5*y <= 55, "Restrição 2:"
problem += x <= 4, "Restrição 3:"
problem.solve()
print ("Resultado Ótimo:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Lucro Máximo:")
print (value(problem.objective))
