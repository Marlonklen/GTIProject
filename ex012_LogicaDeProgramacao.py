palavras = ('mario', 'luigi', 'peach', 'yoshi', 'bowser')
for palavra in palavras:
    print('\nPalavra: {} Vogais:'.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
