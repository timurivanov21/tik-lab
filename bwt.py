from operator import itemgetter


def bw_restore(index_, transform_msg):
    n = len(transform_msg)
    list_1 = sorted([(i, x) for i, x in enumerate(transform_msg)], key=itemgetter(1))
    print("list1", list_1)

    list_2 = [None for i in range(n)]
    for i, y in enumerate(list_1):
        j, _ = y
        list_2[j] = i
    print("list2", list_2)

    tx = [index_]
    for i in range(1, n):
        tx.append(list_2[tx[i - 1]])
    print('tx', tx)

    result = [transform_msg[i] for i in tx]
    print(result)
    result.reverse()
    return ''.join(result)


if __name__ == "__main__":
    print(bw_restore(24, 'styssesvmrgath  ceiis eee r'))
