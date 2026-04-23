#saquenmen de aquiiiiii

temperatura = [25.0, 36.7, 18.8, 20.7, 22.2, 16.9]
alertas = 0
for temp in temperatura:
    if  temp > 24.0:
        print(f"temperatura critica: {temp}c°")
        alertas += 1
print (f"alertas generadas = {alertas}")
