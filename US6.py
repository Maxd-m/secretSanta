from tkinter.ttk import Treeview, Style
from tkinter import Toplevel, font, Canvas, Button, Scrollbar, Frame, messagebox
from PIL import Image, ImageTk

from US1 import lista

def centrar_ventana(ventanacen, width, height):
    wtotal = ventanacen.winfo_screenwidth()
    htotal = ventanacen.winfo_screenheight()
    pwidth = round(wtotal / 2 - width / 2)
    pheight = round(htotal / 2 - height / 2)-40

    #  Se lo aplicamos a la geometría de la ventana
    ventanacen.geometry(str(width) + "x" + str(height) + "+" + str(pwidth) + "+" + str(pheight))
def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_image = image.resize((new_width, new_height))
    photo_resized = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=photo_resized, anchor="nw")
    canvas.image = photo_resized

fuentet = font.Font(family="Comic Sans MS", size=20)
ventana6 = Toplevel()
centrar_ventana(ventana6, 800, 400)
canvas = Canvas(ventana6, width=800, height=400)
canvas.pack(fill="both", expand=True)
image = Image.open('images/resul.png')
ventana6.bind('<Configure>', resize_image)
ventana6.update_idletasks()
ventana6.geometry(f"{ventana6.winfo_width()}x{ventana6.winfo_height()}")
btn_regresar_ventana_55 = Button(ventana6, text="Regresar", bg='#660504', fg='gray',
                   font=("Comic Sans MS", 14), bd=0, relief="flat")
btn_regresar_ventana_55.place(x=240, y=297)

def enviar_correos():
    print("Enviando correos a los participantes...")
    # Aquí agregar la lógica para enviar correos (algoritmo US7)
    flg = False  #bandera que indica si se pudieron enviar los correos

    if flg:
        messagebox.showinfo("Enviar Correos", "Los correos se han enviado correctamente a los participantes.")
    else:
        messagebox.showerror("Enviar Correos", "Los correos no pudieron ser enviados.")

btn_enviar = Button(ventana6, text="Enviar correos", bg='#126a4c', fg='lime green',
                   font=("Comic Sans MS", 11), bd=0, command=enviar_correos,relief="flat")
btn_enviar.place(x=455, y=302)
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


scrollbar_y = Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
scrollbar_x.pack(side="bottom", fill="x")
tree.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)