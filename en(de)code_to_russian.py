codes = {
    'a': 'а',
    'b': 'б',
    'c': 'ц',
    'd': 'д',
    'e': 'ё',
    'f': 'ф',
    'g': 'г',
    'h': 'х',
    'i': 'и',
    'j': 'й',
    'k': 'к',
    'l': 'л',
    'm': 'м',
    'n': 'н',
    'o': 'о',
    'p': 'п',
    'q': 'я',
    'r': 'р',
    's': 'с',
    't': 'т',
    'u': 'у',
    'v': 'ж',
    'w': 'в',
    'x': 'ь',
    'y': 'ы',
    'z': 'з',
    }
def findVal(myVal):
    for key in codes.keys():
        if codes[key] == myVal:
            return key
    else:
        return -1
def encode(str):
    list = []
    for char in str:
        if char in codes:
            list.append(codes[char])
        else:
            list.append(char)
    with open('ciphertext.txt','w') as newfile:
        for item in list:
            newfile.write(item)
def decode(str):
    list = []
    for char in str:
        if findVal(char) != -1:
            list.append(findVal(char))
        else:
            list.append(char)
    with open('plaintext.txt','w') as newfile:
        for item in list:
            newfile.write(item)
with open('text.txt') as file:
    text = file.read()
    text = text.lower()
    encode(text)
    decode(text)
