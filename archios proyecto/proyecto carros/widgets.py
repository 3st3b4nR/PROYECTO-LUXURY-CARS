import tkinter as tk
from PIL import Image , ImageTk
import imagenes as img
import calculos as cl

#--------------------Interfaz----------------------#
interfaz=tk.Tk()
interfaz.title("LUXURY CARS")
interfaz.geometry("1250x630")
interfaz.resizable(0,0)
interfaz.config(bg="gold", bd=10, relief= "ridge")

#------Funciones de movimiento--------
contador = 0
#------Regresar carro-----#
def regresar():
    Boton1=tk.Button(interfaz, text="<", bg="black", fg="white", font=("georgia", 20) ,command=resta_avanzar ) 
    Boton1.place(x= 75, y=350, width= 40, height=40)
    
#------Avanzar carro-----#
def avanzar():
    Boton1=tk.Button(interfaz, text=">", bg="black", fg="white", font=("georgia", 20) ,command=suma_avanzar ) 
    Boton1.place(x= 475, y=350, width= 40, height=40)

#----IMAGEN DERECHA
def suma_avanzar():
    global contador, imagen_siguiente
    contador = (contador + 1) % 3
    imagen_siguiente = img.conversor(marca[contador]["Imagen"])
    carro.config(image=imagen_siguiente)


#------IMAGEN IZQUIERDA
def resta_avanzar():
    global contador, imagen_siguiente
    contador = (contador - 1) % 3
    imagen_siguiente = img.conversor(marca[contador]["Imagen"])
    carro.config(image=imagen_siguiente)

#----------------------Función para limpiar la pantalla----------------------#
def clean(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#------------ Credito --------
def credito():
    clean(interfaz)
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")

    titulo1=tk.Label(frame_blanco, text="- SELECIONA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="TU CREDITO", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.29, anchor="center")
        
    miimage=Image.open(r'C:\Users\Juanm\Python\ALGORITMOS 2\Imagen de WhatsApp 2025-02-25 a las 07.12.58_9f3472e6.jpg')#Abre la imagen
    miimage= miimage.resize((300,150))#medida de la imagen
    foto = ImageTk.PhotoImage(miimage)#La vonvierte en formato pillow
    labell = tk.Label(interfaz,image=foto)#La convierte en etiqueta}
    labell.image=foto
    labell.place(x=125, y=210)

    miimage=Image.open(r'C:\Users\Juanm\Python\ALGORITMOS 2\Imagen de WhatsApp 2025-02-25 a las 07.12.58_9f3472e6.jpg')#Abre la imagen
    miimage= miimage.resize((300,150))#medida de la imagen
    foto = ImageTk.PhotoImage(miimage)#La vonvierte en formato pillow
    labell = tk.Label(interfaz,image=foto)#La convierte en etiqueta}
    labell.image=foto
    labell.place(x=125, y=400)

    miimage=Image.open(r'C:\Users\Juanm\Python\ALGORITMOS 2\Imagen de WhatsApp 2025-02-25 a las 07.12.58_9f3472e6.jpg')#Abre la imagen
    miimage= miimage.resize((300,150))#medida de la imagen
    foto = ImageTk.PhotoImage(miimage)#La vonvierte en formato pillow
    labell = tk.Label(interfaz,image=foto)#La convierte en etiqueta}
    labell.image=foto
    labell.place(x=450, y=300)

    miimage=Image.open(r'C:\Users\Juanm\Python\ALGORITMOS 2\Imagen de WhatsApp 2025-02-25 a las 07.12.58_9f3472e6.jpg')#Abre la imagen
    miimage= miimage.resize((300,150))#medida de la imagen
    foto = ImageTk.PhotoImage(miimage)#La vonvierte en formato pillow
    labell = tk.Label(interfaz,image=foto)#La convierte en etiqueta}
    labell.image=foto
    labell.place(x=850, y=250)

    Boton1= tk.Button( interfaz, bg= "black", text= "Establecer \n Credito", fg="white")
    Boton1.config(width=42, height=2)
    Boton1.place(x= 850, y= 425)


#----------------------Página de compra----------------------#
def pag_compra():
    clean(interfaz)

    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- COMPRA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="TU CARRO", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.29, anchor="center")
    subrayado1=tk.Label(frame_blanco, text="________________________", font=("Georgia", 18), bg="white", fg="black", width=20, height=1)
    subrayado1.place(relx=0.25, rely=0.47, anchor="center")
    texto_confirma=tk.Label(frame_blanco, text="CONFIRMA TU COMPRA", font=("Georgia", 18), bg="white", fg="black")
    texto_confirma.place(relx=0.25, rely=0.45, anchor="center")
    texto_modelo=tk.Label(frame_blanco, text="Modelo:", font=("Georgia", 18), bg="white", fg="black")
    texto_modelo.place(relx=0.14, rely=0.52)
    texto_precio=tk.Label(frame_blanco, text="Precio:", font=("Georgia", 18), bg="white", fg="black")
    texto_precio.place(relx=0.14, rely=0.6)
    texto_papeleo=tk.Label(frame_blanco, text="Papeleo:", font=("Georgia", 18), bg="white", fg="black")
    texto_papeleo.place(relx=0.14, rely=0.68)
    subrayado2=tk.Label(frame_blanco, text="_________________________", font=("Georgia", 18), bg="white", fg="black", width=20, height=1)
    subrayado2.place(relx=0.135, rely=0.80)
    texto_impuesto=tk.Label(frame_blanco, text="Impuesto:", font=("Georgia", 18), bg="white", fg="black")
    texto_impuesto.place(relx=0.135, rely=0.76)
    texto_total=tk.Label(frame_blanco, text="Total:", font=("Georgia", 18), bg="white", fg="black")
    texto_total.place(relx=0.14, rely=0.88)

    contado_boton=tk.Button(frame_blanco, text="PAGAR DE CONTADO", font=("Georgia", 20), bg="black", fg="white", activebackground="white", activeforeground="black", cursor="hand2", command=pag_compra_exitosa)
    contado_boton.place(relx=0.7, rely=0.52, anchor="center")
    hacer_credito_boton=tk.Button(frame_blanco, text="HACER UN CRÉDITO", font=("Georgia", 20), bg="black", fg="white", activebackground="white", activeforeground="black", cursor="hand2", command= credito)
    hacer_credito_boton.place(relx=0.7, rely=0.82, anchor="center")

#----------------------Página de compra exitosa----------------------#
def pag_compra_exitosa():
    clean(interfaz)
    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1100, height=480)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- TU COMPRA -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frame_blanco, text="HA SIDO EXITOSA", font=("Georgia", 50), bg="white", fg="black")
    titulo2.place(relx=0.5, rely=0.32, anchor="center")
    texto_modelo=tk.Label(frame_blanco, text="Modelo:", font=("Georgia", 25), bg="white", fg="black")
    texto_modelo.place(relx=0.14, rely=0.42)
    texto_precio_total=tk.Label(frame_blanco, text="Precio Total:", font=("Georgia", 25), bg="white", fg="black")
    texto_precio_total.place(relx=0.14, rely=0.52)
    texto_cancelado=tk.Label(frame_blanco, text="Cancelado:", font=("Georgia", 25), bg="white", fg="black")
    texto_cancelado.place(relx=0.14, rely=0.62)
    texto_gracias=tk.Label(frame_blanco, text="GRACIAS POR CONFIAR EN", font=("Georgia", 40), bg="white", fg="black")
    texto_gracias.place(relx=0.5, rely=0.9, anchor="center")
    titulo1=tk.Label(interfaz, text="- LUXURY -", font=("Georgia", 25), bg="yellow", fg="black") 
    titulo1.place(relx=0.5,rely=0.92, anchor="center")
    titulo2=tk.Label(interfaz, text="  CARS  ", font=("Georgia", 15), bg="black", fg="yellow") 
    titulo2.place(relx=0.5,rely=0.97, anchor="center")


#----------------------Página de Lamborghini----------------------#
def pag_lamborghini():
    global carro, marca
    clean(interfaz)
    interfaz.config(bg="black")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- LAMBORGHINI -", font=("Georgia", 80), bg="white", fg="gold")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="black", fg="gold", activebackground="gold", activeforeground="black", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.75, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Lamborguini")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    avanzar()
    regresar()

#----------------------Página de Ferrari----------------------#
def pag_ferrari():
    global carro, marca
    clean(interfaz)
    interfaz.config(bg="#EB1B00")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")

    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- FERRARI -", font=("Georgia", 80), bg="white", fg="#DBD407")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="#EB1B00", fg="white", activebackground="white", activeforeground="#EB1B00", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.75, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Ferrari")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    avanzar()
    regresar()

#----------------------Página de Mercedes----------------------#
def pag_mercedes():
    global carro, marca
    clean(interfaz)
    interfaz.config(bg="#929292")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- MERCEDES -", font=("Georgia", 80), bg="white", fg="#929292")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="#929292", fg="white", activebackground="white", activeforeground="#929292", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.75, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Mercedes")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    avanzar()
    regresar()

#----------------------Página de BMW----------------------#
def pag_bmw():
    global carro, marca
    clean(interfaz)
    interfaz.config(bg="#1786EB")
    frame_blanco=tk.Frame(interfaz,bg="white", width=1200, height=600)
    frame_blanco.place(relx=0.5, rely=0.5, anchor="center")
    titulo1=tk.Label(frame_blanco, text="- BMW -", font=("Georgia", 80), bg="white", fg="#1786EB")
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    escoge_modelo=tk.Label(frame_blanco, text="ESCOGE TU MODELO", font=("georgia",30), bg="white", fg="black")
    escoge_modelo.place(relx=0.5, rely=0.3, anchor="center")
    boton_regresar=tk.Button(frame_blanco, text="<", bg="black", fg="white", font=("georgia", 20), command=menu)
    boton_regresar.place(relx=0.05, rely=0.09, anchor="center")

    precio_label=tk.Label(frame_blanco, text="Precio:", font=("Times New Roman", 30), bg="white", fg="black")
    precio_label.place(relx=0.5, rely=0.4)
    año_label=tk.Label(frame_blanco, text="Año:", font=("Times New Roman", 30), bg="white", fg="black")
    año_label.place(relx=0.5, rely=0.5)
    modelo_label=tk.Label(frame_blanco, text="Modelo:", font=("Times New Roman", 30), bg="white", fg="black")
    modelo_label.place(relx=0.5, rely=0.6)
    descripcion_label=tk.Label(frame_blanco, text="Descripción:", font=("Times New Roman", 30), bg="white", fg="black")
    descripcion_label.place(relx=0.5, rely=0.7)
    boton_comprar=tk.Button(frame_blanco, text="COMPRAR", font=("Georgia", 20), bg="#1786EB", fg="white", activebackground="white", activeforeground="#1786EB", cursor="hand2", command=pag_compra)
    boton_comprar.place(relx=0.75, rely=0.9, anchor="center")

    marca = cl.verificador_marca("Bmw")

    carro = tk.Label(interfaz)
    carro.place(x=125, y=260)
    avanzar()
    regresar()

#----------------------Interfaz principal----------------------#
def menu():
    global interfaz
    clean(interfaz) 
    interfaz.config(bg="yellow")
    frametitulo=tk.Frame(interfaz, bg="black", width=1240, height=620)
    frametitulo.pack()
    titulo1=tk.Label(frametitulo, text="- LUXURY -", font=("Georgia", 80), bg="yellow", fg="black") 
    titulo1.place(relx=0.5,rely=0.15, anchor="center")
    titulo2=tk.Label(frametitulo, text="  CARS  ", font=("Georgia", 50), bg="black", fg="yellow") 
    titulo2.place(relx=0.5,rely=0.285, anchor="center")

    escoger_marca=tk.Label(frametitulo, text="- ESCOGE TU MARCA -", font=("Georgia", 30), bg="black", fg="yellow")
    escoger_marca.place(relx=0.5, rely=0.43, anchor="center")

    boton_bmw=tk.Button(frametitulo, text="BMW", font=("Georgia", 20), bg="white", fg="black", width=10, height=1, activebackground="#1786EB", activeforeground="white", cursor="hand2", command=pag_bmw)
    boton_bmw.place(relx=0.15, rely=0.85, anchor="center")

    boton_mercedes=tk.Button(frametitulo, text="Mercedes", font=("Georgia", 20), bg="white", fg="black", width=10, height=1, activebackground="black", activeforeground="white", cursor="hand2", command=pag_mercedes)
    boton_mercedes.place(relx=0.385, rely=0.85, anchor="center")

    boton_ferrari=tk.Button(frametitulo, text="Ferrari", font=("Georgia", 20), bg="white", fg="black", width=10, height=1, activebackground="#EB1B00", activeforeground="white", cursor="hand2", command=pag_ferrari)
    boton_ferrari.place(relx=0.615, rely=0.85, anchor="center")

    boton_lamborghini=tk.Button(frametitulo, text="Lamborghini", font=("Georgia", 20), bg="white", fg="black", width=10, height=1,  activebackground="black", activeforeground="#EBBD36", cursor="hand2", command=pag_lamborghini)
    boton_lamborghini.place(relx=0.85, rely=0.85, anchor="center")

    interfaz.mainloop()

menu()
