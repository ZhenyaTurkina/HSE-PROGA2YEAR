import random
import re

spisok = ["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter = random.choice(spisok)

while True:
    word = (input('enter an english letter: '))
    if word not in spisok:
            print ("не то")
    elif word == letter:
            print("класс")
            break
    elif word > letter:
            print ("чуть раньше")
            continue
    elif word < letter:
            print ("чуть позже")
            continue
    
