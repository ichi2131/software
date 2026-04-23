#bluque 3
intentosmax = 3
intentosbase = 0

acceso = False
while intentosmax > intentosbase and not acceso:

    contra = input("ingrese su contraseña:")
    if contra == "123_bbc":
        print ("acceso consedido, pase master")
        acceso = True
    else :
        intentosbase += 1
        intentosres =intentosmax - intentosbase
        print("te quedan ", intentosres)
if not acceso:
    print("te quedastes sin intentos")
        
