# Módulo word_functions:
feedback(word, secret_word): Gera feedback colorido para cada letra na tentativa (word) comparada à palavra secreta (secret_word).
corret_length(word): Verifica se o comprimento da palavra é 5 letras.
get_secret_word(): Escolhe aleatoriamente uma palavra do arquivo "words.txt" e a retorna em letras minúsculas.
check_word(word): Verifica se a palavra já foi utilizada, consultando o arquivo "drawn_words.txt".
add_word(word): Adiciona a palavra ao arquivo "drawn_words.txt".
clean_draw_words(): Limpa o conteúdo do arquivo "drawn_words.txt".

# Módulo utilities:
input_word(mensage, kick_list): Solicita ao usuário uma palavra, garantindo que seja válida, de 5 letras e não repetida.

# Módulo game:
menu(): Exibe opções de jogo.
start_solo(): Inicia um jogo solo, onde o jogador tenta adivinhar uma palavra de 5 letras.
start_dueto(): Inicia um jogo de dueto com dois jogadores tentando adivinhar duas palavras de 5 letras.
start_quarteto(): Inicia um jogo de quarteto com quatro jogadores tentando adivinhar quatro palavras de 5 letras.
main(): Função principal que interage com o usuário, oferecendo opções de jogo e gerenciando o fluxo do programa.


O código utiliza variáveis como secret_word, kick_list, counter, list_secret_words e outras para armazenar informações relevantes durante o jogo, como palavras secretas, tentativas e feedbacks. A estrutura modular facilita a manutenção e compreensão do código, proporcionando uma experiência interativa de jogo de palavras em Python.
