import random
import sys
from random import choice
from string import ascii_uppercase
from tkinter import *
import time

def runFunction():
    print ("Добро пожаловать в генератор паролей!")
    time.sleep(5)

    userMethod = int(input ("Выберите метод: Генератор пароля в Tkinter(4), генератор одного пароля(3), структурированный (2), не структурированный(1): "))

    


    if userMethod == 1:
        firstNumber = int(input ("Введите первый символ для генератора пароля: "))
        secondNumber = int(input ("Введите второй символ для генератора пароля: "))
        def perebor():
            
            aa = random.randint(firstNumber,secondNumber) # from N symbols to N symbols

            symbols = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            passs = (''.join(choice(symbols) for i in range(aa)))

            print(passs)
            
        for i in range(1000):
            perebor()
        
    if userMethod == 2:
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        number = input('Количество паролей?'+ "\n")
        length = input('Длина пароля?'+ "\n")
        number = int(number)
        length = int(length)
        for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
            print(password)

    elif userMethod == 3:
        num = input('login ')
        pas = ''
        passSymbols = int(input ("Выберите количество символов в пароле: "))
        for x in range(passSymbols): #Количество символов (16)
            pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
        print('Hello, ', num, 'your password is: ', pas)




    if userMethod == 4:
        symbols=['!','@','#','$','%','^','&','*','(',')','~','`']
        numbers=[1,2,3,4,5,6,7,8,9,0]
        words=['a','b','c','d','e''f','g','h','i','j','k','l','m','n','o','p']


        def generate():

            print(str(random.choice(numbers))+
                    random.choice(words)+
                    random.choice(symbols)+
                    str(random.choice(numbers))+
                    random.choice(words)+
                    random.choice(words)+
                    str(random.choice(numbers))+
                    random.choice(symbols)+
                    random.choice(words))

            screen = Tk()
            screen.title("Graphical Password generator")
            screen.geometry('400x400')

            welcome_text=Label(screen, text = "Welcome to my graphical password generator" ,fg='red', bg='yellow')
            welcome_text.pack()

            generate=Button(screen, text='Generate', fg='red', bg='yellow', command=generate)
            generate.place(x=200, y=40)

            name_storage=StringVar()
            name=Entry(screen, textvariable=name_storage)
            name.pack()
            screen.mainloop()

runFunction()  

isUser = str(input('Вы хотите продолжить? '))

if isUser == "yes" or isUser == "y" or isUser == "1" or isUser == "да" or isUser == "Да" or isUser == "Y" or isUser == "Yes":
    runFunction()
else:
    input("Press ENTER to exit programm")