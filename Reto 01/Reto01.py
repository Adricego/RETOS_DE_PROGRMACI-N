print("=== Operadores Aritméticos  ===")
a = 10
b = 3
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

print("\n=== Operadores de Comparación  ===")
print(f"Igualdad: {a} == {b} -> {a == b}")
print(f"Diferencia: {a} != {b} -> {a != b}")
print(f"Mayor que: {a} > {b} -> {a > b}")
print(f"Menor que: {a} < {b} -> {a < b}")
print(f"Mayor o igual que: {a} >= {b} -> {a >= b}")
print(f"Menor o igual que: {a} <= {b} -> {a <= b}")

print("\n=== Operadores Lógicos  ===")
x = True
y = False
print(f"AND: {x} and {y} -> {x and y}")
print(f"OR: {x} or {y} -> {x or y}")
print(f"NOT: not {x} -> {not x}")

print("\n=== Operadores de Asignación  ===")
c = 5
print(f"Valor inicial: c = {c}")
c += 2
print(f"Suma y asignación: c += 2 -> c = {c}")
c *= 3
print(f"Multiplicación y asignación: c *= 3 -> c = {c}")


print("\n=== Operadores de Identidad  ===")
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print(f"lista1 es lista2: {lista1 is lista2} -> {lista1 is lista2}")
print(f"lista1 es lista3: {lista1 is lista3} -> {lista1 is lista3}")
print(f"lista1 no es lista3: {lista1 is not lista3} -> {lista1 is not lista3}")


print("\n=== Operadores de Pertenencia  ===")
frutas = ["manzana", "banana", "cereza"]
print(f"'banana' en frutas: {'banana' in frutas} -> {'banana' in frutas}")
print(f"'uva' no en frutas: {'uva' not in frutas} -> {'uva not in frutas'}")


print("\n=== Operadores a Nivel de Bits  ===")
m = 5  # En binario: 0101
n = 3  # En binario: 0011

print(f"AND a nivel de bits: {m} & {n} = {m & n} (binario: {bin(m)} & {bin(n)} = {bin(m & n)})")
print(f"OR a nivel de bits: {m} | {n} = {m | n} (binario: {bin(m)} | {bin(n)} = {bin(m | n)})")
print(f"XOR a nivel de bits: {m} ^ {n} = {m ^ n} (binario: {bin(m)} ^ {bin(n)} = {bin(m ^ n)})")
print(f"Desplazamiento a la izquierda: {m} << 1 = {m << 1} (binario: {bin(m)} << 1 = {bin(m << 1)})")
print(f"Desplazamiento a la derecha: {m} >> 1 = {m >> 1} (binario: {bin(m)} >> 1 = {bin(m >> 1)})")
print(f"Negación a nivel de bits: ~{m} = {~m} (binario: ~{bin(m)} = {bin(~m)})")

# --- IGNORE ---