import US1, US2, US5
def continuar_interfaz():
    US5.ventana5.deiconify()
    US2.ventana2.iconify()
def continuar():
    if US1.lista.contar_participantes() >= 3:
        US1.lbl_mensaje.config(text="Avanzando a la siguiente pantalla", fg="blue")
        US2.ventana2.deiconify()
        US1.ventana1.iconify()
        # Aquí se puede implementar la lógica para cambiar a la siguiente pantalla
    else:
        US1.lbl_mensaje.config(text="Faltan participantes por registrar", fg="red")
def print_hi(name):
    US1.btn_continuar.config(text="Continuar", command=continuar)
    US2.btn_continuar2.config(text="Continuar", command=continuar_interfaz)
    print(f'Hi, {name}')
    US1.ventana1.mainloop()

if __name__ == '__main__':
    print_hi('PyCharm')

