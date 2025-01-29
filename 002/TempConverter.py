"""
Caleb Thomas
01/29/25
Desciption: a program that converts a temperature in Celsius to Fahrenheit.

startCommand: py TempConverter.py


"""
## formuala = °F = °C × (9/5) + 32
C = 4 # Celsius

## Uses formuala to calculate the farinhates 
F = C * (9/5) + 32

#Print the output into a readable format
print("%d\u00b0C is %s\u00b0F" %(C,float(F)))

