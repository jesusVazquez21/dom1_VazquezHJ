import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. MÓDULO LÓGICO (Fácil de probar)
# ==========================================
def es_mayor_de_edad(edad_texto):
    try:
        edad = int(edad_texto)
        if edad < 0 or edad > 120:
            return None, "Edad no realista"
        
        # Retorna True si es mayor o igual a 18
        return edad >= 18, None
        
    except ValueError:
        return None, "Ingresa solo números enteros"

# ==========================================
# 2. INTERFAZ Y CONEXIÓN (Integración)
# ==========================================
def verificar():
    # Obtener el texto que escribió el usuario
    texto = entrada_edad.get()
    
    # Llamar a la lógica
    autorizado, error = es_mayor_de_edad(texto)
    
    if error:
        # Si escribió letras o números raros
        etiqueta_resultado.config(text="Error", fg="black")
        messagebox.showwarning("Atención", error)
    elif autorizado:
        # Si tiene 18 o más
        etiqueta_resultado.config(text="✅ VENTA AUTORIZADA", fg="green")
    else:
        # Si tiene menos de 18
        etiqueta_resultado.config(text="❌ VENTA DENEGADA", fg="red")

# ==========================================
# 3. DISEÑO DEL SISTEMA (Ventana)
# ==========================================
ventana = tk.Tk()
ventana.title("Taquilla - Cine")
ventana.geometry("400x200")
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="Película Clasificación 'C'", font=("Arial", 12, "bold")).pack()
tk.Label(ventana, text="Ingresa la edad del cliente:").pack(pady=10)

entrada_edad = tk.Entry(ventana, font=("Arial", 14), width=10, justify="center")
entrada_edad.pack()

tk.Button(ventana, text="Verificar", command=verificar, bg="blue", fg="white").pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
etiqueta_resultado.pack()

# Iniciar programa
ventana.mainloop()