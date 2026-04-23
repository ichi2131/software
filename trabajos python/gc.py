#for 4 continue
latencia = [20, 120, -34, 30, 12, 0, 300]
latencias_validas = 0
for lat in latencia:
    if lat <=0:
        print (f"latencia corrupta o incorrecta encontrada: {lat}ms")
        continue
    print(f"procesando latencias correctas: {lat}ms")
    latencias_validas +=1

print(f" se procesaron {latencias_validas} latencias correptas")
