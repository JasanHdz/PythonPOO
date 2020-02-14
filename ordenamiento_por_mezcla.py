import random


def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        half = len(lista) // 2
        left = lista[:half]
        right = lista[half:]

        print(left, '*' * 5, right)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(left)
        ordenamiento_por_mezcla(right)

        # Iteradores para recorrer las 2 sublistas
        i = 0
        j = 0
        # Iterador para lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

        print(f'Izquierda {left}, Derecha {right}')
        print(lista)
        print('-' * 50)
    return lista


if __name__ == '__main__':
    size_list = int(input('De que tamano sera la lista?: '))
    lista = [random.randint(0, 100) for i in range(size_list)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
