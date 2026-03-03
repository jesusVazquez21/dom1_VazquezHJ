import hashlib

def simular_sha256(texto):
    # Convertimos el texto a bytes y aplicamos el algoritmo
    resultado = hashlib.sha256(texto.encode())
    # Retornamos el hash en formato hexadecimal (64 caracteres)
    return resultado.hexdigest()

def minar_bloque(datos_transaccion, curp, btc, usd, dificultad):
    """
    Intenta encontrar un hash que comience con 'n' ceros (dificultad).
    """
    nonce = 0
    objetivo = "0" * dificultad
    hash_curp = simular_sha256(curp)
    
    # 2. Preparar la cadena de datos fija del bloque
    
    datos_fijos = f"Hash CURP: {hash_curp} | BTC: ${btc} | USD: ${usd}"
    print(f"--- Iniciando minería con dificultad: {dificultad} ---")
    
    while True:
        # Combinamos los datos con el nonce actual
        contenido = f"{datos_transaccion}{nonce}"
        hash_intentado = simular_sha256(contenido)
        
        # Mostramos los primeros intentos para ver el cambio
        if nonce < 6:
            print(f"Nonce: {nonce} -> Hash: {hash_intentado}")
        elif nonce == 6:
            print("ciclo terminado......")

        # Si el hash empieza con los ceros requeridos, ¡ganamos!
        if hash_intentado.startswith(objetivo):
            print(f"\n¡BLOQUE MINADO!")
            print(f"Nonce final: {nonce}")
            print(f"Hash válido: {hash_intentado}")
            return hash_intentado
        
        nonce += 1

# --- PRUEBA DEL SIMULADOR ---
# --- CONFIGURACIÓN Y EJECUCIÓN ---

# Datos del alumno (Cambia esto por tu nombre real)
mensaje = "Soy el alumno Jesus Vazquez Hernandez del grupo 5° A"
mi_curp = "PESJ900101HDFRRN01" 

# Valores fijos proporcionados
valor_bitcoin = "1,639,278.45"
valor_dolar = "17.58"

# 1. Ver un hash simple
print(f"Hash inicial: '{mensaje}':\n{simular_sha256(mensaje)}\n")
print(f"Hash inicial: '{mi_curp}':\n{simular_sha256(mi_curp)}\n")
print(f"Hash inicial: '{valor_bitcoin}':\n{simular_sha256(valor_bitcoin)}\n")
print(f"Hash inicial: '{valor_dolar}':\n{simular_sha256(valor_dolar)}\n")

# Iniciar el proceso
minar_bloque(mensaje, mi_curp, valor_bitcoin, valor_dolar, dificultad=6)

