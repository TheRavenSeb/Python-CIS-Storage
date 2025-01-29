## DogYearCalculator.py 
"""
Caleb Thomas
01/29/25
Desciption: a program that takes users age and outputs it in dog years

startCommand: py DogYearCalculator.py


"""


def calculate_Age(age):
    """
    Calculates age in dog years 
    @param(Number): age
    @returns: Number

    """
    
    return age*7


def Init():

    age = input("Input your age: ")
    age = calculate_Age(int(age))
    print("Your age in dog years is: ", age)
    anwser = input("Would you like to calculate a different age? (Y/N): ")
    if anwser.lower() == "y":
        Init()

    elif anwser.lower() == "n":

        print("Closing program.....")



Init()
