# Gustav's Client
import socket
import re
import math
from math import sqrt
import sys
from tkinter import *


# Define constants
FORMAT = 'utf-8'
PORT = 8080
SERVER = "127.0.01"
HEADER = 64
ADDRESS = (SERVER, PORT)

gClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

DISCONNECT = "!DISCONNECT!"

TK_SILENCE_DEPRECATION=1

try:
    gClient.connect(ADDRESS)
    print("Server found...")
except:
    print("Server not found...")

while True:
    
    # Open GUI for user interaction 

    def buttonClick(number):
        global operator
        operator = operator + str(number)
        input_value.set(operator)

    def buttonClear():
        global operator
        operator = ""
        input_value.set("")

    def buttonEqual():
        global operator
        input = str(operator)
        gClient.send(input.encode())
        result = gClient.recv(1024)
        input_value.set(result)
        operator = ""



    main = Tk()
    main.title("Calculator")

    operator = ""
    input_value = StringVar()

    display_text = Entry(main, font=("arial",20,"bold"),
                    textvariable=input_value, bd=8,
                    insertwidth=4, bg="wheat2", justify=RIGHT)
    display_text.grid(columnspan=4)

    # Row 1: C, √, Expo, /
    btn_C = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="C",
                command=buttonClear)
    btn_C.grid(row=1, column=0)

    btn_sqrt = Button(main, padx=31, bd=8, fg="black", 
                font=("arial",16,"bold"), text="√", 
                command=lambda: buttonClick("sqrt("))
    btn_sqrt.grid(row=1, column=1)

    btn_expo = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="expo",
                command=lambda: buttonClick("**"))
    btn_expo.grid(row=1, column=2)

    btn_div = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="/",
                command=lambda: buttonClick("/"))
    btn_div.grid(row=1, column=3)

    # Row 2: 7, 8, 9, *
    btn_7 = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="7",
                command=lambda: buttonClick(7))
    btn_7.grid(row=2, column=0)

    btn_8 = Button(main, padx=29, bd=8, fg="black", 
                font=("arial",20,"bold"), text="8", 
                command=lambda: buttonClick(8))
    btn_8.grid(row=2, column=1)

    btn_9 = Button(main, padx=33, bd=8, fg="black", 
                font=("arial",20,"bold"), text="9",
                command=lambda: buttonClick(9))
    btn_9.grid(row=2, column=2)

    btn_mul = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="*",
                command=lambda: buttonClick("*"))
    btn_mul.grid(row=2, column=3)

    # Row 3: 4, 5, 6, -
    btn_4 = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="4",
                command=lambda: buttonClick(4))
    btn_4.grid(row=3, column=0)

    btn_5 = Button(main, padx=29, bd=8, fg="black", 
                font=("arial",20,"bold"), text="5",
                command=lambda: buttonClick(5))
    btn_5.grid(row=3, column=1)

    btn_6 = Button(main, padx=33, bd=8, fg="black", 
                font=("arial",20,"bold"), text="6",
                command=lambda: buttonClick(6))
    btn_6.grid(row=3, column=2)

    btn_sub = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="-",
                command=lambda: buttonClick("-"))
    btn_sub.grid(row=3, column=3)

    # Row 4: 1, 2, 3, +
    btn_1 = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="1",
                command=lambda: buttonClick(1))
    btn_1.grid(row=4, column=0)

    btn_2 = Button(main, padx=29, bd=8, fg="black", 
                font=("arial",20,"bold"), text="2",
                command=lambda: buttonClick(2))
    btn_2.grid(row=4, column=1)

    btn_3 = Button(main, padx=33, bd=8, fg="black", 
                font=("arial",20,"bold"), text="3",
                command=lambda: buttonClick(3))
    btn_3.grid(row=4, column=2)

    btn_add = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="+",
                command=lambda: buttonClick("+"))
    btn_add.grid(row=4, column=3)

    # Row 5: 0, ., =
    btn_0 = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="0",
                command=lambda: buttonClick(0))
    btn_0.grid(row=5, column=0)


    btn_oBracket = Button(main, padx=29, bd=8, fg="black", 
                font=("arial",18,"bold"), text="(",
                command=lambda: buttonClick("("))
    btn_oBracket.grid(row=5, column=1)

    btn_cBracket = Button(main, padx=33, bd=8, fg="black", 
                font=("arial",18,"bold"), text=")",
                command=lambda: buttonClick(")"))
    btn_cBracket.grid(row=5, column=2)

    btn_eq = Button(main, padx=16, bd=8, fg="black", 
                font=("arial",20,"bold"), text="=",
                command=buttonEqual)
    btn_eq.grid(row=5, column=3)

    main.mainloop()
