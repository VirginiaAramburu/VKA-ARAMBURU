import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

def guardar_datos():
    datos = [entry.get() for entry in entries]
    ocupacion = occupation_var.get()
    estado = state_var.get()
    acciones = [action for action, var in zip(actions, action_vars) if var.get()]

    # CAMBIO: validaciones básicas
    if any(not dato.strip() for dato in datos):
        messagebox.showwarning("Validación", "Por favor completa todos los campos personales.")
        return
    if estado == "Selecciona un estado" or not ocupacion:
        messagebox.showwarning("Validación", "Por favor selecciona un estado y una ocupación.")
        return

    fila = datos + [ocupacion, estado, ", ".join(acciones)]

    archivo_csv = "datos_personales.csv"  # CAMBIO: nombre del archivo como solicitaste
    archivo_existe = os.path.isfile(archivo_csv)

    try:
        with open(archivo_csv, mode="a", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            if not archivo_existe:
                encabezados = ["Nombre", "A. Paterno", "A. Materno", "Correo", "Móvil", "Ocupación", "Estado", "Acciones"]
                writer.writerow(encabezados)
            writer.writerow(fila)
        messagebox.showinfo("Éxito", "Datos guardados correctamente en 'datos_personales.csv'")
        limpiar_formulario()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron guardar los datos:\n{e}")

def limpiar_formulario():
    for entry in entries:
        entry.delete(0, tk.END)
    occupation_var.set("Estudiante")  # CAMBIO: valor por defecto
    state_combo.set("Selecciona un estado")
    for var in action_vars:
        var.set(False)

# Crear ventana principal
root = tk.Tk()
root.title("Muestra Widgets")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Datos personales
datos_frame = ttk.LabelFrame(main_frame, text="Datos Personales", padding="10")
datos_frame.grid(row=0, column=0, columnspan=2, sticky=tk.W)

labels = ["Nombre:", "A. Paterno:", "A. Materno:", "Correo:", "Móvil:"]
entries = []
for i, label in enumerate(labels):
    ttk.Label(datos_frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=2)
    entry = ttk.Entry(datos_frame, width=30)
    entry.grid(row=i, column=1, pady=2)
    entries.append(entry)

# Ocupación
occupation_var = tk.StringVar()
occupation_var.set("Estudiante")  # CAMBIO
occupations = ["Estudiante", "Empleado", "Desempleado"]
occupation_frame = ttk.LabelFrame(main_frame, text="Ocupación", padding="10")
occupation_frame.grid(row=0, column=2, rowspan=3, sticky=tk.NW)
for occupation in occupations:
    ttk.Radiobutton(occupation_frame, text=occupation, variable=occupation_var, value=occupation).pack(anchor=tk.W)

# Estados
states = [
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua",
    "CDMX", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo",
    "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro",
    "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
    "Veracruz", "Yucatán", "Zacatecas"
]
state_var = tk.StringVar()
state_combo = ttk.Combobox(main_frame, textvariable=state_var, values=states, state="readonly", width=27)
state_combo.grid(row=6, column=2, pady=5)
state_combo.set("Selecciona un estado")

# Acciones
acciones_frame = ttk.LabelFrame(main_frame, text="Acciones", padding="10")
acciones_frame.grid(row=6, column=0, columnspan=2, sticky=tk.W)

actions = ["Leer", "Música", "Videojuegos"]
action_vars = []
for action in actions:
    var = tk.BooleanVar()
    ttk.Checkbutton(acciones_frame, text=action, variable=var).pack(side=tk.LEFT, padx=5)
    action_vars.append(var)

# Botones
button_frame = ttk.Frame(root, padding="10")
button_frame.grid(row=1, column=0, sticky=tk.W)
ttk.Button(button_frame, text="Guardar", command=guardar_datos).grid(row=0, column=0, padx=(0, 15))
ttk.Button(button_frame, text="Cancelar", command=root.quit).grid(row=0, column=1)

# Ejecutar
root.mainloop()
