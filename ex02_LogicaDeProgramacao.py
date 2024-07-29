km = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))

valorkm = km * 0.15
ValorDiario = dias * 60

print('O valor total do aluguel por Km é de R${}.'.format(valorkm))
print('O valor total do aluguel pelos dias é de R${}.'.format(ValorDiario))
print('Ovalor total a pagar pelo aluguel do carro é de R${}.'.format(valorkm + ValorDiario))
