from tkinter import *
from tkinter import messagebox


ventana = Tk()
ventana.config(bd=25)

nombre = StringVar()
apellido = StringVar()
edad = StringVar()
profesion = StringVar()

Label(ventana, text='Nombre').pack()
Entry(ventana, justify='center', textvariable=nombre).pack()

Label(ventana, text='Apellido').pack()
Entry(ventana, justify='center', textvariable=apellido).pack()

Label(ventana, text='Edad').pack()
Entry(ventana, justify='center', textvariable=edad).pack()

Label(ventana, text='Profesión').pack()
Entry(ventana, justify='center', textvariable=profesion).pack()

#Label(ventana, text='Resultado').pack()
#Entry(ventana, justify='center', textvariable=resultado, state='disabled').pack()

def mostrarinfo():
    messagebox.showinfo(' INFORMACIÓN ', ' Nombre : ' +  nombre.get() + '\n Apellido: ' + apellido.get() + '\n Edad: ' + edad.get() + '\n Profesion: ' + profesion.get())

Button(ventana, text='Mostrar Información', command=mostrarinfo).pack()

ventana.mainloop()