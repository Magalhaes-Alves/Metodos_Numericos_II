import numpy as np
import LU as decomp

def metodoPotenciaInversa(M, x, eps):
  (L, U) = decomp.LU(M)
  
  error = float('inf')
  antAutoValor = 0
  x = x / np.linalg.norm(x)
  y = decomp.resolutionLU(L, U, x)

  autoValor = ( x.transpose() @ y )
  autoVetor = x

  while (error > eps):
    antAutoValor = autoValor
    x = y / np.linalg.norm(y)
    y = decomp.resolutionLU(L, U, x)
    autoValor = ( x.transpose() @ y )

    error = abs( ( antAutoValor - autoValor ) / autoValor )


  autoValor = 1.0 / autoValor
  autoVetor = y / np.linalg.norm(y)
  
  return (autoValor, autoVetor)

