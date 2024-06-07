def calcular_imc(peso_kg, altura_m):

  try:
      imc = peso_kg / (altura_m ** 2)
      return imc
  except ZeroDivisionError:
      return "La altura no puede ser cero. Ingresa una altura válida."

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

resultado_imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {resultado_imc:.2f}")

if resultado_imc < 18.5:
  print("Bajo peso")
elif 18.5 <= resultado_imc < 24.9:
  print("Peso normal")
elif 25 <= resultado_imc < 29.9:
  print("Sobrepeso")
else:
  print("Obesidad")
