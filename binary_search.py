import random
contador = 0


def search_binary(lista, start, end, objective):
    global contador
    contador += 1
    print(f'Buscando el {objective} entre {lista[start]} y {lista[end - 1]}')
    if start > end:
        return False

    half = (start + end) // 2

    if lista[half] == objective:
        return True
    elif lista[half] < objective:
        return search_binary(lista, half + 1, end, objective)
    elif lista[half] > objective:
        return search_binary(lista, start, half - 1, objective)


if __name__ == '__main__':
    size_list = int(input('De que tamano sera la lista?: '))
    objetivo = int(input('¿Qué número quieres encontrar? '))
    lista = sorted([random.randint(0, 100) for i in range(size_list)])

    encontrado = search_binary(lista, 0, len(lista), objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta "} en la lista')
    print(f'El busquedad hizo {contador} pasos')
