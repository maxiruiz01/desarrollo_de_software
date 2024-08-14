#!/usr/bin/env python3



def Suma():
    print ("Operacion suma, ingrese un numero")
    num1 = input()
    num1 = float(num1)
    print ("Ingrese otro numero")
    num2 =  input()
    num2 = float(num2)
    
    
    print("Resultado: ",num1 + num2)
    
def Resta():
    print ("Operacion Resta, ingrese un numero")
    num1 = input()
    num1 = float(num1)
    print ("Ingrese otro numero")
    num2 =  input()
    num2 = float(num2)
    
    print("Resultado: ",num1 - num2)
    
def Division():
    print ("Operacion Division, ingrese un numero")
    num1 = input()
    num1 = float(num1)
    print ("Ingrese otro numero")
    num2 =  input()
    num2 = float(num2)
    print("Resultado: ",num1/num2)
    
def Multiplicacion():
    print ("Operacion Multiplicacion, ingrese un numero")
    num1 = input()
    num1 = float(num1)
    print ("Ingrese otro numero")
    num2 =  input()
    num2 = float(num2)
    
    
    print("Resultado: ", num1*num2)

Suma()
Resta()
Multiplicacion()
Division()


