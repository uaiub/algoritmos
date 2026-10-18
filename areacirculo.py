# area_circulo.py - Algoritmo para calcular el área de un círculo
import math

radio = float(input("Ingrese el radio del círculo: "))

# Fórmula del área: A = π * r²
area = math.pi * (radio ** 2)

print(f"El área del círculo con radio {radio} es: {area:.2f}")