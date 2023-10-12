# This program displays a table of Celcius and their Fahrenheit equivalents
# Inputs: N/A
# Outputs: Celsius and Fahrenheit
# Written by: C. Conner
# Modified by:  Jose Gonzalez
# Modified Date: Feb 19, 2020

#Format Set up
print("Clesius\tFahrenheit")
print("---------------------------")

#Loop set up in table format and some cool mathamatics to convert C into F 
for Celsius in range(-20,19,2):
    Cool_math = (9/5)* Celsius + 32
    Fahrenheit = (format(Cool_math,'.1f'))
    print(Celsius, "\t", Fahrenheit,)
 #Fin
print("---------------------------")
print("why do we still use Fahrenheit/the Imperial system??")