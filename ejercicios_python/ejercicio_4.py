#!/usr/bin/env python3

def CelciusAFahrenheit(temp):
    
    fahrenheit = (temp * 9/5) + 32
    print("Temperatura en grados fahrenheit: ", fahrenheit)

def FahrenheitACelcius(temp):
    
    celcius = (temp - 32) * 5/9
    print("Temperatura en grados celcius: ", celcius)

print("Ingrese temperatura")
temperatura = input()
print("Ingrese Escala: Celcius o fahrenheit: ")
escala = input()
if (escala[0] == 'c' or escala[0] == 'C'):
    CelciusAFahrenheit(float(temperatura))

elif (escala[0] == 'f' or escala[0] == 'F'):
    FahrenheitACelcius(float(temperatura))

