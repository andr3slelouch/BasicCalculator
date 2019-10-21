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
# sta funcion divide dos numeros
def divide(x, y):
   return x / y
print("Seleccion operacion")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.Exponente")
# Tomar entrada
choice = input("Ingrese selección(1/2/3/4):")
num1 = int(input("Ingrese el primer número: "))
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
else:
   print("Entrada no reconocida")
