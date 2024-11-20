print('Frete \n')  # O programa mostra ao usuário o que será resultado de sua interação

def frete():
    total = int(input('Digite quantidade de produtos adquiridos: '))
    p1 = 10.95  # valor de referência do primeiro produto
    p2 = total * 2.95  # valor do frete considerando que cada item adquirido vale R$2,95
    fr = p1 + (total - 1) * 2.95  # o primeiro item custa R$10,95 e cada item adicional custa R$2,95.
    # total-1 significa que o programa vai considerar um item entre todos os adquiridos custando R$10,95 e separá-lo
    # dos demais que custa R$2,95 cada um | leva em conta que a multiplicação é feita antes da soma
    return total, p1, p2, fr

for i in range(1565):  # pede para o código ser repetido em loop por 1565 vezes
    total, p1, p2, fr = frete()
    print(f'\nSeu frete é de: R${fr:.2f}\n\n')  # .2f é uma formatação para duas casas decimais, para considerar o
    # valor dos centavos

