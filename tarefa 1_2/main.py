import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def convolution(image, kernel, average=False, mostrarProcesso=False):
    if len(image.shape) == 3:
        print(f"Encontrado 3 canais : {image.shape}")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f"Convertendo para escala de cinza. Tamanho: {image.shape}")
    else:
        print(f"Dimensões da Imagem : {image.shape}")
 
    print(f"Dimensões do Filtro : {kernel.shape}")
 
    if mostrarProcesso:
        plt.imshow(image, cmap='gray')
        plt.title("Imagem")
        plt.show()
 
    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape
 
    output = np.zeros(image.shape)
 
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)
 
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
 
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image
 
    if mostrarProcesso:
        plt.imshow(padded_image, cmap='gray')
        plt.title("Imagem Ampliada")
        plt.show()
 
    for row in range(image_row):
        for col in range(image_col):
            output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])
            if average:
                output[row, col] /= kernel.shape[0] * kernel.shape[1]
 
    print(f"Tamanho da imagem de saida : {output.shape}")
 
    if mostrarProcesso:
        plt.imshow(output, cmap='gray')
        plt.title(f"Imagem de saída usando Filtro {kernel_row}X{kernel_col}")
        plt.show()
 
    return output

def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)

  
def gaussian_kernel(size, sigma=1, mostrarProcesso=False):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)
 
    kernel_2D *= 1.0 / kernel_2D.max()
 
    if mostrarProcesso:
        plt.imshow(kernel_2D, interpolation='none', cmap='gray')
        plt.title(f"Filtro ( {size}X{size} )")
        plt.show()
 
    return kernel_2D

 
def gaussian_blur(image, kernel_size, mostrarProcesso=False):
    kernel = gaussian_kernel(kernel_size, sigma=sqrt(kernel_size), mostrarProcesso=mostrarProcesso)
    return convolution(image, kernel, average=True, mostrarProcesso=mostrarProcesso)
 

def aplicando_mascara_derivacao_central(img):
    colunas,linhas = img.shape

    #Criando uma imagem ampliada com 2 pixels a mais na horizontal e na vertical
    paddedimage = np.zeros((colunas+2,linhas+2))
    paddedimage[1:colunas+1,1:linhas+1] = img

    matrizA = np.zeros(img.shape)
    matrizB = np.zeros(img.shape)
    matrizC = np.zeros(img.shape)
    matrizD = np.zeros(img.shape)

    #Usando a derivação central na horizontal e vertical e salvando em suas respectivas matrizes
    for linha in range(1,linhas-1):
        for coluna in range(1,colunas-1):
            matrizA[coluna, linha] = abs((paddedimage[coluna, linha+1] - paddedimage[coluna, linha-1])/2)
            matrizB[coluna, linha] = abs( (paddedimage[coluna+1, linha] - paddedimage[coluna-1, linha])/2 )

    matrizC =np.sqrt( np.square(matrizA) + np.square(matrizB) )

    e = 0.5
    #fazendo a análise do e
    matrizD = np.where(matrizC >e, 1, 0)
    
    return matrizD


def aplicando_laplace(img):
    colunas,linhas = img.shape

    #Criando uma imagem ampliada com 2 pixels a mais na horizontal e na vertical
    paddedimage = np.zeros((colunas+2,linhas+2))
    paddedimage[1:colunas+1,1:linhas+1] = img

    matrizA = np.zeros(img.shape)
    matrizB = np.zeros(img.shape)
    #Usando a derivação central na horizontal e vertical e salvando em suas respectivas matrizes
    for linha in range(1,linhas-1):
        for coluna in range(1,colunas-1):
            matrizA[coluna, linha] = abs((paddedimage[coluna, linha+1] - 2*paddedimage[coluna, linha] + paddedimage[coluna, linha-1])/4 ) + abs( (paddedimage[coluna+1, linha] - 2*paddedimage[coluna, linha] + paddedimage[coluna-1, linha])/4 )

    e = 0.0001
    #fazendo a análise do e
    matrizB = np.where( np.around(matrizA, 1) !=0, 1, 0)
    
    return matrizB


def aplicando_laplace2(img):
    colunas,linhas = img.shape

    #Criando uma imagem ampliada com 2 pixels a mais na horizontal e na vertical
    paddedimage = np.zeros((colunas+4,linhas+4))
    paddedimage[2:colunas+2,2:linhas+2] = img

    matrizA = np.zeros(img.shape)
    matrizB = np.zeros(img.shape)

    #Usando a derivação central na horizontal e vertical e salvando em suas respectivas matrizes
    for linha in range(2,linhas):
        for coluna in range(2,colunas):
            matrizA[coluna, linha] = abs((- paddedimage[coluna,linha+2] + 16*paddedimage[coluna, linha+1] - 30*paddedimage[coluna, linha] + 16*paddedimage[coluna, linha-1] - paddedimage[coluna,linha -2])/12 ) + abs(( - paddedimage[coluna+2,linha] + 16*paddedimage[coluna+1, linha] - 30*paddedimage[coluna, linha] + 16*paddedimage[coluna-1, linha] - paddedimage[coluna-2,linha])/12 )

    e = 0.0001
    #fazendo a análise do e
    matrizB = np.where( np.around(matrizA, 4) >0.0000, 1, 0)
    
    return matrizB


caminho = input('Digite o caminho da imagem com a sua extensão:')

img = (cv2.imread(caminho))

print("Digite 1 para aplicar o filtro gaussiano e depois a detecção de arestas do alg1")
print("Digite 2 para aplicar o filtro gaussiano e depois a detecção de arestas do alg2")
escolha = int(input("Digite o que você deseja:"))


imgFiltrada = gaussian_blur(img, 5, mostrarProcesso = False)

if(escolha==1):
    imgFiltrada = aplicando_mascara_derivacao_central(imgFiltrada)
else:
    imgFiltrada = aplicando_laplace2(imgFiltrada)


plt.imshow(imgFiltrada, cmap = 'gray')
plt.title("Imagem Filtrada")
plt.show()
