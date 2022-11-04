# Инициализация S-блока
def init_s_block(key):
    s_box = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    return s_box


# Генерация псевдослучайного слова K + Операция суммирования по модулю два XOR
def K_XOR(plain, box):
    res = []
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(chr(ord(s) ^ k))

    cipher = "".join(res)
    return cipher

# Зашифровка
def encryption(Mi, box):
    print("Полученный шифротекст:")
    Ci = K_XOR(Mi, box)  # Ci = Mi ⊕ Ki
    print(Ci)
    return Ci

# Расшифровка
def decryptions(Ci, box):
    print("Полученный исходный текст:")
    Mi = K_XOR(Ci, box)  # Mi = Ci ⊕ Ki = (Mi ⊕ Ki) ⊕ Ki
    print(Mi)


if __name__ == '__main__':
    print("Введите исходный текст:")
    message = input()
    print("Введите секретный ключ:")
    key = input()

    box = init_s_block(key)
    encrypt = encryption(message, box)
    box = init_s_block(key)
    decryptions(encrypt, box)
