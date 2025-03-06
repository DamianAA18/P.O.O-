"""
            Ingenieria en Sistemas Computacionales
                Aguileta Argueta Mario Damián 
                        24590347
            Programación Orientada a Objetos
        PROGRAMA TERMINADO Y CORREGIDO EL 5 DE MARZO DE 2025
"""

import random

class Convivio():
    def __init__(self):
        self.tInvitados = 0
        self.hom = 0
        self.muj = 0
        self.costoArra = 160
        self.costoBis = 190
        self.costoCho = 25
        self.costoPoll = 50
        self.costoSalch = 30
        self.totalCarne = 0
        self.carneTotalPrecio = 0
        self.cantCarbon = 0
        self.precioCarbon = 20
        self.totalRefrescos = 0
        self.costRefrescos = 25
        self.comple = 25
        self.costComple = 0
        self.n = 0

    def invitados(self):
        self.hom = int(input("Ingrese la cantidad de Hombres: "))
        self.muj = int(input("Ingrese la cantidad de Mujeres: "))
        self.tInvitados = self.hom + self.muj

    def carne(self):
        self.totalCarne = (self.hom * 0.8) + (self.muj * 0.5)
        self.costoArra = self.costoArra * (self.totalCarne * 0.30)
        self.costoBis = self.costoBis * (self.totalCarne * 0.30)
        self.costoCho = self.costoCho * (self.totalCarne * 0.15)
        self.costoPoll = self.costoPoll * (self.totalCarne * 0.15)
        self.costoSalch = self.costoSalch * (self.totalCarne * 0.10)
        self.carneTotalPrecio = self.costoArra + self.costoBis + self.costoCho + self.costoPoll + self.costoSalch

    def carbon(self):
        self.cantCarbon = self.totalCarne / 3
        self.precioCarbon = self.precioCarbon * self.cantCarbon

    def refrescos(self):
        self.totalRefrescos = 0.500 * self.tInvitados #calculo en litros.
        self.costRefrescos = self.costRefrescos * self.totalRefrescos

    def complementos(self):
        self.n = random.randint(1, self.tInvitados)
        self.costComple = self.n * self.comple

    def compras(self):
        self.invitados()
        self.carne()
        self.carbon()
        self.refrescos()
        self.complementos()
        print(f"""Las personas invitadas son {self.tInvitados}
                y son {self.hom} hombres y {self.muj} mujeres.""")
        print(f"""Los costos de los productos son: 
                Carne:{self.carneTotalPrecio}
                Carbon:{self.precioCarbon}
                Refrescos:{self.costRefrescos}
                Complementos:{self.costComple} y las personas que ponen complementos son: {self.n}""")

    def cooperacion(self):
        self.cooperacion = self.carneTotalPrecio + self.precioCarbon + self.costRefrescos + self.costComple
        print(f"La cooperacion seria de: {self.cooperacion / self.tInvitados}")

carneAsada = Convivio()
carneAsada.compras()
carneAsada.cooperacion()


