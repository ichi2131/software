import os
import time

RUTA = r"C:\Users\shado\OneDrive\Desktop\chamba"

while True:
    os.chdir(RUTA)
    
    status = os.popen("git status --porcelain").read()
    
    if status:
        print("Cambios detectados...")
        os.system("git add .")
        os.system('git commit -m "auto update"')
        os.system("git push")
        print("Subido a GitHub 🚀")
    else:
        print("Sin cambios")
    
    time.sleep(300)  # cada 5 minutos