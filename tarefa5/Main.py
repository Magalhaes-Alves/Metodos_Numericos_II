a1 = -0.861136311
a2 = -0.339981043
a3 = 0.339981043
a4 = 0.861136311

a= [a1,a2,a3,a4]

valor = 1

for i in range(4):
    if(i!=1):
        valor= valor* (a[1] - a[i])
        print(str(valor) + "  " + str(i))

print(valor)