import numpy as np
import LU
from math import sqrt

def dot(a,b):
  dp = 0.0

  for i in range(0,len(a)):
    dp = dp + a[i]*b[i]
  return dp

def norm(a):
  return (sqrt(dot(a,a)))

def normalize2(a,an):
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
  

def metodoPotenciaRegularAlternativo(M, x, eps):
  error = float('inf')

  autoValor = 0
  autoVetor = []
  
  preparaAutoVetor(x,autoVetor)
  
  while (error > eps):
    antAutoValor = autoValor
    # Copiar λnovo para λvelho
    normalize2(x, autoVetor)
    #Normalizar o vetor 
    matrixVec(M, autoVetor, x)
    #Calcular o vetor não normalizado,
    autoValor = dot(autoVetor,x)
    #Calcular a nova estimativa de λnovo:
    error = abs( ( antAutoValor - autoValor ) / autoValor )
    #Calcular o erro relativo para verificar a convergência
  
  normalize2(x, autoVetor)
  
  return (autoValor, autoVetor)

def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

def metodoPotenciaRegular(M, x, eps):  
  error = float('inf')

  autoValor = 0
  autoVetor = x

  while (error > eps):
    antAutoValor = autoValor
    autoVetor = np.dot(M, autoVetor)
    autoValor, autoVetor = normalize(autoVetor)
    error = abs( ( antAutoValor - autoValor ) / autoValor )

  
  return (autoValor, autoVetor)

def metodoPotenciaInversa(M, x, eps):
  (L, U) = LU.LU(M)
  
  error = float('inf')
  antAutoValor = 0
  x = x / np.linalg.norm(x)
  y = LU.resolutionLU(L, U, x)

  autoValor = ( x.transpose() @ y )
  autoVetor = x

  while (error > eps):
    antAutoValor = autoValor
    x = y / np.linalg.norm(y)
    y = LU.resolutionLU(L, U, x)
    autoValor = ( x.transpose() @ y )

    error = abs( ( antAutoValor - autoValor ) / autoValor )


  autoValor = 1.0 / autoValor
  autoVetor = y / np.linalg.norm(y)
  
  return (autoValor, autoVetor)

def metodoPotenciaDeslocamento(M, x, eps, u):
  Mlinha = M - u*np.identity(M.shape[0])
  (autoValorlinha, autoVetorlinha) = metodoPotenciaInversa(Mlinha,x,eps)
  
  autoValor = autoValorlinha + u

  return (autoValor, autoVetorlinha)
