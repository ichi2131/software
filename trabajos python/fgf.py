#ñanga

ips = ["192.1168.1.1", "123.424.2.2", "423.454.321.3", "243.56.78.6"]
ip_vec = "243.56.78.6"

for ip in ips:
    print(f"analisando ip {ip}")
    print
    if ip == ip_vec:
        print(f"bloqueando ip del intruso {ip} - acceso denegado")
        break
print("analisis terminad")
