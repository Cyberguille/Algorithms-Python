__author__ = 'ramon'


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def encrypt(word):
    encripted_word = ''
    for i in range(1, len(word)+1):
        if (ord(word[i-1]) >= 97) and (ord(word[i-1]) <= 122):
            char = ord(word[i-1]) + fibonacci(i)
            #keeping char on boundaries
            while char > 122:
                char -= 26
            encripted_word += chr(char)
        else:
            encripted_word += word[i-1]
    return encripted_word


word = input("Palabra a encriptar: ")
print(encrypt(word))
input("Presione ENTER para salir")
