temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

# Converte para Celsius
if origem == "F":
    temp_c = (temp - 32) * 5 / 9
elif origem == "K":
    temp_c = temp - 273.15
else:
    temp_c = temp

# Converte de Celsius para destino
if destino == "F":
    resultado = (temp_c * 9 / 5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    resultado = temp_c

print(f"Temperatura convertida: {resultado:.2f}°{destino}")
