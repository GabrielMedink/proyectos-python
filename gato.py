import tkinter as tk
from tkinter import messagebox

# Función para verificar si un jugador ha ganado
def verificar_ganador(jugador):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

# Función para manejar el clic en un botón de la cuadrícula
def clic_boton(fila, columna):
    global turno_actual, ganador
    
    if tablero[fila][columna] == "" and not ganador:
        tablero[fila][columna] = turno_actual
        if turno_actual == "X":
            turno_actual = "O"
        else:
            turno_actual = "X"
        
        # Actualizar el contenido del botón
        botones[fila][columna].config(text=tablero[fila][columna])
        
        # Verificar si hay un ganador
        if verificar_ganador("X"):
            ganador = "X"
            messagebox.showinfo("¡Fin del juego!", "¡Ha ganado el jugador X!")
            reiniciar_juego()
        elif verificar_ganador("O"):
            ganador = "O"
            messagebox.showinfo("¡Fin del juego!", "¡Ha ganado el jugador O!")
            reiniciar_juego()
        elif "" not in [casilla for fila in tablero for casilla in fila]:
            messagebox.showinfo("¡Fin del juego!", "¡El juego ha terminado en empate!")
            reiniciar_juego()

# Función para reiniciar el juego
def reiniciar_juego():
    global turno_actual, ganador
    turno_actual = "X"
    ganador = ""
    for i in range(3):
        for j in range(3):
            tablero[i][j] = ""
            botones[i][j].config(text="")

# Configuración inicial
turno_actual = "X"
ganador = ""
tablero = [["" for _ in range(3)] for _ in range(3)]

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear botones
botones = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        botones[i][j] = tk.Button(ventana, text="", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda fila=i, columna=j: clic_boton(fila, columna))
        botones[i][j].grid(row=i, column=j)

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", font=("Helvetica", 14), command=reiniciar_juego)
boton_reiniciar.grid(row=3, column=0, columnspan=3)

# Iniciar bucle de eventos
ventana.mainloop()
