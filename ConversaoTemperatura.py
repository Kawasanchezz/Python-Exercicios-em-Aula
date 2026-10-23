def converte_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

celsius = float(input("Digite a temperatura em graus Celsius:"))
fahrenheit, kelvin = converte_temperatura (celsius)

print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
print(f"A temperatura em Kelvin é: {kelvin:.2f}°K")