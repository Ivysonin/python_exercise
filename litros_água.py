'''
Exercicio:
    Calcular a quantidade de água que precisa para agoar as plantas
    dependendo da temperatura e da quantidade de água que a planta suporta
'''

def waterPlants(temperature, plants):
    total_water = 0

    for planta in plants:
        if 20 <= temperature <= 25:
            if planta == 'Flores':
                total_water += 1
            elif planta == 'Vegetais':
                total_water += 1.5
            elif planta == 'Arbustos':
                total_water += 2
        elif temperature > 25:
            if planta == 'Flores':
                total_water += 1.5
            elif planta == 'Vegetais':
                total_water += 2
            elif planta == 'Arbustos':
                total_water += 3
        elif temperature < 20:
            total_water += 0.5
    return total_water

temperatura = 19
plantas = ["Flores", "Vegetais", "Arbustos"]

print(f'Precisa de {waterPlants(temperatura, plantas)} L de água para agoar as plantas')