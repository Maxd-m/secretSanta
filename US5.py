from tkinter import Button, font, Canvas, Label, Toplevel, messagebox
from tkinter.ttk import Progressbar, Treeview
from PIL import Image, ImageTk
import random
from US1 import lista
from US6 import tree, ventana6, enviar_correos
from US6 import ventana6

def centrar_ventana(ventanacen, width, height):
    wtotal = ventanacen.winfo_screenwidth()
    htotal = ventanacen.winfo_screenheight()
    pwidth = round(wtotal / 2 - width / 2)
    pheight = round(htotal / 2 - height / 2) - 40
    ventanacen.geometry(f"{width}x{height}+{pwidth}+{pheight}")

ventana5 = Toplevel()
ventana5.iconify()
centrar_ventana(ventana5, 800, 400)
canvas = Canvas(ventana5, width=800, height=400)
canvas.pack(fill="both", expand=True, ipadx=10, ipady=10)
image = Image.open('images/christmas.png')
imagec = Image.open('images/carga.png')
imagec = ImageTk.PhotoImage(imagec.resize((600, 300)))
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
    ventana5.iconify()
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
    carg = Label(ventana55, text="Cargando...", font=fuentet, bg='#660504', fg='gray')
    carg.place(x=225, y=40)
    lrul = Label(ventana55, image=photore, bg='#025136')
    lrul.place(x=220, y=90)

    def rotate_image():
        current_angle = (rotate_image.angle + 1) % 360
        rotate_image.angle = current_angle
        rotated_imager = imagere.rotate(current_angle)
        rotated_photor = ImageTk.PhotoImage(rotated_imager)
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
        progress_bar['value'] += 1
        ventana55.after(100, update_progress, progress_bar, ventana55)
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
    btn_final = Button(ventana_final, text="Salir", command=ventana5.master.destroy, bg='#660504', fg='gray',
                       font=("Comic Sans MS", 14), bd=0, relief="flat")
    btn_final.place(x=220, y=296)

    # Botón de Resultados
    btn_resultados = Button(ventana_final, text="Resultados", bg='#126a4c', fg='lime green',
                            font=("Comic Sans MS", 12), bd=0, relief="flat", command=mostrar_resultados)
    btn_resultados.place(x=403, y=297)

    # Botón para enviar correos
    btn_enviar_correos = Button(ventana_final, text="Enviar Correos", bg='#126a4c', fg='white',
                                font=("Comic Sans MS", 12), bd=0, relief="flat", command=enviar_correos)
    btn_enviar_correos.place(x=300, y=350)

    realizar_sorteo()

def mostrar_resultados():
    """Muestra la ventana de US6 que estaba oculta."""
    ventana6.deiconify()  # Vuelve visible la ventana de US6
    ventana5.iconify()    # Opcional: Minimiza la ventana actual si quieres


ventana5.bind('<Configure>', resize_image)
ventana5.update_idletasks()
ventana5.geometry(f"{ventana5.winfo_width()}x{ventana5.winfo_height()}")
btn_sortear = Button(ventana5, text="Sortear", font=fuente, command=open_window, bg='#660504', fg='gray')
btn_sortear.place(x=360, y=310)

imager = Image.open('images/ruleta.png')
imager = imager.resize((200, 200))
photor = ImageTk.PhotoImage(imager)
lruleta = Label(ventana5, image=photor, bg='#660504')
lruleta.place(x=300, y=100)

def rotate_image():
    current_angle = (rotate_image.angle + 1) % 360
    rotate_image.angle = current_angle
    rotated_imager = imager.rotate(current_angle)
    rotated_photor = ImageTk.PhotoImage(rotated_imager)
    lruleta.config(image=rotated_photor)
    lruleta.image = rotated_photor
    ventana5.after(20, rotate_image)

lista_participantes = []
def realizar_sorteo():
    elemento = lista.cabeza
    for i in range(lista.contar_participantes()):
        lista_participantes.append(elemento)
        elemento = elemento.siguiente

    for i in range(len(lista_participantes)):
        ind_aleatorio = random.randint(0, len(lista_participantes) - 1)
        temporal = lista_participantes[i]
        lista_participantes[i] = lista_participantes[ind_aleatorio]
        lista_participantes[ind_aleatorio] = temporal

    for j in range(len(lista_participantes)):
        if j == len(lista_participantes) - 1:
            tree.insert("", "end", values=(lista_participantes[j].correo, lista_participantes[0].correo))
        else:
            tree.insert("", "end", values=(lista_participantes[j].correo, lista_participantes[j + 1].correo))

rotate_image.angle = 0
rotate_image()
