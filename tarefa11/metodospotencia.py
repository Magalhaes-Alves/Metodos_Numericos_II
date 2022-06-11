from math import sqrt

def dot(a,b):
  dp = 0.0

  for i in range(0,len(a)):
    dp = dp + a[i]*b[i]
  return dp

def norm(a):
  return (sqrt(dot(a,a)))

def normalize(a,an):
  l = norm(a)

  for i in range(0, len(a)):
    an[i] = a[i]/l
  

def matrixVec(M, a, b):

  for i in range(0,len(M)):
    s = 0.0
    for k in range(0,len(M)):
      s = s + M[i][k]*a[k]
    b[i] = s

def preparaAutoVetor(x,autovetor):
  n = len(x)

  for i in range(0,n):
    autovetor.append(0)
  

def metodoPotenciaInversa(M, x, eps):
  error = float('inf')

  autoValor = 0
  autoVetor = []
  
  preparaAutoVetor(x,autoVetor)
  
  while (error > eps):
    antAutoValor = autoValor
    # Copiar λnovo para λvelho
    normalize(x, autoVetor)
    #Normalizar o vetor 
    matrixVec(M, autoVetor, x)
    #Calcular o vetor não normalizado,
    autoValor = dot(autoVetor,x)
    #Calcular a nova estimativa de λnovo:
    error = abs( ( antAutoValor - autoValor ) / autoValor )
    #Calcular o erro relativo para verificar a convergência
  
  normalize(x, autoVetor)
  
  return (autoValor, autoVetor)
