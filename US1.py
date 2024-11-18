import tkinter as tk
import tkinter.font as tkFont

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("INTERCAMBIO NAVIDEÑO")
ventana.geometry("400x300")
ventana.configure(bg='#d6f5d6')  # Color de fondo

# Establecer la fuente Comic Sans
fuente = tkFont.Font(family="Comic Sans MS", size=12)

# Título de la aplicación
lbl_titulo = tk.Label(ventana, text="INTERCAMBIO NAVIDEÑO", font=("Comic Sans MS", 16), fg="red", bg="#d6f5d6")
lbl_titulo.pack(pady=10)

# Etiqueta y Campo de texto de Nombre
lbl_nombre = tk.Label(ventana, text="Nombre:", font=fuente, bg="#d6f5d6")
lbl_nombre.pack(pady=5)
txt_nombre = tk.Entry(ventana, font=fuente, width=30)
txt_nombre.pack(pady=5)

# Etiqueta y Campo de texto de Correo
lbl_correo = tk.Label(ventana, text="Correo:", font=fuente, bg="#d6f5d6")
lbl_correo.pack(pady=5)
txt_correo = tk.Entry(ventana, font=fuente, width=30)
txt_correo.pack(pady=5)

# Botones de Registrar y Continuar
btn_frame = tk.Frame(ventana, bg="#d6f5d6")
btn_frame.pack(pady=20)

btn_registro = tk.Button(btn_frame, text="Registrar", font=fuente, bg="white", fg="green", width=10)
btn_registro.pack(side="left", padx=10)

btn_continuar = tk.Button(btn_frame, text="Continuar", font=fuente, bg="white", fg="red", width=10)
btn_continuar.pack(side="right", padx=10)

# Ejecutar la aplicación
ventana.mainloop()
