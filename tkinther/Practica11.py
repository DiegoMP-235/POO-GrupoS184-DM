from tkinter import Tk,Button,Frame

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

#Llamamos al metodo para mostrar la ventana
ventana.mainloop()