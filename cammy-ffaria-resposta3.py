print('Tarifa de taxi \n')

def bandeira1(quilometros):
    tarifa = 4.5
    preco_por_km = 2.75
    total = tarifa + (preco_por_km * quilometros)
    return total


def bandeira2(quilometros):
    tarifa = 5.85
    preco_por_km = 3.5
    total = tarifa + (preco_por_km * quilometros)
    return total


def main():
    dia = input('Digite o dia da semana: ').strip().lower() #strip limpa todos os espaços em
    # branco no final da string e lower converte fodas as caixas de texto para baixas
    horario = input('Digite o horário de início da corrida (exemplo: 7:00; 22:35): ').strip()
    quilometros = float(input('Digite a quantidade de quilômetros percorridos: ').replace (',','.'))

    horas, minutos = map(int, horario.split(':')) #divide o horário em horas e minutos
    horario_decimal = horas + minutos / 60

    if dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado','segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','segunda feira','terca feira','quarta feira','quinta feira','sexta feira']:
        if 6 <= horario_decimal < 20:
            total = bandeira1(quilometros)
            bandeira = 'Bandeira 1'
        else:
            total = bandeira2(quilometros)
            bandeira = 'Bandeira 2'
    else:
        total = bandeira2(quilometros)
        bandeira = 'Bandeira 2'

    print(f'\nBandeira usada: {bandeira}')
    print(f'Valor total da corrida: R$ {total:.2f}')


if __name__ == '__main__':
    main()
