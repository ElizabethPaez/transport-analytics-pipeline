import pandas as pd

# -------------------------
# 1. Cargar datos
# -------------------------
df = pd.read_csv("data/sample_data.csv")

print("📂 Datos cargados:")
print(df.head())

# -------------------------
# 2. Procesamiento
# -------------------------
df["datetime"] = pd.to_datetime(df["fecha"] + " " + df["hora"])
df["hour"] = df["datetime"].dt.hour

# -------------------------
# 3. Análisis
# -------------------------

# Tiempo promedio por ruta
rutas = (
    df.groupby(["origen", "destino"])["tiempo"]
    .mean()
    .reset_index()
)

# Viajes por hora (horas pico)
horas = (
    df.groupby("hour")
    .size()
    .reset_index(name="viajes")
    .sort_values("viajes", ascending=False)
)

# -------------------------
# 4. Resultados
# -------------------------

print("\n📊 Tiempo promedio por ruta:")
print(rutas)

print("\n⏰ Viajes por hora (ordenado):")
print(horas)
