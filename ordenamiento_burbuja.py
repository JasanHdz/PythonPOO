import random


def ordenamiento_de_borbuja(lista):
    n = len(lista)  # 10

    for i in range(n):
        for j in range(0, n - i - 1):  # 0 , 10 - 1 - 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':
    size_list = int(input('De que tamano sera la lista?: '))
    lista = [random.randint(0, 100) for i in range(size_list)]
    print(lista)

    lista_ordenada = ordenamiento_de_borbuja(lista)
    print(lista_ordenada)
