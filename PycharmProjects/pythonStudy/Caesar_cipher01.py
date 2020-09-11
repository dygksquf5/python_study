def makebook():
    encbook = {}
    decbook = {}

    for i in range(0, 26):
        key = chr(65 + i)
        value = i
        encbook[key] = value

    for i in encbook:
        key = encbook[i]
        value = i
        decbook[key] = value

    return encbook, decbook


# print(makebook())


def caesar(msg, key, encbook, decbook, isDec):
    returntText = ''
    for i in msg.upper():
        if i in encbook:
            translated = (encbook[i] + key) % 26
            if isDec:
                returntText += decbook[translated].lower()
            else:
                returntText += decbook[translated]
        else:
            returntText += i  # 이거 띄어쓰기 가능!!왜냐면 공간도 문자열로 인식함 파이썬이! 그렇기때문에 알파벳에 없는 빈 공백을 else 로 적

    return returntText


def main():
    encbook, decbook = makebook()

    plaintext = 'nice to meet you'
    key = 5

    ciphertext = caesar(plaintext, key, encbook, decbook, False)
    decrypted = caesar(ciphertext, -key, encbook, decbook, True)

    print('Plaintext  :', plaintext)
    print('Ciphertext :', ciphertext)
    print('Decrypted  :', decrypted)


print(main())


