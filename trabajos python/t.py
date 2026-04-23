#saquenme 2
empleados = [
    {id: 1, "nombre": "david", "rol": "admin", "activo":True},
    {id: 2, "nombre": "sebastian", "rol": "vive100", "activo":True},
    {id: 3, "nombre": "sofia", "rol": "gerente", "activo":True},
    {id: 4, "nombre": "miguel", "rol": "vive100", "activo":True},
    {id: 5, "nombre": "santiago", "rol": "vive100", "activo":False},
    ]
for emp in empleados:
    if emp["rol"] == "vive100" and emp["activo"]:
        print(f"El empleado {emp['nombre']}se encuentra activo")
