n = int(input('Quantos elementos da sequência de Fibonacci você deseja imprimir? '))
f0 = 0
f1 = 1
f2 = 1
s = 2
print(f0)
print(f1)
while s <= n:
    f2 = f1
    f1 += f0
    f0 = f2
    print(f1)
    s += 1