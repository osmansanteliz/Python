from tkinter import*

ventana = Tk()
ventana.title('Hola')
etiqueta = Label(ventana, text='Pythoneros', font=('Arial Bold', 50), bg='blue', fg='red')
etiqueta.grid(column=0, row=0)
ventana.geometry('350x200')
Button(ventana, text='soy un boton').pack()
ventana.mainloop()