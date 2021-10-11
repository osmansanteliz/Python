from tkinter import*
import time

ventana = Tk()
ventana.title('Hola')
def accion():
    ventana.sleep(3)
    ventana.deiconify()


boton = Button(ventana, text='inicio', command= accion)
boton.pack()
ventana.mainloop()