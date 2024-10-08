temperaturas = [
    26.75431352056954, 21.991086464852872, 27.209759257701366, 23.443668324912598,
    28.8725217962772, 20.731695645337763, 22.58962536117254, 24.846285051127114,
    26.074481791289337, 22.085936681499903, 23.913576519730877, 27.678759112104154,
    24.381354548084965, 23.19239923228099, 20.803472013144523, 21.30390306534694,
    27.102859960400624, 23.763191774421054, 25.157825319899203, 20.2290281340311,
    26.746902019682647, 22.750408458130667, 20.26298637657635, 26.423788201931604
]
# Encontrar los valores mínimos, máximos y promedio
min_temp = min(temperaturas)
max_temp = max(temperaturas)
prom_temp = sum(temperaturas) / len(temperaturas)

# Redondear los resultados a 3 decimales
min_temp = round(min_temp, 3)
max_temp = round(max_temp, 3)
prom_temp = round(prom_temp, 3)
# Mostrar los resultados
print(f"Temperatura mínima: {min_temp}")
print(f"Temperatura máxima: {max_temp}")
print(f"Temperatura promedio: {prom_temp}")