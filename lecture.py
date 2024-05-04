# 1. *Ejercicio de bucles y listas:* Crea un programa que 
#recorra una lista de números y determine cuántos de ellos 
#son pares y cuántos son impares. 

#python
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = contar_pares_impares(numeros)
print("Cantidad de números pares:", resultado[0])
print("Cantidad de números impares:", resultado[1])


#2. *Problema de condicionales y funciones:* Escribe una 
#función que reciba un número como argumento y devuelva True
#si es primo y False si no lo es.

#python
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = 17
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")


#3. *Ejercicio de control de flujo anidado:* Desarrolla un 
#programa que pida al usuario dos números y luego determine 
#si su suma es mayor que 10, menor que 10 o igual a 10.

#python
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

suma = numero1 + numero2

if suma > 10:
    print("La suma es mayor que 10")
elif suma < 10:
    print("La suma es menor que 10")
else:
    print("La suma es igual a 10")


#4. *Problema de bucles y strings:* Crea un programa que tome
# una cadena de texto y cuente la cantidad de vocales que contiene 
#(tanto mayúsculas como minúsculas).
#python
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

texto = "Hola Mundo"
cantidad_vocales = contar_vocales(texto)
print("Cantidad de vocales:", cantidad_vocales)

