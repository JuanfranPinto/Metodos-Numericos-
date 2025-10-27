'''def f(x):
    return (1/4)*((x**3) + 3*(x**2) - 6*(x - 8))

def bisection(a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) >= 0:
        print("La función no cambia de signo en el intervalo dado.")
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2

# Definir los límites del intervalo
a = -5  # Límite inferior
b = 3   # Límite superior

# Llamar al método de bisección
raiz = bisection(a, b)
print(f"La raíz estimada es: {raiz}")'''

'''import math

def biseccion(func, a, b, tol):'''

#var = 0  # Asignando 0 a var
#print(var == 0)

#var = 1  # Asignando 1 a var
#p#rint(var == 0)


#3var = 0  # Asignando 0 a var
#print(var != 0)

#var = 1  # Asignando 1 a var
#print(var != 0)

#n = int(input())  # Toma la entrada del usuario y la convierte en un entero
#print(n >= 100)    # Imprime True si n es mayor o igual a 100, False si no
# Se leen dos números

# Se leen dos números
'''number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)'''


# Se leen tres números
'''number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)
'''

'''# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.

largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)'''


'''income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.

tax = round(tax, 0)
print("El impuesto es:", tax , "pesos")
'''

'''year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")'''
  
  # Solicitar al usuario que ingrese una palabra
#user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
#user_word = user_word.upper()

# Iterar sobre cada letra de la palabra
#for letter in user_word:
    # Si la letra es una vocal, se omite (se "devora")
 #   if letter in "AEIOU":
   #     continue  # Saltar la iteración actual y pasar a la siguiente
    # Si no es una vocal, se imprime la letra
  #  print(letter)


'''# Solicitar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Inicializar una cadena vacía para almacenar las letras sin vocales
word_without_vowels = ""

# Iterar sobre cada letra de la palabra
for letter in user_word:
    # Si la letra es una vocal, se omite (se "devora")
    if letter in "AEIOU":
        continue  # Saltar la iteración actual y pasar a la siguiente
    # Si no es una vocal, se concatena la letra a word_without_vowels
    word_without_vowels += letter

# Imprimir la palabra sin vocales
print(word_without_vowels)'''

'''# Solicitar al usuario que ingrese la cantidad de bloques
blocks = int(input("Ingresa la cantidad de bloques disponibles: "))

# Inicializar la altura de la pirámide y el número de bloques para la siguiente capa
height = 0
next_layer_blocks = 1  # La primera capa tiene 1 bloque

# Mientras haya suficientes bloques para construir la siguiente capa
while blocks >= next_layer_blocks:
    blocks -= next_layer_blocks  # Restar los bloques usados
    height += 1  # Aumentar la altura de la pirámide
    next_layer_blocks += 2  # La siguiente capa tiene 2 bloques más

# Imprimir la altura de la pirámide
print("La altura de la pirámide es:", height) '''
  


# Ejemplo 1:

#print(var > 0)
#print(not (var <= 0))


# Ejemplo 2:
#print(var != 0)
#print(not (var == 0))




'''numebers = [12, 25, 45, 75, 105, 125 ]
# esta es la lista original 

numebers[len (numebers)//2 ] = int (input ("ingresa el nuevo numero central  "))
print (numebers )

numebers.pop()
print (numebers ) 
print (len (numebers) )'''


'''numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(1, 69)
print(len(numbers))
print(numbers)

numbers.append(2048)
print(len(numbers))
print(numbers)'''

'''new_list = [3, 6, 9, 12, 15]

for i in range(10):
    new_list.append(i+1)
    
print(new_list) '''


'''my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)'''


'''my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for i in my_list:
    total += i

print(total)'''

'''my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Lista original
my_list = [1, 2, 3, 4, 5, 6]

# Calcular la longitud de la lista
length = len(my_list)

# Invertir los elementos manualmente
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# Mostrar la lista invertida
print(my_list)'''



def Tripletes():
    # Con N dado, debemos encontrar un triplete (A, B, C) donde sus componentes deben ser diferentes.
    # A + B + C = 2*N y A ^ B ^ C = N     
    n = int(input())
    # Si n es impar o cero no exite solución.
    if n % 2 != 0 or n == 0:
        print(-1)
        return
    # Podemos deducir C directamente como n/2, para solo encontrar A y B.
    c = n // 2
    # Con C conocido, podemos deducir A y B usando las fórmulas:
    suma_AB = n + c      
    xor_AB = n ^ c

    # Se verifica si es que A y B tienen solución si es que la diferencia de la suma y el xor es par.
    if (suma_AB - xor_AB) % 2 != 0:
        print(-1)
        return
    # Calculamos el AND de A y B para obtener A y B
    and_AB = (suma_AB - xor_AB) // 2
    
    # Si es que el AND y el XOR tienen bits en común no existe solucion.
    if (xor_AB & and_AB) != 0:
        print(-1)
        return

    # Despues de verificar las condiciones, calculamos A y B
    a = and_AB
    b = xor_AB + and_AB

    # Verificamos que A, B y C sean positivos y distintos entre sí.
    if a > 0 and b > 0 and c > 0 and a != b and b != c and a != c:
        triplete = sorted([a, b, c])
        print(*triplete)
    else:
        print(-1)

if __name__ == "_main_":
    T = int(input())
    for _ in range(T):
        Tripletes()




