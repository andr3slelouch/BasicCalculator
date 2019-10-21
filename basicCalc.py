# Programa que realiza operaciones matematicas básicas.
# Esta función suma dos numeros
def add(x, y):
   return x + y
# Esta funcion resta dos numeros
def subtract(x, y):
   return x - y
# Esta funcion multiplica dos numeros
def multiply(x, y):
   return x * y
# Esta funcion divide dos numeros
def divide(x, y):
   return x / y
# Esta función eleva a un exponente
def elevate(x,y):
   return x**y
# Esta funcion realiza la raiz de un numero
def esquareroot(x):
   return math.sqrt(x)
print("Seleccion operacion")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Exponente")
print("6.Raiz Cuadrada")
# Tomar entrada
choice = input("Ingrese selección(1/2/3/4):")
num1 = int(input("Ingrese el primer número: "))
if choice != '6':
   num2 = int(input("Ingrese el segundo número: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
   #print("Proximamente")
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
   #print("Proximamente")
elif choice == '5':
   print(num1,"^",num2,"=", elevate(num1,num2))
elif choice == '6':
   print("√",num1,"=", esquareroot(num1))
else:
   print("Entrada no reconocida")
