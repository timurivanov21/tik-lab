def get_data_from_file(path):
    symbols = None
    chances = None
    msg = None
    with open(path) as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                symbols = line
            elif i == 1:
                chances = line
            elif i == 2:
                msg = line

    return symbols.split(), list(map(float, chances.split())), msg


class Node:
    def __init__(self) -> None:
        # для хранения символа
        self.sym = ''
        # для хранения вероятности
        self.pro = 0.0
        # для хранения итогового кода
        self.arr = [0] * 10
        self.top = 0


# функция для поиска кода фано
def fano(l, h, p):
    pack1 = 0
    pack2 = 0
    # проверка на то что у нас осталось два числа и левая граница не превысила правую
    if l + 1 == h or l == h or l > h:
        if l == h or l > h:
            return
        p[h].top += 1
        p[h].arr[p[h].top] = 0
        p[l].top += 1
        p[l].arr[p[l].top] = 1
        return
    else:
        # сумма по вероятностям от l до h
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        # большая вероятность(сверху)
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if diff1 < 0:
            diff1 = diff1 * -1
        # два элемента
        j = 2
        # пока не осталось два элемента
        while j != h - l + 1:
            k = h - j
            pack1 = pack2 = 0
            # собираем сумму от l до k (снизу вверх)
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].pro
            # собираем сумму от h до k (сверху вниз)
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if diff2 < 0:
                diff2 = diff2 * -1
            if diff2 >= diff1:
                break
            diff1 = diff2
            j += 1

        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 1

        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].arr[p[i].top] = 0

        fano(l, k, p)
        fano(k + 1, h, p)


def sort_by_probability(n, p):
    temp = Node()
    for j in range(1, n):
        for i in range(n - 1):
            if p[i].pro > p[i + 1].pro:
                temp.pro = p[i].pro
                temp.sym = p[i].sym

                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym

                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym


def display(n, p, msg):
    print("Символ\tВероятность\tКод", end='')
    for i in range(n - 1, -1, -1):
        print("\n", p[i].sym, "\t\t", p[i].pro, "\t\t", end='')
        for j in range(p[i].top + 1):
            print(p[i].arr[j], end='')

    print("\n\nИтоговый код")
    result = ""
    for symbol in msg:
        for i in range(len(p)):
            if p[i].sym == symbol:
                for j in range(p[i].top + 1):
                    result += str(p[i].arr[j])
    print(result)


def main():
    symbols, chances, msg = get_data_from_file('data.txt')
    print("АГОРИТМ ФАНО")
    print(symbols)
    print(chances)
    print(msg)
    print("")
    n = len(symbols)
    p = [Node() for _ in range(n)]
    total = 0

    for i in range(n):
        # Вставляем символ в узел
        p[i].sym += symbols[i]

    for i in range(n):
        # Вставляем значение в узел
        p[i].pro = chances[i]
        total = total + p[i].pro

    # проверка максимальной вероятности
    if total != 1:
        raise Exception('Суммарная вероятность не равна 1, введите другие значения')

    # Сортировка символов по их вероятности
    sort_by_probability(n, p)

    for i in range(n):
        p[i].top = -1

    # Находим код фано
    fano(0, n - 1, p)

    # Выводим код
    display(n, p, msg)


if __name__ == '__main__':
    main()
