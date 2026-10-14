
import tkinter as tk

# ==========================================
# VENTANA PRINCIPAL
# ==========================================

root = tk.Tk()
root.title("Mapa Conceptual: Circuitería Alternativa de E/S")
root.geometry("1200x720")
root.configure(bg="white")
root.resizable(True, True)

# ==========================================
# LIENZO
# ==========================================

canvas = tk.Canvas(
    root,
    width=1200,
    height=720,
    bg="white",
    highlightthickness=0
)

canvas.pack(fill=tk.BOTH, expand=True)

# ==========================================
# COLORES Y FUENTES
# ==========================================

fuente = ("Arial", 10, "bold")
fuente_titulo = ("Arial", 19, "bold")

color_linea = "#37474F"
color_borde = "#0B2545"

azul_principal = "#D0E1FD"
azul_secundario = "#E1F5FE"
verde = "#F1F8E9"
amarillo = "#FFFDE7"

# ==========================================
# FUNCION PARA CREAR CUADROS
# ==========================================

def crear_cuadro(x, y, texto, ancho, alto, color):

    canvas.create_rectangle(
        x - ancho / 2,
        y - alto / 2,
        x + ancho / 2,
        y + alto / 2,
        fill=color,
        outline=color_borde,
        width=2
    )

    canvas.create_text(
        x,
        y,
        text=texto,
        font=fuente,
        fill=color_linea,
        justify=tk.CENTER,
        width=ancho - 12
    )

# ==========================================
# FUNCION PARA CREAR FLECHAS
# ==========================================

def crear_flecha(x1, y1, x2, y2):

    canvas.create_line(
        x1, y1, x2, y2,
        fill=color_linea,
        width=2,
        arrow=tk.LAST
    )

# ==========================================
# TITULO
# ==========================================

canvas.create_text(
    600, 28,
    text="Mapa Conceptual: Circuitería Alternativa de E/S",
    font=fuente_titulo,
    fill=color_borde
)

# ==========================================
# POSICIONES
# ==========================================

principal_x = 600
principal_y = 100

izquierda_x = 200
centro_x = 600
derecha_x = 1000

nivel1_y = 265
nivel2_y = 490

memory_x = 890
port_x = 1090
direccion_y = 555

# ==========================================
# MEDIDAS
# ==========================================

principal_ancho = 340
principal_alto = 65

nivel1_ancho = 260
nivel1_alto = 60

nivel2_ancho = 280
nivel2_alto = 115

direccion_ancho = 190
direccion_alto = 100

# ==========================================
# CUADRO PRINCIPAL
# ==========================================

crear_cuadro(
    principal_x, principal_y,
    "Circuitería Alternativa\nde E/S",
    principal_ancho, principal_alto,
    azul_principal
)

# ==========================================
# SEGUNDO NIVEL
# ==========================================

crear_cuadro(
    izquierda_x, nivel1_y,
    "Acceso Directo\na Memoria (DMA)",
    nivel1_ancho, nivel1_alto,
    azul_secundario
)

crear_cuadro(
    centro_x, nivel1_y,
    "Canales de E/S",
    nivel1_ancho, nivel1_alto,
    azul_secundario
)

crear_cuadro(
    derecha_x, nivel1_y,
    "Técnicas de\nDireccionamiento",
    nivel1_ancho, nivel1_alto,
    azul_secundario
)

# ==========================================
# TERCER NIVEL: DMA
# ==========================================

crear_cuadro(
    izquierda_x, nivel2_y,
    "Controlador DMAC\n"
    "• Libera ciclos de la CPU\n"
    "• Transfiere bloques\n"
    "• Mayor eficiencia en E/S",
    nivel2_ancho, nivel2_alto,
    verde
)

# ==========================================
# TERCER NIVEL: CANALES DE E/S
# ==========================================

crear_cuadro(
    centro_x, nivel2_y,
    "Procesador dedicado\n"
    "• Ejecuta programas de canal\n"
    "• Alta autonomía\n"
    "• Sistemas grandes (Mainframe)\n"
    "• Soporte múltiple de E/S",
    nivel2_ancho, nivel2_alto,
    verde
)

# ==========================================
# TERCER NIVEL: MEMORY-MAPPED I/O
# ==========================================

crear_cuadro(
    memory_x, direccion_y,
    "Memory-Mapped I/O\n"
    "• Memoria compartida\n"
    "• Direcciones unificadas",
    direccion_ancho, direccion_alto,
    amarillo
)

# ==========================================
# TERCER NIVEL: PORT-MAPPED I/O
# ==========================================

crear_cuadro(
    port_x, direccion_y,
    "Port-Mapped I/O\n"
    "• Puertos aislados\n"
    "• Instrucciones específicas",
    direccion_ancho, direccion_alto,
    amarillo
)

# ==========================================
# FLECHAS DESDE EL CUADRO PRINCIPAL
# ==========================================

crear_flecha(
    principal_x - 90, principal_y + principal_alto / 2,
    izquierda_x, nivel1_y - nivel1_alto / 2
)

crear_flecha(
    principal_x, principal_y + principal_alto / 2,
    centro_x, nivel1_y - nivel1_alto / 2
)

crear_flecha(
    principal_x + 90, principal_y + principal_alto / 2,
    derecha_x, nivel1_y - nivel1_alto / 2
)

# ==========================================
# FLECHAS HACIA DMA Y CANALES
# ==========================================

crear_flecha(
    izquierda_x, nivel1_y + nivel1_alto / 2,
    izquierda_x, nivel2_y - nivel2_alto / 2
)

crear_flecha(
    centro_x, nivel1_y + nivel1_alto / 2,
    centro_x, nivel2_y - nivel2_alto / 2
)

# ==========================================
# FLECHAS HACIA LAS TECNICAS
# ==========================================

crear_flecha(
    derecha_x - 45, nivel1_y + nivel1_alto / 2,
    memory_x, direccion_y - direccion_alto / 2
)

crear_flecha(
    derecha_x + 45, nivel1_y + nivel1_alto / 2,
    port_x, direccion_y - direccion_alto / 2
)

# ==========================================
# INICIAR PROGRAMA
# ==========================================

root.mainloop()
