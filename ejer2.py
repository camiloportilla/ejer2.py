# Lista de estado de sensores
estadoSensores = [True, True, True, False, False, False, True, False, True, False, False, True, True, False, False, True, False, False, False, True, True, False, False, False, True, True, True, False, True, True, True, False, False, True, False, False, False, True, True, False]

# Contar la cantidad de sensores en estado de error (True) y OK (False)
error_count = estadoSensores.count(True)
ok_count = estadoSensores.count(False)

# Crear el diccionario con las cantidades
resultado = {
    "Sensores OK": ok_count,
    "Sensores en falla": error_count
}
# Imprimir el resultado en forma textual
print(f"Hay {resultado['Sensores OK']} Sensores ok y {resultado['Sensores en falla']} Sensores en falla")