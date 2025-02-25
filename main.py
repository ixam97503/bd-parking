import tkinter as tk
import random
import pandas as pd
from tkinter import messagebox

# Manejo de directorios
from pathlib import Path
import os

# Lista de nombres de usuarios y matrículas aleatorias
usuarios = [
    {"nombre": "", "matricula": ""},
    {"nombre": "", "matricula": ""},
    {"nombre": "", "matricula": ""},
    {"nombre": "", "matricula": ""},
    {"nombre": "", "matricula": ""},
    {"nombre": "", "matricula": ""}
]

# Espacios de estacionamiento
espacios = ["Disponible"] * 6

# Función para asignar un puesto de estacionamiento aleatoriamente
def asignar_puesto(matricula, nombre):
    global espacios, usuarios
    indice_disponible = [i for i, espacio in enumerate(espacios) if espacio == "Disponible"]
    if indice_disponible:
        indice = random.choice(indice_disponible)
        espacios[indice] = "Ocupado"
        usuarios[indice] = {"nombre": nombre, "matricula": matricula}
        return True
    else:
        return False

# Función para liberar un puesto de estacionamiento
def liberar_puesto(indice):
    global espacios, usuarios
    espacios[indice] = "Disponible"
    usuarios[indice] = {"nombre": "", "matricula": ""}
    actualizar_interfaz()

# Función para actualizar la interfaz
def actualizar_interfaz():
    for i, espacio in enumerate(espacios):
        if espacio == "Ocupado":
            usuario = usuarios[i]
            texto_boton = f'{usuario["nombre"]} - {usuario["matricula"]}'
            botones[i].config(text=texto_boton, bg="red", command=lambda i=i: liberar_puesto(i))
        else:
            botones[i].config(text=str(i + 1), bg="blue", fg="white", command=None, borderwidth=3, width=15)

    mensaje_label.config(text=mensaje)

def estacionar():
    ruta = Path(os.getcwd(), 'base.xlsx')
    global mensaje
    matricula = matricula_entry.get()
    nombre = nombre_entry.get()

    if matricula and nombre:
        asignado = asignar_puesto(matricula, nombre)
        if asignado:
            mensaje = f'¡Bienvenido, {nombre}! Su puesto de estacionamiento ha sido asignado.'
            messagebox.showinfo("Éxito", "Información guardada correctamente.")
            messagebox.showinfo("Plaza ocupada", mensaje)
        else:
            mensaje = 'Lo sentimos, no hay espacios disponibles en este momento.'
        actualizar_interfaz()
    else:
        messagebox.showwarning("Datos incompletos", "Por favor ingrese la matrícula y el nombre del usuario.")

    # Si todos los campos son válidos, guardar la información del inventario
    infoBaseDeInventario = {
        'Matricula': [matricula],
        'Nombre': [nombre]
    }

    CrearBaseInventario = pd.DataFrame(infoBaseDeInventario, index=[0])

    try:
        existing_data = pd.read_excel(ruta, sheet_name='Base')
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    updated_data = pd.concat([existing_data, CrearBaseInventario], ignore_index=True)

    with pd.ExcelWriter(ruta, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        updated_data.to_excel(writer, sheet_name='Base', index=False)

    # Recetear cada uno de los campos
    matricula_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)



# Configuración de la interfaz

root = tk.Tk()
root.title("Parqueadero")
root.geometry("1920x1080")
root.configure(bg="#4D4D4D")
root.iconbitmap('parqueadero.ico')

image = tk.PhotoImage(file="parqueadero1.png")
image_label = tk.Label(image=image, bg="#4D4D4D")
image_label.place(x=5, y=10)

# Etiquetas
titulo_label = tk.Label(root, text="Parqueadero", font=("Arial", 35), bg="#4D4D4D", fg="yellow")
titulo_label.place(relx=0.5, rely=0.1, anchor="center")

mensaje = ""
mensaje_label = tk.Label(root, text=mensaje, bg="#4D4D4D")
mensaje_label.place(relx=0.5, rely=0.2, anchor="center")

# Entradas de texto
matricula_label = tk.Label(root, text="Matrícula:", font=("Arial", 14), bg="#4D4D4D", fg="white")
matricula_label.place(relx=0.35, rely=0.3, anchor="center")
matricula_entry = tk.Entry(root)
matricula_entry.place(relx=0.45, rely=0.3, anchor="center")

nombre_label = tk.Label(root, text="Nombre:", font=("Arial", 14), bg="#4D4D4D", fg="white")
nombre_label.place(relx=0.55, rely=0.3, anchor="center")
nombre_entry = tk.Entry(root)
nombre_entry.place(relx=0.65, rely=0.3, anchor="center")

# Botones de espacios de estacionamiento
botones = []
for i in range(6):
    boton = tk.Button(root, text=str(i + 1), bg="blue", width=6, height=3, font=("Arial", 14), borderwidth=5)
    boton.place(x=(i * 150) + 360, y=400)
    botones.append(boton)

# Botón de estacionar
estacionar_button = tk.Button(root, text="Estacionar", command=estacionar, font=("Arial", 14), bg="blue", fg="white", relief=tk.GROOVE, borderwidth=3, width=10)
estacionar_button.place(x=700, y=600, anchor="center")

# Mostrar la interfaz
actualizar_interfaz()  # Llamar después de configurar la interfaz
root.mainloop()
