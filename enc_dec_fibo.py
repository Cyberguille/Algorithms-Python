__author__ = 'ramon'


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def encrypt(word):
    encripted_word = ''
    j = 1
    for i in range(1, len(word)+1):
        if (ord(word[i-1]) >= 97) and (ord(word[i-1]) <= 122):
            char = ord(word[i-1]) + fibonacci(j)
            if j == 30:
                j = 1
            else:
                j += 1
            #keeping char on boundaries
            while char > 122:
                char -= 26
            encripted_word += chr(char)
        else:
            encripted_word += word[i-1]
    return encripted_word


def decrypt(encripted_word):
    word = ''
    j = 1
    for i in range(1, len(encripted_word)+1):
        if (ord(encripted_word[i-1]) >= 97) and (ord(encripted_word[i-1]) <= 122):
            char = ord(encripted_word[i-1]) - fibonacci(j)
            if j == 30:
                j = 1
            else:
                j += 1
            #keeping char on boundaries
            while char < 97:
                char += 26
            word += chr(char)
        else:
            word += encripted_word[i-1]
    return word


option = 1
while option == 1 or option == 2:
    option = int(input("Presione 1 para encriptar, 2 para desencriptar y cualquier otro para salir:"))
    if option == 1:
        word = input("Palabra a encriptar: ")
        print(encrypt(word))
    elif option == 2:
        encripted_word = input("Palabra a desencriptar: ")
        print(decrypt(encripted_word))