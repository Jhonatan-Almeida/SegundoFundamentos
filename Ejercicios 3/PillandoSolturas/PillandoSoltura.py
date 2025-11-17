#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def duplicados_a_unicos(lst):
    """1. Devuelve lista solo con elementos únicos."""
    vistos, dup = set(), set()
    for x in lst:
        (dup if x in vistos else vistos).add(x)
    return [x for x in lst if x not in dup]

def unir_y_ordenar(a, b):
    """2. Une dos listas y las ordena."""
    return sorted(a + b)

def segundo_mas_grande(lst):
    """3. Segundo número más alto sin usar sorted()[-2]."""
    unicos = list(set(lst))
    unicos.remove(max(unicos))
    return max(unicos)

def mayores_que(lst, umbral):
    """4. Cuantos elementos superan el umbral."""
    return sum(1 for x in lst if x > umbral)

def suma_divisibles_por(lst, n):
    """5. Suma los divisibles por n."""
    return sum(x for x in lst if x % n == 0)

def mayor_inferior(lst, limite):
    """6. Mayor número < limite."""
    candidatos = [x for x in lst if x < limite]
    return max(candidatos) if candidatos else None

def comunes(a, b):
    """7. Elementos comunes sin repetir."""
    return list(set(a) & set(b))

def apariciones(lst, elem):
    """8. Veces que aparece elem."""
    return lst.count(elem)

def solo_positivos(lst):
    """9. Solo números positivos."""
    return [x for x in lst if x > 0]

def longitudes(strings):
    """10. Lista con longitudes."""
    return [len(s) for s in strings]

def a_mayusculas(strings):
    """11. Lista en mayúsculas."""
    return [s.upper() for s in strings]

# --- menú rápido para probar ---
if __name__ == "__main__":
    ops = {
        1: ("duplicados→únicos", lambda: duplicados_a_unicos([1, 2, 2, 3, 4, 4, 5])),
        2: ("unir y ordenar", lambda: unir_y_ordenar([3, 1], [4, 2])),
        3: ("segundo mayor", lambda: segundo_mas_grande([10, 5, 8, 20])),
        4: ("mayores que umbral", lambda: mayores_que([1, 5, 9, 12], 6)),
        5: ("suma divisibles por", lambda: suma_divisibles_por(range(1, 21), 3)),
        6: ("mayor < límite", lambda: mayor_inferior([3, 7, 12, 5], 10)),
        7: ("elementos comunes", lambda: comunes([1, 2, 3], [2, 3, 4])),
        8: ("apariciones", lambda: apariciones([23, 65, 23], 23)),
        9: ("solo positivos", lambda: solo_positivos([-4, 3, 0, 7, -1])),
        10: ("longitudes strings", lambda: longitudes(["sol", "luna"])),
        11: ("strings mayúsculas", lambda: a_mayusculas(["hola", "mundo"])),
    }
    while True:
        print("\n" + "=" * 30)
        for k, (desc, _) in ops.items():
            print(f"{k} – {desc}")
        print("0 – Salir")
        try:
            op = int(input(">> "))
            if op == 0:
                break
            print("Resultado:", ops[op][1]())
        except (ValueError, KeyError):
            print("Opción inválida.")