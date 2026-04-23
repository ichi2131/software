#pepe
archivos = [
    {"nombre": "epstein.files", "peso": 40000},
    {"nombre": "basi.exe", "peso": 400},
    {"nombre": "videos.mp4", "peso": 2000},
    {"nombre": "roblox.exe", "peso": 800},
    {"nombre": "tesis.pdf", "peso": 3509},]
espacio =0
for arc in archivos:
    print(f"analizando archivos: {arc['nombre']}...peso:{arc['peso']} mb")
    espacio += arc ['peso']

print(f"peso total de los archivos {espacio} mb")
