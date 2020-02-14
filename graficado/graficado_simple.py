from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file('gráficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres gráficar? '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Ingresa el valor Y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
