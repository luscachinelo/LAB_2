def find_element(lista, indice):
    try:
        if 0 <= indice < len(lista):
            return lista[indice]
        else:
            raise IndexError("Índice inválido. Forneça um índice dentro dos limites da lista.")
    except IndexError as e:
        print(e)



frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']

indice_desejado = input("Digite o índice da fruta que você deseja: ")

try:
   
    indice_desejado = int(indice_desejado)
    resultado = find_element(frutas, indice_desejado)
   
   
   
    if resultado is not None:
        print("Você escolheu:", resultado)


except ValueError:
    print("Entrada inválida. Por favor, forneça um número inteiro.")
