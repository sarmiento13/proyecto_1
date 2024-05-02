# controles de flujo
Los controles de flujo en Python **son estructuras que nos permiten tomar decisiones en función de ciertas condiciones.** Estas estructuras nos permiten controlar cómo se ejecuta nuestro código y qué acciones se toman en diferentes situaciones. Aquí tienes un resumen sobre los controles de flujo en Python decisiones, junto con algunos ejemplos:
 
## 1. Estructura "if":
 
- La estructura **"if"** nos permite ejecutar un bloque de código solo si una condición es verdadera.
- Ejemplo:
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
 ```
## 2. Estructura "if-else":
 
- La estructura **"if-else"** nos permite ejecutar un bloque de código si una condición es verdadera, y otro bloque de código si la condición es falsa.
- Ejemplo:
```python
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
 ```
## 3. Estructura "if-elif-else":
- La estructura **"if-elif-else"** nos permite evaluar múltiples condiciones y ejecutar diferentes bloques de código dependiendo de la primera condición que sea verdadera.
- Ejemplo:
```python
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Bueno")
elif nota >= 70:
    print("Regular")
else:
    print("Reprobado")
 ```
