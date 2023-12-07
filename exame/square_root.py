class NegativeNumberError(Exception):
   pass

def calculate_square_root(num ):  
        resultado= num  ** (1/2)
        return resultado

def main():
    while True:
        try:
            num =int(input("Digite um número inteiro: "))
            if num  < 0:
                raise NegativeNumberError("O valor fornecido é negativo")

            break      
        
        except NegativeNumberError as e:
            print(e)
        
        except ValueError as e:
            print(e)        
        
    print(f"O resultado é: {calculate_square_root(num )}")

main()
