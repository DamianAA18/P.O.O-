"""
            Ingenieria en Sistemas Computacionales
                Aguileta Argueta Mario Damián 
                        24590347
            Programación Orientada a Objetos

                    PROGRAMA HECHO EN CLASE 
        REVISADO Y CORREGIDO ENTRE EL 4 Y 5 DE MARZO DE 2025
"""
#Iniciamos con los conceptos de POO del paso de parametros, y de simplificación del codigo
class Figuras:
    def _init_(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def operaciones(self):
        print("""Seleccione una figura para calcular su área:")
        1. Círculo
        2. Trapecio
        3. Rectangulo""")

        r = int(input("Ingresa una opciòn"))
        return (r)

    def circulo (self, r):
        areaCirculo = 3.1416 * r**2
        return (areaCirculo)
        
    def trapecio (self, b1, b2, h):
        areaTrapecio = (b1+b2 * h) / 2 
        return (areaTrapecio)
    def rectangulo (self, b, h):
        areaRectangulo = b * h
        return (areaRectangulo)


obj = Figuras ()
s = obj.operaciones()

if s == 1:
    obj.a = float(input("Dame el valor del radio"))
    resultado = obj.circulo(obj.a)
    print (f"El area del circulo es {resultado}")

elif s == 2:
    obj.a = float(input("Dame el valor de la base menor"))
    obj.b = float(input("Dame el valor de la base mayor"))
    obj.c = float(input("Dame el valor de la h"))
    resultado = obj.trapecio(obj.a, obj.c, obj.b)
    print(f"El area del trapecio es: {resultado} ")


elif s == 3:
    obj.a = float(input("Dame el valor de la altura"))
    obj.b  = float(input("Dame el valor de la base"))
    resultado = obj.rectangulo(obj.a, obj.b)
    print(f"El area del rectangulo es {resultado}")