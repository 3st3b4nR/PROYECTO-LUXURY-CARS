from PIL import Image, ImageTk

# ---- Abre la imagen y luego la transforma a formato pillow -----
def conversor(ubicacion):
    imagen = Image.open(ubicacion)
    imagen = imagen.resize((340, 196))
    foto = ImageTk.PhotoImage(imagen)
    return foto

