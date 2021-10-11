from tkinter import*

ventana = Tk()
ventana.title('Inventario de Computo Plus')
ventana.geometry('800x600')
etiqueta = Label(ventana, text='Bienvenidos al Sistema de Inventario',
    font=('Arial Bold', 30), bg='pink', fg='green')
etiqueta.grid(column =0, row=0)
inventario = {'id': '1', 'producto':'mouse', 'proveedor':'spark', 'existencia':'27'}


ventana.mainloop()
