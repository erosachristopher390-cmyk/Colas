
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


class SistemaSeguros:
    def __init__(self):
        self.colas = {
            1: Cola(),
            2: Cola(),
            3: Cola()
        }

        self.contadores = {
            1: 0,
            2: 0,
            3: 0
        }

    def registrar_cliente(self, servicio):
        if servicio not in self.colas:
            print("Servicio no válido.")
            return

        self.contadores[servicio] += 1
        turno = self.contadores[servicio]

        self.colas[servicio].insertar(turno)

        print(
            f"Cliente registrado en el servicio {servicio}. "
            f"Su número de atención es {turno}."
        )

    def atender_cliente(self, servicio):
        if servicio not in self.colas:
            print("Servicio no válido.")
            return

        if self.colas[servicio].esta_vacia():
            print(f"No hay clientes en la cola del servicio {servicio}.")
            return

        turno = self.colas[servicio].quitar()

        print(
            f"Llamando al cliente número {turno} "
            f"del servicio {servicio}."
        )

    def mostrar_colas(self):
        print("\nESTADO ACTUAL DE LAS COLAS")
        print("-" * 35)

        for servicio, cola in self.colas.items():
            print(f"Servicio {servicio}: {cola.mostrar()}")

    def ejecutar(self):
        while True:
            print("\nSISTEMA DE ATENCIÓN DE SEGUROS")
            print("C + número: registrar cliente")
            print("A + número: atender cliente")
            print("M: mostrar todas las colas")
            print("S: salir")

            comando = input("Ingrese una opción: ").strip().upper()

            if comando == "S":
                print("Sistema finalizado.")
                break

            elif comando == "M":
                self.mostrar_colas()

            elif len(comando) >= 2 and comando[0] in ("C", "A"):
                try:
                    servicio = int(comando[1:])

                    if comando[0] == "C":
                        self.registrar_cliente(servicio)
                    else:
                        self.atender_cliente(servicio)

                except ValueError:
                    print("Debe ingresar una opción válida, por ejemplo C1 o A2.")

            else:
                print("Opción incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    sistema = SistemaSeguros()
    sistema.ejecutar()
