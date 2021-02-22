# Шифр цезаря
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890'
method = ['зашифровать', 'з', 'дешифровать', 'д']
max_key_size = len(alphabet)
result = ''

def getInputData():
    while True:
        try:
            mode = input('Зашифровать или Дешифровать? Введите "д" или "з": ').lower()
            if mode in method:
                return mode
            else:
                print('Введите правильное значение')
        except:
            print('Введите правильное значение!')


def getKey():
    while True:
        key = int(input(f'Введите смещение текста, значение от 1 до {len(alphabet)}'))
        if 1 <= key <= len(alphabet):
            return key
        else:
            print('Введите корректное значение! ')


def encrypt(mode, key):
    global result
    text = input('Введите ваш текст для конвертации! ')
    if mode[0] == 'д':
        key = -key

    for symbol in text:
        index = alphabet.find(symbol)
        if index == - 1:
            result +=symbol
        else:
            index += key

            if index >= max_key_size:
                index -= max_key_size
            elif index <= 0:
                index += max_key_size

            result += alphabet[index]

    return result


mode = getInputData()
key = getKey()
print(f'Конвертированный текст: {encrypt(mode, key)}')
