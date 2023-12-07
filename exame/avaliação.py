while True:
#while foi usado pra deixar o codigo rodando até colocar um NUMERO de 0 a 10
    try:
        numero=float(input("Digite sua avaliação: "))
        
        assert   0 <= numero <= 10, "De 0 a 10, por favor."
        print(f"Avaliação do produto {numero}/10")
        break

    except AssertionError as e:
        print(e)
    except ValueError:
        print("Digite um Número de 0 a 10.")
