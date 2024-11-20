from tkinter import Tk, Button, font, Canvas, Label, Toplevel
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import random


class Nodo:
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.siguiente = None

def centrar_ventana(ventanacen, width, height):
    wtotal = ventanacen.winfo_screenwidth()
    htotal = ventanacen.winfo_screenheight()
    pwidth = round(wtotal / 2 - width / 2)
    pheight = round(htotal / 2 - height / 2)-40

    #  Se lo aplicamos a la geometría de la ventana
    ventanacen.geometry(str(width) + "x" + str(height) + "+" + str(pwidth) + "+" + str(pheight))

ventana5 = Tk()
centrar_ventana(ventana5, 800, 400)
canvas = Canvas(ventana5, width=800, height=400)
canvas.pack(fill="both", expand=True)
image = Image.open('images/christmas.png')
imagec = Image.open('images/carga.png')
imagec = ImageTk.PhotoImage(imagec.resize((600,300)))
fuente = font.Font(family="Comic Sans MS", size=12)
fuentet = font.Font(family="Comic Sans MS", size=20)
imagere = Image.open('images/ruleta.png')
imagere = imagere.resize((150, 150))
photore = ImageTk.PhotoImage(imagere)

def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_image = image.resize((new_width, new_height))
    photo_resized = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=photo_resized, anchor="nw")
    canvas.image = photo_resized

def open_window():
    ventana55 = Toplevel(ventana5)
    ventana55.grab_set_global()
    ventana55.grab_set()
    ventana55.focus_set()
    global canvasc
    ventana55.overrideredirect(True)
    centrar_ventana(ventana55, 600, 300)
    canvasc = Canvas(ventana55, width=400, height=200)
    canvasc.pack(fill="both", expand=True)
    canvasc.create_image(0, 0, image=imagec, anchor="nw")
    canvasc.image = imagec
    progress_bar = Progressbar(ventana55, length=200, mode='determinate')
    progress_bar.place(x=193, y=250)
    start_progress(progress_bar, ventana55)
    carg= Label(ventana55, text="Cargando...", font=fuentet, bg='#660504', fg='gray')
    carg.place(x=225, y=40)
    lrul = Label(ventana55, image=photore, bg='#025136')
    lrul.place(x=220, y=90)

    def rotate_image():
        current_angle = (rotate_image.angle + 1) % 360
        rotate_image.angle = current_angle
        rotated_imager = imagere.rotate(current_angle)  # Rotar la imagen
        rotated_photor = ImageTk.PhotoImage(rotated_imager)  # Convertir la imagen a PhotoImage
        lrul.config(image=rotated_photor)
        lrul.image = rotated_photor
        ventana55.after(1, rotate_image)

    rotate_image.angle = 0
    rotate_image()

def start_progress(progress_bar, ventana55):
    progress_bar['value'] = 0
    update_progress(progress_bar, ventana55)

def update_progress(progress_bar, ventana55):
    if progress_bar['value'] < 100:
        progress_bar['value'] += 1  # Aumentar el valor de la barra de progreso
        ventana55.after(100, update_progress, progress_bar, ventana55)  # Repetir cada 100ms
    else:
        on_progress_complete(progress_bar, ventana55)

def on_progress_complete(progress_bar, ventana55):
    progress_bar.stop()
    ventana55.destroy()
    ventana_final = Toplevel(ventana5)
    ventana_final.grab_set_global()
    ventana_final.grab_set()
    ventana_final.overrideredirect(True)
    ventana_final.focus_set()

    centrar_ventana(ventana_final, 700, 400)
    canvasfinal = Canvas(ventana_final, width=700, height=400)
    canvasfinal.pack(fill="both", expand=True)
    imagefinal = Image.open('images/venfinal.png')
    resized_image_fin = imagefinal.resize((700, 400))
    photo_resized_fin = ImageTk.PhotoImage(resized_image_fin)
    canvasfinal.create_image(0, 0, image=photo_resized_fin, anchor="nw")
    canvasfinal.image = photo_resized_fin
    btn_final = Button(ventana_final, text="Salir", command=ventana5.destroy, bg='#660504', fg='gray',
                       font=("Comic Sans MS", 14), bd=0, relief="flat")
    btn_final.place(x=325, y=295)
    realizar_sorteo()


ventana5.bind('<Configure>', resize_image)
ventana5.update_idletasks()
ventana5.geometry(f"{ventana5.winfo_width()}x{ventana5.winfo_height()}")
btn_sortear = Button(ventana5, text="Sortear", font=fuente, command=open_window, bg='#660504', fg='gray')
btn_sortear.place(x=360, y=310)


imagee = Image.open('images/exit.png')
imagee = imagee.resize((100, 100))
photoe = ImageTk.PhotoImage(imagee)
#btn_back = Button(ventana5, width=100, height=100,image=photoe, bd=0
                  #,compound="center", bg='#660504',relief="flat", fg='gray')
#btn_back.place(x=0, y=0)

imager = Image.open('images/ruleta.png')
imager = imager.resize((200, 200))
photor = ImageTk.PhotoImage(imager)
lruleta=Label(ventana5, image=photor, bg='#660504')
lruleta.place(x=300, y=100)



def rotate_image():
    current_angle = (rotate_image.angle + 1) % 360
    rotate_image.angle = current_angle
    rotated_imager = imager.rotate(current_angle)  # Rotar la imagen
    rotated_photor = ImageTk.PhotoImage(rotated_imager)  # Convertir la imagen a PhotoImage
    lruleta.config(image=rotated_photor)
    lruleta.image = rotated_photor
    ventana5.after(20, rotate_image)

def realizar_sorteo():
    nodo1 = Nodo(1, 'Elias', 'eliasct72@1')
    nodo2 = Nodo(2, 'Rabo', 'rabo72@1')
    nodo3 = Nodo(3, 'Max', 'Max@1')
    nodo4 = Nodo(4, 'Juan', 'juan@2')
    lista = [nodo1, nodo2, nodo3, nodo4]
    for i in range(len(lista)):
        ind_aleatorio= random.randint(0, len(lista) - 1)
        temporal = lista[i]
        lista[i] = lista[ind_aleatorio]
        lista[ind_aleatorio] = temporal

    for j in range(len(lista)):
        if j == len(lista)-1:
            print("El usuario " + str(lista[j].nombre)+ ", le regala a " + str(lista[0].nombre))
        else:
            print("El usuario " + str(lista[j].nombre)+ ", le regala a " + str(lista[j+1].nombre))

rotate_image.angle = 0
rotate_image()
ventana5.mainloop()