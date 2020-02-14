

def morral(knapsack_size, weights, values, n):
    if n == 0 or knapsack_size == 0:
        return 0

    # Si el elemento que quiero incluir en el morral,
    #  pesa más que el tamaño que le queda al morral
    if weights[n - 1] > knapsack_size:
        print(f'El peso actual es de {weights[n -1]}')
        return morral(knapsack_size, weights, values, n - 1)

    max_value = max(values[n - 1] + morral(knapsack_size - weights[n - 1], weights, values, n - 1),
                    morral(knapsack_size, weights, values, n - 1))

    print(
        f'La mochila pesa: {knapsack_size} el valor maximo es de: {max_value}')
    return max_value


if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    knapsack_size = 90
    n = len(values)

    result = morral(knapsack_size, weights, values, n)
    print(result)
