__author__ = 'Ramon'


def compare(s1, s2):
    min_len = min(len(s1), len(s2))
    counter = 0
    for i in range(min_len):
        if s1[i] == s2[i]:
            counter += 1
        else:
            break
    return s1[:counter], counter


def compare2(s1, s2):
    i = 0
    while s1[i] == s2[i]:
        i += 1
    return s1[:i], i


def compare3(s1, s2):
    min_len = min(len(s1), len(s2))
    #print(s1, s2, min_len)
    if s1[:min_len] == s2[:min_len]:
        return s1[:min_len], min_len
    return compare3(s1[:min_len-1], s2[:min_len-1])

print(compare("C:\Python34\python.exe D:/projects/Python/1st/1stTime/compare_words.py",
              "C:\Python34\python.exe D:/projects/Python/1st/1stTime/compare_words.c"))  # O(n)
print(compare2("C:\Python34\python.exe D:/projects/Python/1st/1stTime/compare_words.py",
               "C:\Python34\python.exe D:/projects/Python/1st/1stTime/compare_words.c"))  # O(n)
print(compare3("C:\Python34\python.exe D:/projects/Python/1st/1stTime/compare_words.py",
               "C:\Python34\python.exe D:/projects/Python/1st/1stTime/compare_words.c"))  # O(log(n))