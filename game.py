import utilities
import word_functions

def menu():
    print("1- Iniciar Solo. ")
    print("2- Iniciar Dueto.")
    print("3- Iniciar Quarteto. ")
    print("4- Encerrar Programa.")
    print("5- Resetar palavras. ")

def start_solo():
    while True:
            secret_word = word_functions.get_secret_word()

            if word_functions.check_word(secret_word):
                break
        
    kick_list = []
    for _ in range(5):
        
        kick = utilities.input_word("Digite seu palpite:", kick_list)[0]

        feedback = word_functions.feedback(kick, secret_word)
        print(feedback[0])

        if kick == secret_word:
            word_functions.add_word(secret_word)
            print("Parabens você acertou!")
            return True
    
    print("Não foi dessa vez, tente na proxima 😉")
    return False

def start_dueto():
    #6 tentativas 2 palavras
    counter = 2
    list_secret_words = []
    original_list = []

    while counter > 0:
            secret_word = word_functions.get_secret_word()

            if word_functions.check_word(secret_word) and secret_word not in list_secret_words:
                counter -= 1
                list_secret_words.append(secret_word)
                original_list.append(secret_word)

    remove = 0
    kick_list = []
    result_list = []
    for _ in range(6):

        kick = utilities.input_word("Digite seu palpite:", kick_list)[0]
        
        list_feedback = []
        for x in range(len(list_secret_words)):
            feedback = word_functions.feedback(kick, list_secret_words[x])
            if feedback[1]:
                result_list.append([feedback[0], feedback[2]])
                remove = list_secret_words[x]
            list_feedback.append(feedback[0])

        if remove != 0:
            list_secret_words.remove(remove)
            remove = 0

        if len(list_feedback) == 2:
            print (f"{list_feedback[0]} \t\t {list_feedback[1]}")

        elif len(list_feedback) == 1: 
            print(f"{result_list[0][0]} \t\t {list_feedback[0]}")
           
        else:
            print(f"{result_list[0][0]} \t\t {result_list[1][0]}")

        if len(result_list) == 2:
            word_functions.add_word(original_list[0])
            word_functions.add_word(original_list[1])
            print("Parabens você acertou!")
            return True
    print("Não foi dessa vez tente na proxima.")
    return False

def start_quarteto():
    #8 tentativas 4 palavras
    counter = 4
    list_secret_words = []
    original_list = []

    while counter > 0:
            secret_word = word_functions.get_secret_word()

            if word_functions.check_word(secret_word) and secret_word not in list_secret_words:
                counter -= 1
                list_secret_words.append(secret_word)
                original_list.append(secret_word)

    remove = 0
    kick_list = []
    result_list = []
    for _ in range(8):

        kick = utilities.input_word("Digite seu palpite:", kick_list)[0]
        
        list_feedback = []
        for x in range(len(list_secret_words)):
            feedback = word_functions.feedback(kick, list_secret_words[x])
            if feedback[1]:
                result_list.append([feedback[0], feedback[2]])
                remove = list_secret_words[x]
            list_feedback.append(feedback[0])

        if remove != 0:
            list_secret_words.remove(remove)
            remove = 0

        if len(list_feedback) == 4:# se tem 4 feedback
            print (f"{list_feedback[0]} \t\t {list_feedback[1]} \n{list_feedback[2]} \t\t {list_feedback[3]}")

        elif len(list_feedback) == 3: #se tem 3 feedback
            print(f"{result_list[0][0]} \t\t {list_feedback[0]} \n{list_feedback[1]} \t\t {list_feedback[2]}")

        elif len(list_feedback) == 2: #se tem 2 feedback
            print(f"{result_list[0][0]} \t\t {result_list[1][0]} \n{list_feedback[0]} \t\t {list_feedback[1]}")

        elif len(list_feedback) == 1: #se tem 1 feedback
            print(f"{result_list[0][0]} \t\t {result_list[1][0]} \n{result_list[2][0]} \t\t {list_feedback[0]}")

        else:
            print(f"{result_list[0][0]} \t\t {result_list[1][0]} \n{result_list[2][0]} \t\t {result_list[3][0]}")

        if len(result_list) == 4:
            word_functions.add_word(original_list[0])
            word_functions.add_word(original_list[1])
            word_functions.add_word(original_list[2])
            word_functions.add_word(original_list[3])
            print("Parabens você acertou!")
            return True
    print("Não foi dessa vez tente na proxima.")
    return False



