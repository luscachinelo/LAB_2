try:
    # Aqui repete quando der erro, exemplo, o maluco coloca uma string.
    a=float(input("Digite o primeiro lado do triangulo: "))
    b=float(input("Digite o segundo lado do triangulo: "))    
    c=float(input("Digite o terceiro lado do triangulo: "))
except ValueError:
    print("Digite um número válido para um triangulo.")
    #eu dou a exceção que eu quero tratar, e possivelmente pode dar erro.
def type_triangle(a, b, c):
    if a == b == c:
        print("Esse triangulo é um Equilátero")
        # Esse é um triangulo que tem todos os lados iguais.
    elif a == b or c == b or a == c:
        print("Esse triangulo é um Isósceles")
        # Esse triangulo é o que tem dois dos lados iguais.
    else:
        print("Esse triangulo é um Escaleno")
        # Esse triangulo é o que tem todos os lados diferentes.
type_triangle(a, b, c)
