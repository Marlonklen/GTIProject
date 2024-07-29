def valida_int(pergunta, min, max):
    """
    Verifica se o valor está entre os parâmetros pedidos.
    :param pergunta: Pede ao usuário a entrada de um parâmetro.
    :param min: Condição mínima de parâmetro.
    :param max: Condição maxima de parâmetro
    :return: Retorna o valor se a uma variável se passar na condição.
    """
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def fatorial(num):
    """
    Calcula o Fatorial de um numero.
    :param num: Número que quer calcular.
    :return: Retorna número em sua forma fatorial.
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat
# programa principal
x = valida_int(input('Dgite um numero para calcular a fatorial: ',0, 999999))
print('{}! = {}'.format(x, fatorial(x)))

