from tkinter import*

ventana = Tk()
ventana.title('Hola')
lbl = Label(ventana,text='Hola Mundo').pack()
Label(ventana,text='Hola Mundo').pack(anchor=NW)
Label(ventana,text='Hola Mundo2').pack(anchor=CENTER)
Label(ventana,text='Hola Mundo3').pack(anchor=SW)
Label.config(fg='white', bg='black', font=('Verdana',100))
ventana.mainloop()