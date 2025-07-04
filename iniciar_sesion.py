import tkinter as tk  # Importa la biblioteca Tkinter con un alias para crear interfaces gráficas
from tkinter import messagebox   #Importa la función messagebox para mostrar mensajes emergentes

# Función para iniciar sesión
def iniciar_sesion():
    usuario = entrada_usuario.get()  # Obtiene el texto ingresado en el campo de usuario
    contrasena = entrada_contrasena.get()  # Obtiene el texto ingresado en el campo de contraseña
 
# Crea la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Inicio de sesión")  # Establece el título de la ventana
ventana.geometry("300x200")  # Define el tamaño de la ventana en píxeles

# Crea un marco  dentro de la ventana principal
frame = tk.Frame(ventana)
frame.pack(pady=20)  # Coloca el frame con un espacio superior

# Agrega una etiqueta para "Nombre de usuario"
tk.Label(frame, text="Nombre de usuario:").grid(row=0, column=0, sticky="w")

# Campo de entrada para escribir el nombre de usuario
entrada_usuario = tk.Entry(frame)
entrada_usuario.grid(row=0, column=1)  # Posiciona el campo en la misma fila, columna 1

# Agrega una etiqueta para "Contraseña"
tk.Label(frame, text="Contraseña:").grid(row=1, column=0, sticky="w")

# Campo de entrada para escribir la contraseña (oculta los caracteres)
entrada_contrasena = tk.Entry(frame, show="*")
entrada_contrasena.grid(row=1, column=1)  # Posiciona el campo junto a la etiqueta

# Botón para iniciar sesión, vinculado a la función iniciar_sesion
boton_login = tk.Button(frame, text="Ingresar", command=iniciar_sesion)
boton_login.grid(row=2, columnspan=2, pady=10)  # Ocupa las dos columnas y añade espacio abajo

# Inicia el bucle principal de la aplicación (la ventana se mantiene abierta)
ventana.mainloop()
