"""
libreria_funciones_proyecto1.py
--------------------------------
Librería externa con funciones de distintas áreas de aplicación.
El estudiante debe elegir UNA sola función relacionada con su
área de formación o trabajo y conectarla con widgets en Streamlit
(Ejercicio 3).

Cada función recibe parámetros simples (int, float o str) y
retorna un resultado que puede mostrarse fácilmente en pantalla.
"""


def calcular_interes_compuesto(capital: float, tasa_anual: float, anios: int) -> float:
    """
    Área: Finanzas / Analytics financiero
    Calcula el monto final de un capital invertido a interés compuesto.

    capital: monto inicial invertido
    tasa_anual: tasa de interés anual en porcentaje (ej. 5 para 5%)
    anios: número de años de la inversión
    """
    tasa_decimal = tasa_anual / 100
    monto_final = capital * (1 + tasa_decimal) ** anios
    return round(monto_final, 2)


def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """
    Área: Salud
    Calcula el Índice de Masa Corporal (IMC).

    peso_kg: peso de la persona en kilogramos
    altura_m: altura de la persona en metros
    """
    if altura_m <= 0:
        raise ValueError("La altura debe ser mayor a 0")
    imc = peso_kg / (altura_m ** 2)
    return round(imc, 2)


def calcular_promedio_notas(notas: list) -> float:
    """
    Área: Educación
    Calcula el promedio de una lista de notas/calificaciones.

    notas: lista de valores numéricos (ej. [12, 15, 18, 14])
    """
    if len(notas) == 0:
        return 0.0
    return round(sum(notas) / len(notas), 2)


def calcular_descuento(precio: float, porcentaje_descuento: float) -> float:
    """
    Área: Ventas / Marketing / Retail
    Calcula el precio final de un producto luego de aplicar un descuento.

    precio: precio original del producto
    porcentaje_descuento: porcentaje de descuento a aplicar (ej. 20 para 20%)
    """
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return round(precio_final, 2)


def convertir_temperatura(valor: float, unidad_origen: str) -> float:
    """
    Área: Ingeniería / Ciencias
    Convierte una temperatura entre Celsius y Fahrenheit.

    valor: valor numérico de la temperatura
    unidad_origen: 'Celsius' o 'Fahrenheit'
    """
    if unidad_origen == "Celsius":
        return round((valor * 9 / 5) + 32, 2)  # resultado en Fahrenheit
    elif unidad_origen == "Fahrenheit":
        return round((valor - 32) * 5 / 9, 2)  # resultado en Celsius
    else:
        raise ValueError("Unidad de origen no reconocida")
