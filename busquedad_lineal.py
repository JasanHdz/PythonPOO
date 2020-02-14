import random
contador = 0


def busquedad_lineal(lista, objetivo):
    global contador
    match = False
    for element in lista:
        contador += 1
        if element == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    size_list = int(input('De que tamano sera la lista?: '))
    objetivo = int(input('¿Qué número quieres encontrar? '))
    lista = [random.randint(0, 100) for i in range(size_list)]

    encontrado = busquedad_lineal(lista, objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta "} en la lista')
    print(f'La búsquedad hizo {contador} pasos')
