print('Calcule a hipotenusa\n')  # O programa mostra ao usuário o que será resultado de sua interação

import math  # Função usada para algumas operações matemáticas

def hipotenusa():
    lado1 = float(input('Digite lado 01: ').replace(',', '.'))
    lado2 = float(input('Digite lado 02: ').replace(',', '.'))
    resultado = math.sqrt(lado1**2 + lado2**2)  # Cálculo da hipotenusa. "sqrt" significa "square root", ou seja, raíz
    # quadrada
    return lado1, lado2, resultado

for i in range(1565): #pede para o código ser repetido em loop por 1565 vezes
    lado1, lado2, resultado_hipotenusa = hipotenusa()
    print('\nVocê digitou', lado1, 'para lado 01 e', lado2, 'para lado 02. \n\nO valor da hipotenusa é:', resultado_hipotenusa)  # Exibe o resultado

print('\n\n') #duas quebras de linha inseridas apenas para ficar mais organizado
hipotenusa()
