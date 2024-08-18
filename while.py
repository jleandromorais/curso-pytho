contador = 0

while contador < 100:
    contador += 1
    
    if contador == 6:
        print('N vou exibir o 6 na tela')
        continue
    

    if contador >10 and contador<27:
        print('Não vou mostrar o contador',contador)
        continue
    print(contador)
    if contador == 40 :
        print('Esta no numero 4')
        break
 

print ('Acabou ')