from tkinter.ttk import Treeview, Style
from tkinter import Toplevel, font, Canvas, Button, Scrollbar, Frame, messagebox
from PIL import Image, ImageTk
from tkinter import Toplevel, Canvas, Label, font, ttk, messagebox
from tkinter.ttk import Treeview
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from US2 import obtener_datos_intercambio


# Configuración del servidor SMTP (asegúrate de modificar esto con tu información)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = '21030149@itcelaya.edu.mx'  # Cambia esto por tu correo electrónico
EMAIL_PASSWORD = 'pahtketdlucfidjq'       # Cambia esto por tu contraseña

ventana6 = Toplevel()
ventana6.title("Resultados del Sorteo")
ventana6.iconify()  # La ventana comienza oculta
fuente = font.Font(family="Comic Sans MS", size=14)
ventana6.geometry("700x400")

# Fondo de la ventana
canvas = Canvas(ventana6, width=700, height=400, bg='#025136')
canvas.pack(fill="both", expand=True)

titulo = Label(ventana6, text="Resultados del Sorteo", font=("Comic Sans MS", 18, "bold"), bg='#126a4c', fg='white')
titulo.pack(pady=10)

# Configuración de la tabla Treeview
tree = Treeview(ventana6, columns=("Participante", "Pareja"), show="headings", height=15)
tree.heading("Participante", text="Participante")
tree.heading("Pareja", text="Pareja")
tree.column("Participante", width=200, anchor="center")
tree.column("Pareja", width=200, anchor="center")
tree.pack(pady=20)

import re

# Función para validar una dirección de correo electrónico
def es_correo_valido(correo):
    correo = correo.strip()  # Eliminar espacios al principio y al final
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, correo):
        return True
    return False

def enviar_correos():
    try:
        datos_intercambio = obtener_datos_intercambio()
        lugar = datos_intercambio["lugar"]
        fecha = datos_intercambio["fecha"]
        hora = datos_intercambio["hora"]
        tematica = datos_intercambio["tematica"]
        presupuesto_min = datos_intercambio["presupuesto_min"]
        presupuesto_max = datos_intercambio["presupuesto_max"]

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Inicia conexión segura
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Inicia sesión
        
        # Recorre los datos de la tabla y envía un correo a cada participante
        for item in tree.get_children():
            participante, pareja = tree.item(item, "values")
            
            # Agregar depuración para ver el correo
            print(f"Validando correo: {participante}")
            
            # Validar si el correo del participante es válido
            if not es_correo_valido(participante):
                messagebox.showerror("Error", f"La dirección de correo '{participante}' no es válida.")
                return  # Detener la ejecución si encontramos un correo inválido
            
            # Construcción del mensaje
            subject = "Resultado del Sorteo"
            body = (f"Hola {participante},\n\n"
                    f"Te informamos que tu pareja asignada en el sorteo es: {pareja}.\n\n"
                    f"Datos del intercambio:\n"
                    f"- Lugar: {lugar}\n"
                    f"- Fecha: {fecha}\n"
                    f"- Hora: {hora}\n"
                    f"- Temática: {tematica}\n"
                    f"- Presupuesto: ${presupuesto_min} - ${presupuesto_max}\n\n"
                    f"¡Felicidades y que lo disfrutes!\n\n"
                    f"Atentamente,\nEl equipo organizador.")
            
            message = MIMEMultipart()
            message["From"] = EMAIL_ADDRESS
            message["To"] = participante
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            
            server.send_message(message)
        
        server.quit()  # Cierra la conexión con el servidor SMTP
        messagebox.showinfo("Éxito", "Los correos han sido enviados con éxito.")
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron enviar los correos.\n{str(e)}")

style = Style()
style.configure("Treeview",
                font=("Arial", 15),
                background="#660504",
                fieldbackground="#ffffff",
                foreground="grey",
                rowheight=25)

style.configure("Treeview.Heading",
                font=("Arial", 13, "bold"),
                background="#4CAF50",
                foreground="lime green")

frame = Frame(ventana6)
frame.pack(padx=10, pady=10)
tree = Treeview(ventana6, columns=("Participante", "Regala a"), show='headings', height=5)
tree.heading("Participante", text="Participante")
tree.heading("Regala a", text="Regala a")
tree.column("Participante", width=200)
tree.column("Regala a", width=200)
tree.place(x=195, y=120)

#wa
scrollbar_y = Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
scrollbar_x.pack(side="bottom", fill="x")
tree.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)