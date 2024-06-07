from datetime import date


#função menu
def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro','Novembro', 'Dezembro' )
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    print(f'\n{dia} de {meses[mes - 1]} de {ano}.\n ')
    print('1 - calcular quadrilátero')
    print('2 - calcular círculo')
    print('3 - calcular triângulo')
    print('4 - calcular trapézio')
    print('5 - Sair do progrma')


def calcular_quadrilatero(b,h):
    a = b*h
    return a
#função do circulo(r)
def calcular_circulo(r):
    a = 3.14*r**2
    return a
#função do triangulo
def calcular_triangulo(b,h):
    a = (b*h)/2
    return a
#função do trapezio
def calcular_trapezio(b_menor, b_maior, h):
    a = ((b_menor+b_maior)*h)/2
    return a