#IMPORTA O MODÚLO
'''from modulo import calcular_circulo

#entrada de dados (import modulo)
b = int(input('Informe o valor da base: '))
h = int(input('Informe o valor da altura: '))

print(f'Área do quadrilatero: {modulo.calcular_quadrilatero (b,h)}')

#entrada de dados
r = float(input('Informe o valor do raio: '))

#exibe a área da circunferência
print(f'Área do cículo: {calcular_circulo(r)}.') '''

import modulo

#faz as importações principal
if __name__ == '__main__':
    while True:
        modulo.exibir_menu()
        opcao =input('Opção desejada: ')

        match opcao:
            case '1':
                b = int(input('Base do quadrilatéro: '))
                h = int(input('Altura do quadrilatério: '))
                print(f'Área: {modulo.calcular_quadrilatero(b,h)}')
                continue
            case '2':
                r = int(input('Raio do círculo: '))
                print(f' Área: {modulo.calcular_circulo(r)}')
                continue
            case '3':
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f' Área: {modulo.calcular_triangulo(b,h)}')
                continue
            case '4':
                b_menor = int(input('Base menor do trapézio: '))
                b_maior = int(input('Base maior do trapézio: '))
                h = int(input('Altura do trapézio: '))
                print(f' Área: {modulo.calcular_trapezio(b_menor, b_maior, h)}')
            case '5':
                print('Saindo do programa')
                break
