#Dia/Hora de inicio:Jueves, 24 de mayo del 2024 / 08:02PM
#Dia/Hora de finalizacion: Viernes, 25 de mayo del 2024 / 12:27AM
"""
Ejercicio:
Título: Generador de contraseñas seguras
Descripción: Desarrolla una aplicación que genere contraseñas seguras y únicas con opciones personalizables.
Requisitos:
Permitir al usuario escoger que tipo de configuración para contraseña desea (letras mayúsculas y minúsculas, números, símbolos)
Permitir al usuario personalizar la longitud de la contraseña
Mostrar al usuario la contraseña generada
Datos:
Seguridad:
Las contraseñas generadas deben ser seguras y difíciles de adivinar.
No se debe almacenar la contraseña en el código fuente.
Usabilidad:
La aplicación debe ser fácil de usar e intuitiva.
Se debe proporcionar una interfaz clara y concisa.
"""

import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    if not any([incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos]):
        messagebox.showerror("Error", "Por favor, selecciona al menos una opción para generar la contraseña.")
        return''
        """por si queremos generar una contraseña sin haber elegido una de las opciones disponibles,
        lo vi mas comodo trabajar de este modo y no que me genere una contraseña aleatoria de minusculas y numeros
        para mayor seguridad"""

    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def generar_contraseña_click():
    longitud_str = longitud_entry.get()
    if not longitud_str.isdigit():#por si no metemos numeros en el campo de longitud de contraseñas, aumque dejemos el espacio vacio saldra este mensaje
        messagebox.showerror("Error", "Por favor, ingresa solo números en el campo de la longitud.")
        return

    longitud = int(longitud_str)
    incluir_mayusculas = mayusculas_var.get()
    incluir_minusculas = minusculas_var.get()
    incluir_numeros = numeros_var.get()
    incluir_simbolos = simbolos_var.get()

    contraseña_generada = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    if contraseña_generada:
        contraseña_label.config(text="tu contraseña es: \n" + contraseña_generada)
        copiar_button.pack(**padding)  #Mostrar el botón de copiar contraseña despues de generar la contraseña 

    else:
        contraseña_label.config(text="") #cuando no seleccionaba ninguna de las opciones a incluir, aparte del mensaje de error, se me imprimia igual 
             #"tu contraseña es:" y me aparecia el campo de la contraseña vacio, con esto evito que eso se imprima cuando no se genere una contraseña

#crear un boton para copiar la contraseña generada, podria sernos de utilidad
def copiar_contraseña():
    contraseña = contraseña_label.cget("text").split("\n")[-1]
    ventana.clipboard_clear()
    ventana.clipboard_append(contraseña)
    messagebox.showinfo("Copiar Contraseña", "Contraseña copiada al portapapeles")


# Crear ventana principal:
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("450x500")  # Establece un tamaño para la ventana


# Configurar padding y tamaño de fuente:
padding = {'padx': 6, 'pady': 6}
font_style = ('Arial', 12, "normal")


# Crear estilo para los checkbuttons
style = ttk.Style()
style.configure("TCheckbutton", font=font_style, foreground="red")


# Crear un Frame principal para centrar todos los widgets
main_frame = ttk.Frame(ventana)
main_frame.pack(expand=True, fill=tk.BOTH)

# Espaciado superior, esto lo cree con una simple finalidad, dejar todo lo mas centrado posible, quizas haya otras formas mejores de hacerlo
top_spacer = ttk.Label(main_frame, text="", font=font_style)
top_spacer.pack(pady=20)

# Crear widgets dentro del Frame principal:
longitud_label = ttk.Label(main_frame, text="Longitud de la contraseña:", font=font_style)
longitud_label.pack(**padding)
longitud_entry = ttk.Entry(main_frame, font=font_style)
longitud_entry.pack(**padding)

# Crear un frame para los checkbuttons dentro del main_frame
checks_frame = ttk.Frame(main_frame)
checks_frame.pack(**padding)

mayusculas_var = tk.BooleanVar()
mayusculas_check = ttk.Checkbutton(checks_frame, text="Incluir mayúsculas", variable=mayusculas_var, style="TCheckbutton")
mayusculas_check.grid(row=0, column=0, sticky=tk.W, **padding)

minusculas_var = tk.BooleanVar()
minusculas_check = ttk.Checkbutton(checks_frame, text="Incluir minúsculas", variable=minusculas_var, style="TCheckbutton")
minusculas_check.grid(row=1, column=0, sticky=tk.W, **padding)

numeros_var = tk.BooleanVar()
numeros_check = ttk.Checkbutton(checks_frame, text="Incluir números", variable=numeros_var, style="TCheckbutton")
numeros_check.grid(row=2, column=0, sticky=tk.W, **padding)

simbolos_var = tk.BooleanVar()
simbolos_check = ttk.Checkbutton(checks_frame, text="Incluir símbolos", variable=simbolos_var, style="TCheckbutton")
simbolos_check.grid(row=3, column=0, sticky=tk.W, **padding)

generar_button = ttk.Button(main_frame, text="Generar Contraseña", command=generar_contraseña_click)
generar_button.pack(**padding)


contraseña_label = ttk.Label(main_frame, text="", font=font_style)
contraseña_label.pack(**padding)

copiar_button = ttk.Button(main_frame, text="Copiar Contraseña", command=copiar_contraseña)

# Espaciado inferior, lo mismo que con el espacio superior
bottom_spacer = ttk.Label(main_frame, text="", font=font_style)
bottom_spacer.pack(pady=20)


# Ejecutar la ventana principal
ventana.mainloop()