import streamlit as st
import math

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

st.title("🔢 Verificador de Números Primos/Prime Number checker (por Julio García)")

numero = st.number_input("Ingresa un número", min_value=1, step=1)

if st.button("Verificar"):
    if es_primo(numero):
        st.success(f"{numero} es primo ✅")
    else:
        st.error(f"{numero} no es primo ❌")
