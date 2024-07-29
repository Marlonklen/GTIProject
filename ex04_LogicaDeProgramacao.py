a = int(input('Digite o 1ª lado do triângulo: '))
b = int(input('Digite o 2ª lado do triângulo: '))
c = int(input('Digite o 3ª lado do triângulo: '))

if (a > 0) and (b > 0) and (c > 0):
    if (a + b > c) and (a + c > b) and (b + c > a):
    # se você chegoiu até aqui é porque o triângulo é válido.

        if (a != b) and (a != c):
            print('Triângulo escaleno!')
        elif a == b and a == c:
            print('Triângulo equilátero!')
        else:
            print('Triângulo Isósceles!')
    else:
        print('Ao menos um dos valores indicados não serve para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não serve para formar um triângulo')
