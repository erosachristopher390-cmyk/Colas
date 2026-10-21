
from collections import deque


class Cola:
    def __init__(self):
        self.elementos = deque()

    def insertar(self, elemento):
        self.elementos.append(elemento)

    def quitar(self):
        if self.esta_vacia():
            return None
        return self.elementos.popleft()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        return list(self.elementos)

    def __len__(self):
        return len(self.elementos)


def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()

    if len(cola_a) != len(cola_b):
        raise ValueError("Las dos colas deben tener la misma cantidad de elementos.")

    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        numero_a = cola_a.quitar()
        numero_b = cola_b.quitar()
        cola_resultado.insertar(numero_a + numero_b)

    return cola_resultado


def main():
    cola_a = Cola()
    cola_b = Cola()

    datos_a = [3, 4, 2, 8, 12]
    datos_b = [6, 2, 9, 11, 3]

    for numero in datos_a:
        cola_a.insertar(numero)

    for numero in datos_b:
        cola_b.insertar(numero)

    print("SUMA DE DOS COLAS")
    print("-" * 40)
    print(f"Cola A:       {cola_a.mostrar()}")
    print(f"Cola B:       {cola_b.mostrar()}")

    cola_resultado = sumar_colas(cola_a, cola_b)

    print(f"Cola resultado: {cola_resultado.mostrar()}")


if __name__ == "__main__":
    main()
