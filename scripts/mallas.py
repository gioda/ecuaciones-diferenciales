"""Ayuda opcional para las mallas de los ejercicios M2-E0049 y M2-E0068.

Python 3, sin paquetes adicionales. Las etapas actualizan el vector completo.
La salida es una tabla CSV que puede representarse en una hoja de cálculo.
Uso: python3 mallas.py E0049
     python3 mallas.py E0068
"""
import argparse
import csv
import sys


def sumar(y, k, factor):
    return tuple(yi + factor * ki for yi, ki in zip(y, k))


def euler(f, t, y, h):
    return sumar(y, f(t, y), h)


def rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h / 2, sumar(y, k1, h / 2))
    k3 = f(t + h / 2, sumar(y, k2, h / 2))
    k4 = f(t + h, sumar(y, k3, h))
    return tuple(yi + h * (a + 2 * b + 2 * c + d) / 6
                 for yi, a, b, c, d in zip(y, k1, k2, k3, k4))


def integrar(f, y0, t_final, h, paso):
    n = round(t_final / h)
    if abs(n * h - t_final) > 1e-12:
        raise ValueError('El paso debe dividir el intervalo.')
    y = tuple(y0)
    filas = [(0.0, y)]
    for i in range(n):
        y = paso(f, i * h, y, h)
        filas.append(((i + 1) * h, y))
    return filas


def campo_poblaciones(t, y):
    x1, x2 = y
    return (2 * x1 - 2 * x1 * x2, x1 * x2 - x2)


def campo_tercer_orden(t, y):
    posicion, velocidad, derivada_segunda = y
    return (velocidad, derivada_segunda,
            velocidad ** 2 - 1 - posicion * derivada_segunda)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ejercicio', choices=['E0049', 'E0068'])
    args = parser.parse_args()
    salida = csv.writer(sys.stdout)
    if args.ejercicio == 'E0049':
        salida.writerow(['t', 'x1', 'x2'])
        for t, y in integrar(campo_poblaciones, (1, 3), 1, 0.025, rk4):
            salida.writerow([f'{t:.3f}', *(f'{z:.11f}' for z in y)])
    else:
        salida.writerow(['h', 't', 'y', 'y_prima', 'y_segunda'])
        for h in (0.1, 0.05, 0.025):
            for t, y in integrar(campo_tercer_orden, (0, 0, 1.32824), 2, h, euler):
                salida.writerow([h, f'{t:.3f}', *(f'{z:.11f}' for z in y)])


if __name__ == '__main__':
    main()
