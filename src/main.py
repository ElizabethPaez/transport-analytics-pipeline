import pandas as pd

# Leer datos
df = pd.read_csv("data/sample_data.csv")

# Convertir fecha y hora
df["datetime"] = pd.to_datetime(df["fecha"] + " " + df["hora"])

# Extraer hora
df["hour"] = df["datetime"].dt.hour

# Tiempo promedio por ruta
rutas = df.groupby(["origen", "destino"])["tiempo"].mean().reset_index()

# Conteo por hora (para detectar horas pico)
horas = df.groupby("hour").size().reset_index(name="viajes")

print("Tiempo promedio por ruta:")
print(rutas)

print("\n Viajes por hora:")
print(horas)
