# Exercício pratico utilizando os conceitos de listas e outros já aprendidos.

palavra_secreta = 'jogador'
print(' Jogo de adivinhação.\n Tente a sorte e adivinhe a palavra secreta letra por letra. :D')
digitadas = []
dica = len(palavra_secreta)
print(f' A palavra possui {dica} letras')
chances = 3
while True:
    if chances <= 0:
        print(' GAME OVER. ')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Vigarista é uma letra de cada vez!!! Tenta de novo.')
        continue
    digitadas.append(letra)
    if letra in palavra_secreta:
        print(f'Boa! A letra {letra} existe na palavra secreta.')
    else:
        print(f' A letra {letra} não existe na palavra secreta.')
        digitadas.pop()
    segredo_temp = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            segredo_temp += letra_secreta
        else:
            segredo_temp += '*'
    print(F'o que você ja descobriu: {segredo_temp}')
    if segredo_temp == palavra_secreta:
        print('Parabéns você descobriu a palavra secreta.')
        print(f'A palavra secreta é {palavra_secreta}. ')
        break
    if letra not in palavra_secreta:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
