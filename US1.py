import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

def centrar_ventana(ventanacen, width, height):
    wtotal = ventanacen.winfo_screenwidth()
    htotal = ventanacen.winfo_screenheight()
    pwidth = round(wtotal / 2 - width / 2)
    pheight = round(htotal / 2 - height / 2)-40

    #  Se lo aplicamos a la geometría de la ventana
    ventanacen.geometry(str(width) + "x" + str(height) + "+" + str(pwidth) + "+" + str(pheight))
# Clase para representar un nodo en la lista enlazada
class Nodo:
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.siguiente = None


# Clase para manejar la lista enlazada de participantes
class ListaParticipantes:
    def __init__(self):
        self.cabeza = None
        self.id = 1  # Contador de IDs

    def agregar_participante(self, nombre, correo):
        nuevo_nodo = Nodo(self.id, nombre, correo)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.id += 1  # Incrementar ID automáticamente

    def contar_participantes(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

# Función para registrar un participante
def registrar_participante():
    nombre = txt_nombre.get().strip()
    correo = txt_correo.get().strip()

    if nombre and correo:  # Validamos que los campos no estén vacíos
        lista.agregar_participante(nombre, correo)
        lbl_mensaje.config(text="Registro exitoso", fg="green")
        txt_nombre.delete(0, tk.END)  # Limpiar campo de texto
        txt_correo.delete(0, tk.END)
    else:
        lbl_mensaje.config(text="Faltan campos por llenar", fg="red")

# Función para continuar
def continuar():
    if lista.contar_participantes() >= 3:
        lbl_mensaje.config(text="Avanzando a la siguiente pantalla", fg="blue")
        # Aquí se puede implementar la lógica para cambiar a la siguiente pantalla
    else:
        lbl_mensaje.config(text="Faltan participantes por registrar", fg="red")

# Función para redimensionar la imagen al tamaño de la ventana
def ajustar_imagen(event=None):
    nueva_imagen = imagen_original.resize((ventana1.winfo_width(), ventana1.winfo_height()))
    fondo_nuevo = ImageTk.PhotoImage(nueva_imagen)
    canvas.itemconfig(imagen_canvas, image=fondo_nuevo)
    canvas.fondo_nuevo = fondo_nuevo 

def mostrar_participantes():
    actual = lista.cabeza
    print("Lista de participantes registrados")
    while actual:
        print(f"ID: {actual.id}, Nombre: {actual.nombre}, Correo: {actual.correo}")
        actual = actual.siguiente

# Crear la lista enlazada de participantes
lista = ListaParticipantes()

# Ventana principal
ventana1 = tk.Tk()
ventana1.title("INTERCAMBIO NAVIDEÑO")
ventana1.geometry("800x400")
centrar_ventana(ventana1, 800,400)

# Imagen de fondo
imagen_original = Image.open("images/fondo.png")
fondo = ImageTk.PhotoImage(imagen_original)
canvas = tk.Canvas(ventana1, width=800, height=400)
canvas.pack(fill="both", expand=True)
imagen_canvas = canvas.create_image(0, 0, image=fondo, anchor="nw")

# Fuente
fuente = tkFont.Font(family="Comic Sans MS", size=12)

# Título
lbl_titulo = tk.Label(canvas, text="INTERCAMBIO NAVIDEÑO", font=("Comic Sans MS", 16), fg="red", bg="#d6f5d6")
lbl_titulo.place(x=300, y=20)

# Campos de texto
lbl_nombre = tk.Label(canvas, text="Nombre:", font=fuente, bg="#d6f5d6")
lbl_nombre.place(x=300, y=80)
txt_nombre = tk.Entry(canvas, font=fuente, width=30)
txt_nombre.place(x=300, y=110)

lbl_correo = tk.Label(canvas, text="Correo:", font=fuente, bg="#d6f5d6")
lbl_correo.place(x=300, y=150)
txt_correo = tk.Entry(canvas, font=fuente, width=30)
txt_correo.place(x=300, y=180)

# Mensaje de estado
lbl_mensaje = tk.Label(canvas, text="", font=fuente, bg="#d6f5d6")
lbl_mensaje.place(x=300, y=280)

# Botones de Registrar y Continuar
btn_registro = tk.Button(canvas, text="Registrar", font=fuente, bg="white", fg="green", width=10, command=registrar_participante)
btn_registro.place(x=300, y=230)

btn_continuar = tk.Button(canvas, text="Continuar", font=fuente, bg="white", fg="red", width=10)
btn_continuar.place(x=420, y=230)

btn_mostrar = tk.Button(canvas, text="Mostrar registros", font=fuente, bg="white", fg="blue", width=15, command=mostrar_participantes)
btn_mostrar.place(x=300, y=320)

# Ajuste de la imagen al tamaño de la ventana
ventana1.update_idletasks()
ajustar_imagen()

# Redimensionamiento
ventana1.bind("<Configure>", ajustar_imagen)
