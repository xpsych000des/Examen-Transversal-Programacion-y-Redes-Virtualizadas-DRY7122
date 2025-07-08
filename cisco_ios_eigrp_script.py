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

# Configuración EIGRP Nombrado (AS 666)
config_commands = [
    'router eigrp PEREIRA-QUINTANA',
    'address-family ipv4 unicast autonomous-system 666',
    'af-interface default',
    'passive-interface',
    'exit-af-interface',
    'exit-address-family',
    'address-family ipv6 unicast autonomous-system 666',
    'af-interface default',
    'passive-interface',
    'exit-af-interface',
    'exit-address-family',
]

# Enviar Configuración
output_config = net_connect.send_config_set(config_commands)

# Obtener EIGRP de la Configuración en Ejecución (running-config)
output_eigrp = net_connect.send_command("show running-config | section eigrp")

# Mostrar Resultados
print("=== CONFIGURACIÓN ENVIADA ===")
print(output_config)
print("\n=== RUNNING-CONFIG SECTION EIGRP ===")
print(output_eigrp)