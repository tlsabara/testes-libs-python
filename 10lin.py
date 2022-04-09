from random import randint
from tkinter import N

def numlines(code):
    if len(code) < 10:
        continue_witre = True
        return continue_witre
    else:
        continue_witre = False
        return continue_witre
    

def write_code(idea):
    if idea == 'good':
        line = '<Encoded Idea>'
        print(line)
        return line
    else:
        line = 'Bug Error'
        print(line)
    return None

line_codes = []

while(numlines(line_codes)):
    if (randint(0,9000000000)%2) == 0:
        think_idea = 'good'
    else:
        think_idea = 'bad'
        
    line_codes.append(write_code(think_idea))
    
