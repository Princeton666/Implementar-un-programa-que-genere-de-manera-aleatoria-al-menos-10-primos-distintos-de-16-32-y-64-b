import math
import random

aleatorio = random.SystemRandom() #esto es para generar números aleatorios

def prueba(n, a): #función con los valores "n" y "a" siguiendo la fórmula -> "a" elevado a "(n-1)" es congruente con "1 módulo n"
    exp = n - 1 #es la potencia
    while not exp & 1: #mientras el exponente sea par
        exp >>= 1 #manipulamos bits rápida, esto es lo mismo que exp //= 2 
    if pow(a, exp, n) == 1: #aquí verificamos el módulo con ayuda de la librería math si es igual a 1 para que retorne verdadero
        return True
    while exp < n - 1: 
        if pow(a, exp, n) == n - 1: #algoritmo para verificar que uno sea divisible 
            return True
        exp <<= 1 #desplazamos bit
    return False

def Miller_Rabin(n, k = 40): #ponemos 40 como ejemplo ya que es la cantidad de valores de n
    for i in range(k): #recorremos hasta "k" valores
        a = aleatorio.randrange(2, n - 1) #a = a un número aleatorio con el rango
        if not prueba(n, a): #hacemos la verificación
            return False
    return True

def gen_prime(bits):
    while True:
        #todo esto garantiza que "a" es impar moviendo bits
        a = (aleatorio.randrange(1 << bits - 1, 1 << bits) >> 1) + 1
        if Miller_Rabin(a): #hacemos test de primalidad
            return a #devolvemos el número aleatorio 

print("Generar numeros primos aleatorios de 16, 32 y 64 bits")
print("Elija si quiere || 1.- 16 bits || 2.- 32 bits || 3.- 64")
eleccion = int(input("Elija: "))
if eleccion == 1:
    print("10 Primos aleatorios de 16 bits")
    for i in range(0, 10):
        print(gen_prime(16))
if eleccion == 2:
    print("10 Primos aleatorios de 32 bits")
    for i in range(0, 10):
        print(gen_prime(32))
if eleccion == 3:
    print("10 Primos aleatorios de 64 bits")
    for i in range(0, 10):
        print(gen_prime(64))


