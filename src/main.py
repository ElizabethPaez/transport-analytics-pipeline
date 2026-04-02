import pandas as pd

# Leer datos
df = pd.read_csv("data/sample_data.csv")

# Calcular tiempo promedio por ruta
resultado = df.groupby(["origen", "destino"])["tiempo"].mean().reset_index()

print("📊 Tiempo promedio por ruta:")
print(resultado)
