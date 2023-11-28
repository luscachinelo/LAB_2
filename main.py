import word_functions
import utilities
import game

def main ():

    while True:
        game.menu()
        option = input("Digite sua opção: ")
        if option == '1':
            game.start_solo()

        elif option == '2':
            game.start_dueto()

        elif option == '3':
            game.start_quarteto()
        
        elif option == '5':
            word_functions.clean_draw_words()
            print("Palavras resetadas.")
        
        elif option == '4':
            word_functions.clean_draw_words()
            break

        else:
            print("Opção invalida tente novamente.")

print("Programa encerrado.")
    
main()