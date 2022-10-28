l1 = int(input('Digite o valor do primeiro lado do triângulo: '))
l2 = int(input('Digite o valor do segundo lado do triângulo: '))
l3 = int(input('Digite o valor do terceiro lado do triângulo: '))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    if l1 == l2 == l3:
        print('Os lados são de um triângulo equilátero.')
    elif l1 != l2 and l1 != l2 and l2 != l3:
        print ('Os lados são de um triângulo escaleno.')
    else:
        print('Os lados são de um triângulo isósceles.')
else:
    print('Os valores não formam um triângulo.')