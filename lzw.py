from struct import *


def decode(path, n):
    # получение сжатого файла и количество битов из командной строки
    # открытие сжатого файла
    input_file, n = path, n
    file = open(input_file, "rb")
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    string = ""

    # Чтение сжатого файла
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data,) = unpack('>H', rec)
        compressed_data.append(data)

    print(compressed_data)

    # Создание и инициализация словаря
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])
    print(dictionary)

    # перебор кодов
    # Алгоритм LZW
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    # сохранение распакованной строки в файл
    out = input_file.split(".")[0]
    output_file = open(out + "_decoded.txt", "w")
    for data in decompressed_data:
        output_file.write(data)

    output_file.close()
    file.close()


if __name__ == '__main__':
    decode("data2_encoded.txt", 8)
