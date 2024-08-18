while True:
 try:
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero :'))
    operação = input('Digite a o operação')
    resultado = 0


    if operação == '-':
         resultado=num1-num2
    elif operação == '+' :
        resultado = num1 + num2
    elif operação == '/':
        resultado = num1 / num2
    elif operação == '*':
        resultado = num1 * num2
    else:
        print('Comando inavlido,continue')
        continue

    print(f'Seu resultado foi {resultado}')

 except ZeroDivisionError:
    print('Não é possivel fazer a divisão')

 except ValueError:
        print('Por favor, digite números válidos.') 


 sair = input('Quer sair? (s para sim, qualquer outra tecla para não): ').lower()
 if sair.startswith('s'):  
     break


   
