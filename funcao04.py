# Fórmula para calcular: (°C * 9/5) + 32

def celsius_para_fahrenheit (graus) :
    conversao = (graus * 9/5) + 32
    return conversao

numero = float(input ("Informe a temperatura em °C: "))

print(f"A temperatura de {numero}°C corresponde a {celsius_para_fahrenheit(numero)}°F")
