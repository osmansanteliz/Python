from tkinter import*
import time

ventana = Tk()
ventana.title('Hola')
Label(ventana, text='Ingrese su nombre').pack()
Entry(ventana, justify='center').pack()
Label(ventana, text='Ingrese su apellido').pack()
Entry(ventana, justify='center').pack()
Label(ventana, text='Ingrese su edad').pack()
Entry(ventana, justify='center').pack()
ventana.mainloop()