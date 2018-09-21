import os
import re
import random
spisok = []

file_list = os.listdir()
#print (file_list)

print ("Темы:")
for element in file_list:
    bez_rasch = os.path.splitext(element)
    if bez_rasch[1] == ".txt":
        print (bez_rasch[0])
        spisok.append(bez_rasch[0])

#print (spisok)
while True: 
    word = (input("Выберите одну из предложенных тем: "))

    if word not in spisok:
        print ("Проверьте правильность введённого")
    else:
        f = open(word + ".txt", "r", encoding = 'utf-8',)
        text = f.read().splitlines()
        #print (text)
        guess = random.choice(text)
        #print (guess)
        a = len(guess)
        n = 7
        att = print("У вас есть ", n ," попыток, чтобы угадать слово из ", a, " букв: ")
        
        #этот кусок прочерчивает подчеркивания и просит ввести букву
        ans = '_ ' * a
        print(ans)
        letter = input("Введите букву: ")

        end = False
        while not end:

            while not letter.isalpha():
                letter = input ("Введите букву: ")

            while not re.search ('^[А-Яа-я]+$', letter):
                letter = input ("Введите букву: ")
                       
            while letter not in guess: #этот кусок, когда вводят неправильные буквы
                n = n-1
                if n == 0:
                   print ("Вы проиграли, к сожалению.")
                   end = True
                   break
                print ("Попробуйте ещё! У вас осталось ", n, "попыток.")
                i = 0
                while i != a:
                    print('_', end = ' ')
                    i = i+1
                letter = input ("Введите букву: ")

            while letter in guess: #этот кусок, когда вводят правильные буквы
                index = guess.find(letter)
                while index != -1:
                    #print(index)
                    guess = guess[:index] + '|' + guess[(index + 1):] 
                    #print (guess)
                    ans = ans[:index*2] + letter + ans[(index*2 + 1):]
                    print (ans)
                    index = guess.find(letter)
                if '_' not in ans:
                    print ("Поздравляю! Вы выиграли!")
                    end = True
                else:
                    letter = input ("Введите букву: ")








            
        
        
        



