preco = float(input('digite o preco de um produto: '))
p = float(input('Digite o desconto a ser aplicado: '))

desconto = preco * (p / 100)
final = preco - desconto
print('O preço do desconto {}. Desconto de {}%'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))