import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
from PIL import Image, ImageTk

intercambios = []  # Lista global para almacenar intercambios

# Ventana principal
ventana = tk.Tk()
ventana.title("DATOS DEL INTERCAMBIO")
ventana.geometry("800x400")

# Imagen de fondo
imagen_original = Image.open("images/fondo.png")
fondo = ImageTk.PhotoImage(imagen_original)
canvas = tk.Canvas(ventana, width=800, height=400)
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

# Guardar la información
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
        datos_intercambio = {
            "Lugar": lugar,
            "Fecha": fecha,
            "Hora": hora,
            "Temática": tematica,
            "Presupuesto Mínimo": presupuesto_min,
            "Presupuesto Máximo": presupuesto_max
        }
        intercambios.append(datos_intercambio)  # Guardar datos
        lbl_mensaje.config(text="¡Información guardada exitosamente!", fg="green")
        print("Intercambio guardado:", datos_intercambio)  # Para depuración


def mostrar_registros():
    ventana_registros = tk.Toplevel()
    ventana_registros.title("Registros de Intercambios")
    ventana_registros.geometry("600x400")

    text_area = tk.Text(ventana_registros, font=fuente, wrap="word")
    text_area.pack(expand=True, fill="both")

    for i, intercambio in enumerate(intercambios, start=1):
        registro = f"Intercambio {i}:\n"
        for clave, valor in intercambio.items():
            registro += f"{clave}: {valor}\n"
        registro += "\n"
        text_area.insert("end", registro)

    text_area.config(state="disabled")  # Evitar edición

# Botón para guardar
btn_guardar = tk.Button(canvas, text="Guardar", font=fuente, bg="white", fg="green", width=10, command=guardar_informacion)
btn_guardar.place(x=300, y=300)

# Botón para ver datos
btn_ver_registros = tk.Button(canvas, text="Ver Registros", font=fuente, bg="white", fg="blue", width=15, command=mostrar_registros)
btn_ver_registros.place(x=420, y=300)


# Mensaje de estado
lbl_mensaje = tk.Label(canvas, text="", font=fuente, bg="#d6f5d6")
lbl_mensaje.place(x=300, y=350)

# Función para redimensionar la imagen al tamaño de la ventana
def ajustar_imagen(event=None):
    nueva_imagen = imagen_original.resize((ventana.winfo_width(), ventana.winfo_height())) 
    fondo_nuevo = ImageTk.PhotoImage(nueva_imagen)
    canvas.itemconfig(imagen_canvas, image=fondo_nuevo)
    canvas.fondo_nuevo = fondo_nuevo 

# Ajuste de la imagen al tamaño de la ventana
ventana.update_idletasks() 
ajustar_imagen()

# Redimensionamiento
ventana.bind("<Configure>", ajustar_imagen)

ventana.mainloop()
