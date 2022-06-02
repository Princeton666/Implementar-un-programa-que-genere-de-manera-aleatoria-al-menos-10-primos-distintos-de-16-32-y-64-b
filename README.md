# Implementar-un-programa-que-genere-de-manera-aleatoria-al-menos-10-primos-distintos-de-16-32-y-64-b

Álgebra Abstracta - CCOMP3-2 // Permanente 02a

Integrantes:

Fabricio Arian Messa Mandujano

Royer Diosdado Carcausto Choquehuanca

2.- Implementar un programa que genere de manera aleatoria al menos 10 primos distintos de 16, 32 y 64 bits.

Utilizamos aleatorio = random.SystemRandom() para generar números aleatorios

creamos una funcion "def prueba(n, a):" con los valores "n" y "a" siguiendo la fórmula -> "a" elevado a "(n-1)" es congruente con "1 módulo n"

creamos un "while not exp & 1:" mientras el exponente sea par, luego con "exp >>= 1" manipulamos bits rápida (exp //= 2)
para verificar el módulo usamos la ayuda de la libreria math, donde si es igual a 1 nos retorne True

Creamos un algoritmo para verificar que uno sea divisible "if pow(a, exp, n) == n - 1:", luego desplazamos el bit con "exp <<= "

ponemos 40 como ejemplo ya que es la cantidad de valores de n "def Miller_Rabin(n, k = 40):", seguido recorremos hasta "k" valores "for i in range(k):"

creamos un numero aleatorio a con el rango  (2, n - 1), luego verificamos con "if not prueba(n, a):"


creamos def gen_prime(bits):
    while True:
        #todo esto garantiza que "a" es impar moviendo bits
        a = (aleatorio.randrange(1 << bits - 1, 1 << bits) >> 1) + 1
        if Miller_Rabin(a): #hacemos test de primalidad
            return a #devolvemos el número aleatorio 
