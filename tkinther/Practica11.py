from tkinter import Tk,Button,Frame,messagebox
#creamos funciones para probar el command
def muestraMensaje():
    messagebox.showinfo("Aviso!","Haz presionado el boton")
    messagebox.showerror("Error","La tarea fallo con exito")
    messagebox.askquestion("Pregunta","Te gusta la pizza con pinia")

    answer = messagebox.askyesnocancel("Prueba","Si?\nNo?\nCancelar?")
    print(answer)
#6.Funcion para agregar botones
def agregarBoton():
    botonVerde.config(text="+",bg="#00CC00",fg="#FFFFFF")
    botonNew = Button(seccion3,text="Nuevo BTN")
    botonNew.pack()
    
#1.Instanciamos un objeto de tipo "ventana"
ventana = Tk()
ventana.title("Mi primera interfaz grafica (con 3 frames)")
ventana.geometry("600x400")
#2.Agregamos los frames
seccion1 = Frame(ventana,bg="#FF0000")
seccion1.pack(expand=True,fill='both')

seccion2 = Frame(ventana,bg="#00FF00")
seccion2.pack(expand=True,fill='both')

seccion3 = Frame(ventana,bg="#0000FF")
seccion3.pack(expand=True,fill='both')

#3.Agregamos botones
boton1 = Button(seccion1,text="Soy un boton azul",fg="blue",font="bold",command=muestraMensaje)
boton1.place(x = 60,y = 60)


boton2 = Button(seccion2,text="Soy un boton amarillo",bg="#f6ff08",fg="#000000")
boton2.grid(row = 1,column = 1)

boton3 = Button(seccion2,text="Soy un boton negro",bg="#000000",fg="#FFFFFF")
boton3.grid(row = 0,column = 0)

botonVerde = Button(seccion3,text="Soy boton verde",bg="#008800",font="Sans-serif",fg="#FFFFFF",command=agregarBoton)
botonVerde.configure(height=2,width=10)
botonVerde.pack()

#Llamamos al metodo para mostrar la ventana
ventana.mainloop()