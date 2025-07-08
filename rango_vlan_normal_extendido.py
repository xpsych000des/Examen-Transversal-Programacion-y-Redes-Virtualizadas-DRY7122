# Rango NORMAL (1–1005)
# Rango EXTENDIDO (1006–4094)

# Insta al usuario a escribir el número de VLAN
vlan_input = input("Ingresa el número de VLAN del cual quieras información: ")

# Verifica si el valor es un número entero
try:
    vlan = int(vlan_input)

    # Validación del rango de VLAN
    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} corresponde al rango NORMAL.")
    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} corresponde al rango EXTENDIDO.")
    elif vlan == 0 or vlan == 4095:
        print(f"La VLAN {vlan} está reservada.")
    else:
        print("El número de VLAN ingresado, se encuentra fuera de un rango válido (1-4094).")
except ValueError:
    print("Solicitud fallida. Por favor, ingresa un número entero.")