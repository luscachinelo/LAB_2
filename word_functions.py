import random


def feedback(word, secret_word):
    feedback = ''
    for i in range(len(secret_word)):
        if word[i] == secret_word[i]:
            feedback += '\033[92m' + word[i] + '\033[0m'  # Verde
        elif word[i] in secret_word:
            feedback += '\033[93m' + word[i] + '\033[0m'  # Amarelo
        else:
            feedback += '\033[97m' + word[i] + '\033[0m'  # Branco
    
    if secret_word == word:
        return feedback, True, word

    return feedback, False

def corret_length(word):
    if len(word) == 5:
        return True
    
    return False

def get_secret_word(): 

    file = open("words.txt", "r")

    lines = file.read().split('\n')

    secret_word = random.choice(lines)

    file.close()
    return secret_word.lower()

def check_word(word):

    file = open('drawn_words.txt', 'r') 
    if word in file: 
        file.close()
        return False
    file.close()
    return True

def add_word(word): 

    file = open('drawn_words.txt', 'a')
    
    file.write(str(f'{word}\n'))

    file.close()

    return True

def clean_draw_words():
  
    file = open('drawn_words.txt', 'w')

    file.close ()

    return True
