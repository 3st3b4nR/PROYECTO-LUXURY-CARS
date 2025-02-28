import tkinter as tk
from calculos import inventario_mercedes
import imagenes as img # Importamos la función desde funciones.py

indice = 0
imagen_actual = None  # Variable global para la imagen

def siguiente():
    global indice, imagen_actual
    indice = (indice + 1) % 3  # Asegurar que el índice esté en rango
    imagen_actual = img.label(inventario_mercedes[indice]["Imagen"])
    mer.config(image=imagen_actual)

# ---- Configuración de la ventana ----
root = tk.Tk()

mer = tk.Label(root)  # Creamos el Label sin imagen al inicio
mer.pack()

boton = tk.Button(root, text="Siguiente", command=siguiente)
boton.pack()

root.mainloop()