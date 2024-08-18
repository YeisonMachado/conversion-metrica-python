# Paso 1: solicitar al usuario las medidas de la pieza delmueble en cms

medidas_en_cms = float(input("Por favor, ingrese las medias de la pieza del mueble (en cms): "))

# Paso 2: Convertir las medidas de centímetros a pulgadas

medida_en_pulgadas = medidas_en_cms / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario

print("Las medidas en pulgads de la pieza ingresada son : ", medida_en_pulgadas)