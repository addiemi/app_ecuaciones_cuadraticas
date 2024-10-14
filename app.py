import streamlit as st
import plotly.graph_objects as go
import math

def calcular_soluciones(a, b, c):
    """Calcula las soluciones de una ecuación cuadrática."""
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None  # No hay soluciones reales
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (x1, x2)

def main():
    st.set_page_config(page_title="Simulación de Puente", layout="centered")
    st.title("🏗️ Simulación de Puente con Distribución de Peso")
    
    # Sección de Instrucciones
    st.header("📋 Instrucciones para Usar la Aplicación")
    st.markdown(""" 
    1. **Configurar los Parámetros del Puente**:
       - En la barra lateral, ajusta los valores de los coeficientes `a`, `b` y `c` para definir la forma del arco del puente.
       
    2. **Visualizar las Soluciones**:
       - La aplicación calculará las soluciones de la ecuación cuadrática y representará gráficamente el puente.
       
    3. **Interpretar el Gráfico**:
       - La **plataforma** del puente está representada por una línea negra.
       - El **arco** del puente está representado por una línea roja.
       
    4. **Experimentos**:
       - Cambia los valores de `a`, `b` y `c` para ver cómo afecta la estructura del puente y sus soportes.
    """)
    
    st.sidebar.header("🔧 Parámetros del Puente")
    
    # Entradas del usuario para los coeficientes de la ecuación cuadrática
    a = st.sidebar.number_input("Coeficiente a (curvatura del arco)", value=-2)
    b = st.sidebar.number_input("Coeficiente b (altura máxima del arco)", value=8)
    c = st.sidebar.number_input("Coeficiente c (posición del arco)", value=-5)
    
    st.write(f"La ecuación del arco del puente es: {a}x² + ({b})x + ({c}) = 0")
    
    soluciones = calcular_soluciones(a, b, c)
    
    if soluciones:
        st.subheader("📊 Soluciones de la Ecuación")
        st.write(f"Solución 1: {soluciones[0]}")
        st.write(f"Solución 2: {soluciones[1]}")
        
        # Gráfico del puente usando Plotly
        fig = go.Figure()
        
        # Dibujar la carretera del puente
        fig.add_trace(go.Scatter(x=[soluciones[0], soluciones[1]], y=[0, 0],
                                 mode='lines',
                                 name='Plataforma',
                                 line=dict(color='black', width=4)))
        
        # Dibujar el arco del puente
        arco_x = [soluciones[0], (soluciones[0] + soluciones[1])/2, soluciones[1]]
        arco_y = [0, 3, 0]  # Puedes ajustar la altura del arco
        fig.add_trace(go.Scatter(x=arco_x, y=arco_y,
                                 mode='lines',
                                 name='Arco',
                                 line=dict(color='red', width=3)))
        
        # Configurar la gráfica
        fig.update_layout(title='Representación Simplificada del Puente',
                          xaxis_title='Posición (metros)',
                          yaxis_title='Altura (metros)',
                          showlegend=True,
                          width=700,
                          height=400)
        
        st.plotly_chart(fig)
        
    else:
        st.error("La ecuación del arco del puente no tiene soluciones reales.")

if __name__ == "__main__":
    main()
