def corret_length(word):
    if len(word) == 5:
        return True
    
    return False

def input_word(mensage, kick_list):
    while True:
        kick = input(mensage)
        if not kick.isalpha():
            print("Digite uma palavra sem espaços e sem numeros.")
            continue

        if not corret_length(kick):
            print("Digite uma palavra de 5 letras.")
            continue
            
        elif kick in kick_list:
            print("Você ja digitou essa palavra.")    
            continue

        kick_list.append(kick)
        break
    return kick, kick_list