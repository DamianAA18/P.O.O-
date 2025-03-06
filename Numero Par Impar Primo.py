"""
            Ingenieria en Sistemas Computacionales
                Aguileta Argueta Mario Damián 
                        24590347
            Programación Orientada a Objetos

                    PROGRAMA DE LA CLASE DEL 14 DE FEBRERO DE 2025
            REALIZADO EL 17 DE FEBRERO DEL 2025 Y TERMINADO EL 5 DE MARZO
"""

class NumParPrimoImpar():
    def __init__(self):
        self.num=0
    def pedirNums(self):
        self.num=int(input("Ingrese el numero: "))
    def numeroPar (self):
        return self.num%2==0
    def numeroPrimo(self):
            for i in range(2, int(self.num**0.5) + 1):
                if self.num % i == 0:
                    print(f"El numero {self.num} no es primo")
                    return
            print(f"El numero {self.num} es primo")
    def imprimirRes(self):
        if self.numeroPar():
            print("Y es par")
        else:
            print("Y es impar")

par=NumParPrimoImpar()
par.pedirNums()
par.numeroPrimo()
par.numeroPar()
par.imprimirRes()