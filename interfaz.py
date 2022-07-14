# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:37:48 2022

@author: Topacio Manrique
"""

import tkinter as tk
from tkinter import messagebox

def validar():
    if entrada.get()== "name":
        abrirventana2()
    else:
        messagebox.showwarning("Usuario o contraseña incorrecta")
        
def abrirventana2():
    import tkinter as tk
    from tkinter import messagebox
    ventana = tk.Tk()
    ventana.title("Informacion de clientes")
    ventana.geometry("500x800")

    etiqueta = tk.Label(ventana, text = "Introduce el nombre del cliente")
    etiqueta.pack()
    
    etiqueta = tk.Label(ventana, text = "Cliente")
    etiqueta.pack()
    cajaTexto = tk.Entry(ventana)
    cajaTexto.pack()
    
    boton2 = tk.Button(ventana, text = "Buscar", command = mostrar_informacion)
    boton2.pack(side=tk.TOP)
    
    ventana.mainloop()


def saludo(name):
    print("Hola " + name)  
    
def mostrar_informacion():
    if nivel_autorizacion = 
        print("")    
    
def cerrarventana():
    ventana.destroy()
    
    
    
import tkinter as tk
from tkinter import messagebox    
ventana = tk.Tk()
ventana.title("BBVA Ejecutivos")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text = "Bienvenido ejecutivo ")
etiqueta.pack()

etiqueta = tk.Label(ventana, text = "Usuario")
etiqueta.pack()
cajaTexto = tk.Entry(ventana)
cajaTexto.pack()

etiqueta = tk.Label(ventana, text = "Contraseña")
etiqueta.pack()
cajaTexto = tk.Entry(ventana)
cajaTexto.pack()

boton1 = tk.Button(ventana, text = "Acceder", command = abrirventana2)
boton1.pack(side=tk.TOP)

ventana.mainloop()



