import US1, US2, US5, US6

def continuar_interfaz():
    """Muestra ventana 5 y oculta ventana 2."""
    US5.ventana5.deiconify()
    US2.ventana2.withdraw()  # Oculta ventana 2

def continuar():
    """Valida la cantidad de participantes y muestra la ventana 2."""
    if US1.lista.contar_participantes() >= 3:
        US1.lbl_mensaje.config(text="Avanzando a la siguiente pantalla", fg="blue")
        US2.ventana2.deiconify()  # Muestra ventana 2
        US1.ventana1.withdraw()  # Oculta ventana 1
    else:
        US1.lbl_mensaje.config(text="Faltan participantes por registrar", fg="red")

def print_hi(name):
    """Configura los botones y la visibilidad inicial de las ventanas."""
    US1.btn_continuar.config(text="Continuar", command=continuar)
    US2.btn_continuar2.config(text="Continuar", command=continuar_interfaz)

    # Oculta todas las ventanas secundarias al iniciar
    US2.ventana2.withdraw()
    US5.ventana5.withdraw()
    US6.ventana6.withdraw()  # Oculta ventana 6

    print(f'Hi, {name}')
    US1.ventana1.mainloop()  # Inicia el bucle principal de ventana 1

if __name__ == '__main__':
    # Oculta ventanas de otros módulos por seguridad
    US6.ventana6.withdraw()
    print_hi('PyCharm')
