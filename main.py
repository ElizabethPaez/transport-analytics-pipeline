import pandas as pd

# Simulación de datos
data = {
    "origen": ["A", "B", "A", "C"],
    "destino": ["B", "C", "C", "A"],
    "tiempo": [10, 15, 20, 25]
}

df = pd.DataFrame(data)

# Calcular tiempo promedio por ruta
resultado = df.groupby(["origen", "destino"])["tiempo"].mean().reset_index()

print(resultado)
