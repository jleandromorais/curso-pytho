frase = 'python é a linguagem mais utilizada em progamação'\
'ela é interesante e audaz'

i = 0 
apereceu_mais_vezes = 0
letra_apareceu_mais = ''

   

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue

    if apereceu_mais_vezes < quantas_vezes_apareceu:
        apereceu_mais_vezes = quantas_vezes_apareceu
        letra_apareceu_Mais = letra_atual
    
    i += 1
    

print(f"A letra que apareceu mais foi '{letra_apareceu_Mais}' e apareceu {apereceu_mais_vezes} vezes.")

    