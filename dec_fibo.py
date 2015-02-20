__author__ = 'ramon'


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def decrypt(encripted_word):
    word = ''
    for i in range(1, len(encripted_word)+1):
        if (ord(encripted_word[i-1]) >= 97) and (ord(encripted_word[i-1]) <= 122):
            char = ord(encripted_word[i-1]) - fibonacci(i)
            #keeping char on boundaries
            while char < 97:
                char += 26
            word += chr(char)
        else:
            word += encripted_word[i-1]
    return word


encripted_word = input("Palabra a desencriptar: ")
print(decrypt(encripted_word))
input("Presione ENTER para salir")