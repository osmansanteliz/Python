from tkinter import*

ventana = Tk()
ventana.title('Hola')

texto = StringVar()
texto.set('Nuevo Texto')
Label.config(texto=texto)
ventana.mainloop()