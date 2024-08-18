nome = input('Digite seu nome ')
idade = input('Digite sua idade')
nome_inverso = nome[::-1]
ultima_letra = nome[-1]
primeira_letra = nome[0]
if not nome or not idade:
    print("Desculpe,voce deixou campos vazios") 
   
else:

    print(f'Seu nome é:{nome}')
    print (f'seu nome invertido é: {nome_inverso}')
    print(f'Ultima letra do seu nome é:{ultima_letra}')
    print(f'primeira letra é:{primeira_letra}')
    print(f'Seu nome tem essa  quantidade :{len(nome)}')
