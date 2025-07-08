from netmiko import ConnectHandler

# Datos CSR1kv (Router)
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',       # Dirección IP
    'username': 'cisco',            # Usuario
    'password': 'cisco123!',        # Contraseña
}

# Conexión al Router por SSH
net_connect = ConnectHandler(**router)
net_connect.enable()

# Visualizar Info. sobre el Estado de Interfaces IP
output_interfaces = net_connect.send_command("show ip interface brief")

# Visualizar Config. en Ejecución (running-config)
output_running_config = net_connect.send_command("show running-config")

# Obtener Info. de Versión del Router
output_version = net_connect.send_command("show version")

# Mostrar Resultados
print("\n=== ESTADO DE INTERFACES (IP/STATUS) ===")
print(output_interfaces)

print("\n=== RUNNING CONFIG ===")
print(output_running_config)

print("\n=== INFORMACIÓN SOBRE VERSIÓN DEL ROUTER ===")
print(output_version)