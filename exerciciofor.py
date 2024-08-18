
        

    
nome = 'jose'
letras_corretas = ''
numero_tentativa = 0

while True:
    letra = input('Digite uma letra para adivinhar:').lower()

    if len(letra) > 1:
        print('Você digitou mais de uma letra, digite novamente.')
        continue

    numero_tentativa += 1

    if letra in nome:
        if letra not in letras_corretas:
            letras_corretas += letra
        print('Você acertou uma letra!')
    else:
        print('*')

    palavra_formada = ''
    for letra_secreta in nome:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == nome:
        print(f'Você ganhou! A palavra é: {nome}')
        print(f'Número de tentativas: {numero_tentativa}')
        break
