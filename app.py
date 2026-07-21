"""
app.py
------
Proyecto Aplicado en Streamlit - Fundamentos de Programación
Especialización en Python for Analytics - Módulo 1: Python Fundamentals

Autor: [ESCRIBE AQUÍ TU NOMBRE COMPLETO]
Fecha: [ESCRIBE AQUÍ LA FECHA DE ENTREGA]
"""

import streamlit as st
import pandas as pd
import numpy as np

from libreria_funciones_proyecto1 import (
    calcular_interes_compuesto,
    calcular_imc,
    calcular_promedio_notas,
    calcular_descuento,
    convertir_temperatura,
)
from libreria_clases_proyecto1 import GestorProductos, GestorClientes, GestorTareas

# -----------------------------------------------------------------------
# Configuración general de la página
# -----------------------------------------------------------------------
st.set_page_config(page_title="Proyecto 1 - Python Fundamentals", page_icon="🐍", layout="centered")

# -----------------------------------------------------------------------
# Inicialización de session_state (se conserva la información entre
# interacciones del usuario, tal como recomienda la guía del proyecto)
# -----------------------------------------------------------------------
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []  # Ejercicio 1: lista de movimientos

if "registros_productos" not in st.session_state:
    st.session_state.registros_productos = []  # Ejercicio 2: lista de arrays

if "historial_funcion" not in st.session_state:
    st.session_state.historial_funcion = []  # Ejercicio 3: historial de resultados

if "gestor_crud" not in st.session_state:
    st.session_state.gestor_crud = None  # Ejercicio 4: instancia de la clase elegida


# -----------------------------------------------------------------------
# Menú lateral de navegación
# -----------------------------------------------------------------------
seccion = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"],
)


# =========================================================================
# 1. HOME
# =========================================================================
if seccion == "Home":
    st.title("Proyecto 1 - Fundamentos de Programación en Python")
    st.subheader("Especialización en Python for Analytics - Módulo 1")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 👤 Datos del estudiante")
        st.write("**Nombre:** [Tu nombre completo]")
        st.write("**Módulo:** Python Fundamentals")
        st.write("**Año:** 2026")
    with col2:
        st.markdown("### 📌 Descripción del proyecto")
        st.write(
            "Esta aplicación integra los conceptos fundamentales del Módulo 1: "
            "variables, estructuras de datos, control de flujo, funciones, "
            "programación funcional y programación orientada a objetos (POO), "
            "a través de 4 ejercicios interactivos desarrollados en Streamlit."
        )

    st.markdown("### 🛠️ Tecnologías utilizadas")
    st.markdown(
        """
        - **Python 3**
        - **Streamlit** (interfaz interactiva)
        - **Pandas** (manejo de DataFrames)
        - **NumPy** (arreglos numéricos)
        - **Git / GitHub** (control de versiones)
        - **Streamlit Cloud** (despliegue de la aplicación)
        """
    )

    st.markdown("### 🧭 Contenido de la aplicación")
    st.markdown(
        """
        1. **Ejercicio 1** – Flujo de caja con listas
        2. **Ejercicio 2** – Registro con NumPy, arrays y DataFrame
        3. **Ejercicio 3** – Uso de funciones desde una librería externa
        4. **Ejercicio 4** – Uso de clases desde una librería externa con CRUD
        """
    )


# =========================================================================
# 2. EJERCICIO 1 - Flujo de caja con listas
# =========================================================================
elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1 - Flujo de caja con listas")
    st.markdown(
        """
        En este ejercicio se registran movimientos financieros (ingresos y gastos)
        en una **lista** almacenada en `st.session_state`. Con esa lista se calcula
        el total de ingresos, el total de gastos y el saldo final del flujo de caja.
        """
    )

    st.markdown("### ➕ Registrar movimiento")
    col1, col2, col3 = st.columns(3)
    with col1:
        concepto = st.text_input("Concepto", placeholder="Ej. Venta de producto")
    with col2:
        tipo_movimiento = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    with col3:
        valor = st.number_input("Valor (S/.)", min_value=0.0, step=10.0)

    if st.button("Agregar movimiento"):
        if concepto.strip() == "" or valor <= 0:
            st.error("Debes ingresar un concepto válido y un valor mayor a 0.")
        else:
            st.session_state.movimientos.append(
                {"Concepto": concepto, "Tipo": tipo_movimiento, "Valor": valor}
            )
            st.success(f"Movimiento '{concepto}' agregado correctamente.")

    st.markdown("### 📋 Movimientos registrados")
    if len(st.session_state.movimientos) > 0:
        df_movimientos = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_movimientos, use_container_width=True)

        total_ingresos = df_movimientos.loc[df_movimientos["Tipo"] == "Ingreso", "Valor"].sum()
        total_gastos = df_movimientos.loc[df_movimientos["Tipo"] == "Gasto", "Valor"].sum()
        saldo_final = total_ingresos - total_gastos

        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Total ingresos", f"S/. {total_ingresos:,.2f}")
        col_b.metric("Total gastos", f"S/. {total_gastos:,.2f}")
        col_c.metric("Saldo final", f"S/. {saldo_final:,.2f}")

        if saldo_final >= 0:
            st.success("✅ El flujo de caja está A FAVOR.")
        else:
            st.error("⚠️ El flujo de caja está EN CONTRA.")
    else:
        st.info("Aún no hay movimientos registrados. Agrega el primero arriba 👆")


# =========================================================================
# 3. EJERCICIO 2 - Registro con NumPy, arrays y DataFrame
# =========================================================================
elif seccion == "Ejercicio 2":
    st.title("Ejercicio 2 - Registro con NumPy, arrays y DataFrame")
    st.markdown(
        """
        En este ejercicio se registran productos vendidos. Cada registro se
        almacena primero como un **array de NumPy** y luego se convierte en un
        **DataFrame de Pandas** que se muestra actualizado en pantalla.
        """
    )

    st.markdown("### 📝 Formulario de registro de productos")
    col1, col2 = st.columns(2)
    with col1:
        nombre_producto = st.text_input("Nombre del producto", placeholder="Ej. Laptop HP 15'")
        categoria = st.selectbox("Categoría", ["Tecnología", "Ropa", "Hogar", "Alimentos", "Otros"])
    with col2:
        precio = st.number_input("Precio unitario (S/.)", min_value=0.0, step=1.0)
        cantidad = st.number_input("Cantidad", min_value=0, step=1)

    if st.button("Agregar registro"):
        if nombre_producto.strip() == "" or precio <= 0 or cantidad <= 0:
            st.error("Completa todos los campos con valores válidos.")
        else:
            total = precio * cantidad
            # Se arma el registro como array de NumPy
            fila_array = np.array([nombre_producto, categoria, precio, cantidad, total], dtype=object)
            st.session_state.registros_productos.append(fila_array)
            st.success(f"Producto '{nombre_producto}' agregado correctamente.")

    st.markdown("### 📊 DataFrame actualizado")
    if len(st.session_state.registros_productos) > 0:
        matriz = np.array(st.session_state.registros_productos, dtype=object)
        df_productos = pd.DataFrame(
            matriz, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"]
        )
        st.dataframe(df_productos, use_container_width=True)
        st.metric("Total acumulado en ventas", f"S/. {df_productos['Total'].astype(float).sum():,.2f}")
    else:
        st.info("Aún no hay productos registrados. Agrega el primero arriba 👆")


# =========================================================================
# 4. EJERCICIO 3 - Uso de funciones desde una librería externa
# =========================================================================
elif seccion == "Ejercicio 3":
    st.title("Ejercicio 3 - Uso de funciones desde una librería externa")
    st.markdown(
        """
        En este ejercicio se conecta **una función** de la librería
        `libreria_funciones_proyecto1.py` con widgets de Streamlit.
        Se seleccionó la función **`calcular_interes_compuesto`**, relacionada
        con el área de **Finanzas / Analytics financiero**, por ser la más
        relevante para el perfil del estudiante.
        """
    )

    st.markdown("### ⚙️ Función seleccionada")
    funcion_elegida = st.selectbox(
        "Selecciona la función a ejecutar",
        ["calcular_interes_compuesto"],
        help="En tu entrega real, elige solo UNA función de la librería relacionada a tu área.",
    )

    st.markdown("### 🔢 Parámetros")
    col1, col2, col3 = st.columns(3)
    with col1:
        capital = st.number_input("Capital inicial (S/.)", min_value=0.0, value=1000.0, step=100.0)
    with col2:
        tasa = st.number_input("Tasa anual (%)", min_value=0.0, value=5.0, step=0.5)
    with col3:
        anios = st.number_input("Número de años", min_value=1, value=3, step=1)

    if st.button("Ejecutar función"):
        if funcion_elegida == "calcular_interes_compuesto":
            resultado = calcular_interes_compuesto(capital, tasa, int(anios))
            st.success(f"Monto final proyectado: **S/. {resultado:,.2f}**")

            st.session_state.historial_funcion.append(
                {
                    "Función": funcion_elegida,
                    "Capital": capital,
                    "Tasa (%)": tasa,
                    "Años": anios,
                    "Resultado (S/.)": resultado,
                }
            )

    st.markdown("### 📈 Histórico de resultados")
    if len(st.session_state.historial_funcion) > 0:
        df_historial = pd.DataFrame(st.session_state.historial_funcion)
        st.dataframe(df_historial, use_container_width=True)
    else:
        st.info("Aún no has ejecutado la función. Ingresa los parámetros y presiona el botón 👆")


# =========================================================================
# 5. EJERCICIO 4 - Uso de clases desde una librería externa con CRUD
# =========================================================================
elif seccion == "Ejercicio 4":
    st.title("Ejercicio 4 - Uso de clases desde una librería externa con CRUD")
    st.markdown(
        """
        En este ejercicio se conecta **una clase** de la librería
        `libreria_clases_proyecto1.py` con widgets de Streamlit, implementando
        las 4 operaciones CRUD: **Crear, Leer, Actualizar y Eliminar**.
        """
    )

    clases_disponibles = {
        "GestorProductos": GestorProductos,
        "GestorClientes": GestorClientes,
        "GestorTareas": GestorTareas,
    }

    clase_elegida = st.selectbox("Selecciona la clase a utilizar", list(clases_disponibles.keys()))

    # Si el usuario cambia de clase, se reinicia la instancia
    if (
        st.session_state.gestor_crud is None
        or type(st.session_state.gestor_crud).__name__ != clase_elegida
    ):
        st.session_state.gestor_crud = clases_disponibles[clase_elegida]()

    gestor = st.session_state.gestor_crud

    tabs = st.tabs(["➕ Crear", "📋 Leer", "✏️ Actualizar", "🗑️ Eliminar"])

    # ---------------- CREAR ----------------
    with tabs[0]:
        st.markdown("#### Crear nuevo registro")
        if clase_elegida == "GestorProductos":
            nombre = st.text_input("Nombre del producto", key="crear_nombre")
            categoria = st.text_input("Categoría", key="crear_categoria")
            precio = st.number_input("Precio", min_value=0.0, step=1.0, key="crear_precio")
            stock = st.number_input("Stock", min_value=0, step=1, key="crear_stock")
            if st.button("Crear producto"):
                gestor.crear(nombre, categoria, precio, stock)
                st.success("Producto creado correctamente.")

        elif clase_elegida == "GestorClientes":
            nombre = st.text_input("Nombre del cliente", key="crear_nombre_cli")
            correo = st.text_input("Correo", key="crear_correo")
            telefono = st.text_input("Teléfono", key="crear_telefono")
            if st.button("Crear cliente"):
                gestor.crear(nombre, correo, telefono)
                st.success("Cliente creado correctamente.")

        elif clase_elegida == "GestorTareas":
            titulo = st.text_input("Título de la tarea", key="crear_titulo")
            prioridad = st.selectbox("Prioridad", ["Alta", "Media", "Baja"], key="crear_prioridad")
            if st.button("Crear tarea"):
                gestor.crear(titulo, prioridad)
                st.success("Tarea creada correctamente.")

    # ---------------- LEER ----------------
    with tabs[1]:
        st.markdown("#### Registros actuales")
        registros = gestor.leer()
        if len(registros) > 0:
            st.dataframe(pd.DataFrame(registros), use_container_width=True)
        else:
            st.info("Todavía no hay registros. Crea uno en la pestaña 'Crear'.")

    # ---------------- ACTUALIZAR ----------------
    with tabs[2]:
        st.markdown("#### Actualizar registro existente")
        registros = gestor.leer()
        if len(registros) > 0:
            ids_disponibles = [r["id"] for r in registros]
            id_actualizar = st.selectbox("ID del registro a actualizar", ids_disponibles, key="id_act")

            if clase_elegida == "GestorProductos":
                nuevo_precio = st.number_input("Nuevo precio", min_value=0.0, step=1.0, key="act_precio")
                nuevo_stock = st.number_input("Nuevo stock", min_value=0, step=1, key="act_stock")
                if st.button("Actualizar producto"):
                    gestor.actualizar(id_actualizar, precio=nuevo_precio, stock=nuevo_stock)
                    st.success("Producto actualizado correctamente.")

            elif clase_elegida == "GestorClientes":
                nuevo_correo = st.text_input("Nuevo correo", key="act_correo")
                nuevo_telefono = st.text_input("Nuevo teléfono", key="act_telefono")
                if st.button("Actualizar cliente"):
                    gestor.actualizar(id_actualizar, correo=nuevo_correo, telefono=nuevo_telefono)
                    st.success("Cliente actualizado correctamente.")

            elif clase_elegida == "GestorTareas":
                nuevo_estado = st.selectbox(
                    "Nuevo estado", ["Pendiente", "En proceso", "Completada"], key="act_estado"
                )
                if st.button("Actualizar tarea"):
                    gestor.actualizar(id_actualizar, estado=nuevo_estado)
                    st.success("Tarea actualizada correctamente.")
        else:
            st.info("No hay registros disponibles para actualizar.")

    # ---------------- ELIMINAR ----------------
    with tabs[3]:
        st.markdown("#### Eliminar registro")
        registros = gestor.leer()
        if len(registros) > 0:
            ids_disponibles = [r["id"] for r in registros]
            id_eliminar = st.selectbox("ID del registro a eliminar", ids_disponibles, key="id_elim")
            if st.button("Eliminar registro"):
                gestor.eliminar(id_eliminar)
                st.success(f"Registro con ID {id_eliminar} eliminado correctamente.")
        else:
            st.info("No hay registros disponibles para eliminar.")
