from os import system as s, name as n
from time import sleep


def util(n):
    print(n)
    sleep(0.5)
    s('cls' if n == 'nt' else 'clear')
 

button = True
def rec(number) -> str:
    if number == 0:
        util(number)
        rec(number + 1)
        button = False
        if number == start:
            print("end")
    elif button:
        util(number)
        rec(number - 1)
        
 
start = rec(5)