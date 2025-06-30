import socket  

def scan_ports(target_ip, ports):  
    print(f"Escaneando puertos en {target_ip}...")  
    for port in ports:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.settimeout(1)  
        result = sock.connect_ex((target_ip, port))  # Intenta la conexión  
        if result == 0:  
            print(f"✅ Puerto {port} abierto")  
        else:  
            print(f"❌ Puerto {port} cerrado")  
        sock.close()  

# Definir la dirección IP y los puertos a escanear  
target = "scanme.nmap.org"  # Puedes cambiarlo por una IP específica  
ports_to_scan = [21, 22, 80, 443]  # Puertos comunes  

scan_ports(target, ports_to_scan)