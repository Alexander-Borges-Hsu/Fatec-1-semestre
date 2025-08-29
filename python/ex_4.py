#Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahreinheit
temp_celsius = float(input("Insira a temperatura em celsius (somente números): "))

temp_fahreinheit = (9 * temp_celsius + 160) / 5

print(f"A temperatura de {temp_celsius:.2f}°C convertida para fahreinheit é {temp_fahreinheit:.2f}°F.")