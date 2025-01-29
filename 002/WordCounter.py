"""
Caleb Thomas
01/29/25
Desciption: a program that takes in a sentance and returns the number of words in the sentance.

startCommand: py WordCounter.py


"""

def Init():

    sentance = input("Input sentance: ")
    
    
    print("The number of words in your sentance is: ", sentance.count(' '))
    anwser = input("Would you like to try a different sentance? (Y/N): ")
    if anwser.lower() == "y":
        Init()

    elif anwser.lower() == "n":

        print("Closing program.....")



Init()