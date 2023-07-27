import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())
        resultado_label.config(text="Resultado: " + str(resultado))
    except:
        resultado_label.config(text="Error al calcular")

def eliminar_caracter():
    entrada.delete(len(entrada.get()) - 1, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear una caja de entrada para ingresar la operación
entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear botones numéricos y de operaciones
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "DEL", "+"  
]

fila = 1
columna = 0

for boton in botones:
    if boton == "DEL":
        tk.Button(ventana, text=boton, padx=20, pady=20, command=eliminar_caracter).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20, command=lambda b=boton: entrada.insert(tk.END, b)).grid(row=fila, column=columna)
    
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Crear botón para calcular el resultado
tk.Button(ventana, text="Calcular", padx=20, pady=20, command=calcular).grid(row=5, column=0, columnspan=4)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.grid(row=6, column=0, columnspan=4)

# Ejecutar el bucle principal de la interfaz
ventana.mainloop()
