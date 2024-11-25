import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
from PIL import Image, ImageTk
def centrar_ventana(ventanacen, width, height):
    wtotal = ventanacen.winfo_screenwidth()
    htotal = ventanacen.winfo_screenheight()
    pwidth = round(wtotal / 2 - width / 2)
    pheight = round(htotal / 2 - height / 2)-40

    #  Se lo aplicamos a la geometría de la ventana
    ventanacen.geometry(str(width) + "x" + str(height) + "+" + str(pwidth) + "+" + str(pheight))

# Ventana principal
ventana2 = tk.Toplevel()
centrar_ventana(ventana2, 800, 500)
ventana2.iconify()
ventana2.title("DATOS DEL INTERCAMBIO")
ventana2.geometry("800x500")

# Imagen de fondo
imagen_original = Image.open("images/fondo.png")
fondo = ImageTk.PhotoImage(imagen_original)
canvas = tk.Canvas(ventana2, width=800, height=500)
canvas.pack(fill="both", expand=True)
imagen_canvas = canvas.create_image(0, 0, image=fondo, anchor="nw")

# Fuente
fuente = tkFont.Font(family="Comic Sans MS", size=12)

# Título
lbl_titulo = tk.Label(canvas, text="INTERCAMBIO NAVIDEÑO", font=("Comic Sans MS", 16), fg="red", bg="#d6f5d6")
lbl_titulo.place(x=300, y=10)

# Etiquetas y widgets
lbl_lugar = tk.Label(canvas, text="Lugar del intercambio:", font=fuente, bg="#d6f5d6")
lbl_lugar.place(x=50, y=50)
txt_lugar = tk.Entry(canvas, font=fuente, width=40)
txt_lugar.place(x=300, y=50)

lbl_fecha = tk.Label(canvas, text="Fecha del intercambio:", font=fuente, bg="#d6f5d6")
lbl_fecha.place(x=50, y=100)
cal_fecha = DateEntry(canvas, font=fuente, width=18, background="darkred", foreground="white", borderwidth=2)
cal_fecha.place(x=300, y=100)

# Hora
lbl_hora = tk.Label(canvas, text="Hora (HH:MM):", font=fuente, bg="#d6f5d6")
lbl_hora.place(x=50, y=150)

combo_horas = ttk.Combobox(canvas, values=[f"{i:02}" for i in range(24)], font=fuente, width=5, state="readonly")
combo_horas.set("HH")
combo_horas.place(x=300, y=150)

lbl_dos_puntos = tk.Label(canvas, text=":", font=fuente, bg="#d6f5d6")
lbl_dos_puntos.place(x=360, y=150)

combo_minutos = ttk.Combobox(canvas, values=[f"{i:02}" for i in range(60)], font=fuente, width=5, state="readonly")
combo_minutos.set("MM")
combo_minutos.place(x=380, y=150)

# Temática
lbl_tematica = tk.Label(canvas, text="Temática del intercambio:", font=fuente, bg="#d6f5d6")
lbl_tematica.place(x=50, y=200)
tematicas = ["Sin temática", "Libros", "Manualidades", "Bufandas", "Tazas", "Suéteres"]
combo_tematica = ttk.Combobox(canvas, values=tematicas, font=fuente, width=35)
combo_tematica.set("Seleccionar temática")
combo_tematica.place(x=300, y=200)

# Presupuesto
lbl_presupuesto = tk.Label(canvas, text="Presupuesto (mín - máx):", font=fuente, bg="#d6f5d6")
lbl_presupuesto.place(x=50, y=250)
spin_presupuesto_min = tk.Spinbox(canvas, from_=50, to=1000, increment=50, width=10, font=fuente)
spin_presupuesto_min.place(x=300, y=250)
spin_presupuesto_max = tk.Spinbox(canvas, from_=50, to=1000, increment=50, width=10, font=fuente)
spin_presupuesto_max.place(x=400, y=250)

# Función para guardar la información
def guardar_informacion():
    lugar = txt_lugar.get()
    fecha = cal_fecha.get()
    hora = f"{combo_horas.get()}:{combo_minutos.get()}"
    tematica = combo_tematica.get()
    presupuesto_min = spin_presupuesto_min.get()
    presupuesto_max = spin_presupuesto_max.get()

    if not lugar or tematica == "Seleccionar temática":
        lbl_mensaje.config(text="Por favor, completa todos los campos obligatorios.", fg="red")
    else:
        lbl_mensaje.config(text="¡Información guardada exitosamente!", fg="green")

# Función para obtener los datos del intercambio
def obtener_datos_intercambio():
    lugar = txt_lugar.get()
    fecha = cal_fecha.get()
    hora = f"{combo_horas.get()}:{combo_minutos.get()}"
    tematica = combo_tematica.get()
    presupuesto_min = spin_presupuesto_min.get()
    presupuesto_max = spin_presupuesto_max.get()
    
    return {
        "lugar": lugar,
        "fecha": fecha,
        "hora": hora,
        "tematica": tematica,
        "presupuesto_min": presupuesto_min,
        "presupuesto_max": presupuesto_max,
    }


# Función para mostrar los registros en consola
def mostrar_registros():
    lugar = txt_lugar.get()
    fecha = cal_fecha.get()
    hora = f"{combo_horas.get()}:{combo_minutos.get()}"
    tematica = combo_tematica.get()
    presupuesto_min = spin_presupuesto_min.get()
    presupuesto_max = spin_presupuesto_max.get()

    if not lugar or tematica == "Seleccionar temática":
        print("Error: Faltan campos por completar.")
    else:
        mensaje = (
            f"Lugar: {lugar}\n"
            f"Fecha: {fecha}\n"
            f"Hora: {hora}\n"
            f"Temática: {tematica}\n"
            f"Presupuesto: ${presupuesto_min} - ${presupuesto_max}"
        )
        print("Datos del intercambio:")
        print(mensaje)


# Botones
btn_guardar = tk.Button(canvas, text="Guardar", font=fuente, bg="white", fg="green", width=10, command=guardar_informacion)
btn_guardar.place(x=300, y=300)

btn_mostrar = tk.Button(canvas, text="Mostrar Registros", font=fuente, bg="white", fg="blue", width=15, command=mostrar_registros)
btn_mostrar.place(x=420, y=300)

btn_continuar2 = tk.Button(canvas, text="Continuar", font=fuente, bg="white", fg="purple", width=10)
btn_continuar2.place(x=360, y=350)

# Mensaje de estado ajustado
lbl_mensaje = tk.Label(canvas, text="", font=fuente, bg="#d6f5d6")
lbl_mensaje.place(x=50, y=400)

# Función para redimensionar la imagen al tamaño de la ventana
def ajustar_imagen(event=None):
    nueva_imagen = imagen_original.resize((ventana2.winfo_width(), ventana2.winfo_height()))
    fondo_nuevo = ImageTk.PhotoImage(nueva_imagen)
    canvas.itemconfig(imagen_canvas, image=fondo_nuevo)
    canvas.fondo_nuevo = fondo_nuevo 

# Ajuste de la imagen al tamaño de la ventana
ventana2.update_idletasks()
ajustar_imagen()

# Redimensionamiento
ventana2.bind("<Configure>", ajustar_imagen)

