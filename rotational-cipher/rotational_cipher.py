def rotate(text, key):
    s=''
    listword = []

    for element in text:
        number = ord(element)
        number += key
        char = chr(number)
        listword.append(char)

    print(s.join(listword))
    
rotate("John", 6)