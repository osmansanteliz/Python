from tkinter import *


def sumar():
    resultado.set(float(num1.get()) + float(num2.get()))

ventana = Tk()
ventana.config(bd=25)

num1 = StringVar()
num2 = StringVar()
resultado = StringVar()

Label(ventana, text='Numero 1').pack()
Entry(ventana, justify='center', textvariable=num1).pack()

Label(ventana, text='Numero 2').pack()
Entry(ventana, justify='center', textvariable=num2).pack()

Label(ventana, text='Resultado').pack()
Entry(ventana, justify='center', textvariable=resultado, state='disabled').pack()

Button(ventana, text='sumar', command=sumar).pack()

ventana.mainloop()