import os
import time

while True:
    status = os.popen("git status --porcelain").read()
    
    if status:
        os.system("git add .")
        os.system('git commit -m "auto update"')
        os.system("git push")
        print("Subido 🚀")
    else:
        print("Sin cambios")
    
    time.sleep(300)