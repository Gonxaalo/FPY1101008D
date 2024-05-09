import os

Pikachu_Roll = 4500
Otaku_Roll = 5000
Pulpo_Roll = 5200
Anguila_Roll = 4800

contador = 0
salir = False
factura = {
    "Pikachu Roll": 0,
    "Otaku Roll": 0,
    "Pulpo Venenoso Roll": 0,
    "Anguila Eléctrica Roll": 0
}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Bienvenido a nuestro menú de sushi")
    print("1. Pikachu Roll $4500")
    print("2. Otaku Roll $5000")
    print("3. Pulpo Venenoso Roll $5200")
    print("4. Anguila Eléctrica Roll $4800")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese su opción en número: "))

        if opcion == 1:
            cantidad_pikachu = int(input("¿Cuántos Pikachu Roll va a llevar?: "))
            subtotal = Pikachu_Roll * cantidad_pikachu
            print(f"Subtotal Pikachu Roll: ${subtotal}")
            factura["Pikachu Roll"] += cantidad_pikachu
            contador += 1
        elif opcion == 2:
            cantidad_otaku = int(input("¿Cuántos Otaku Roll va a llevar?: "))
            subtotal = Otaku_Roll * cantidad_otaku
            print(f"Subtotal Otaku Roll: ${subtotal}")
            factura["Otaku Roll"] += cantidad_otaku
            contador += 1
        elif opcion == 3:
            cantidad_pulpo = int(input("¿Cuántos Pulpo Venenoso Roll va a llevar?: "))
            subtotal = Pulpo_Roll * cantidad_pulpo
            print(f"Subtotal Pulpo Venenoso Roll: ${subtotal}")
            factura["Pulpo Venenoso Roll"] += cantidad_pulpo
            contador += 1
        elif opcion == 4:
            cantidad_anguila = int(input("¿Cuántos Anguila Eléctrica Roll va a llevar?: "))
            subtotal = Anguila_Roll * cantidad_anguila
            print(f"Subtotal Anguila Eléctrica Roll: ${subtotal}")
            factura["Anguila Eléctrica Roll"] += cantidad_anguila
            contador += 1
        elif opcion == 5:
            salir = True
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Ingrese un número válido.")

    if contador > 0:
        input("Presione Enter para continuar...")

    if salir:
        break

if contador > 0:
    total_productos = sum(factura.values())
    subtotal = (Pikachu_Roll * factura["Pikachu Roll"]) + (Otaku_Roll * factura["Otaku Roll"]) + \
               (Pulpo_Roll * factura["Pulpo Venenoso Roll"]) + (Anguila_Roll * factura["Anguila Eléctrica Roll"])
    descuento = subtotal * 0.1
    total = subtotal - descuento

    print("******************************")
    print(f"TOTAL PRODUCTOS: {total_productos}")
    print("******************************")
    print(f"Pikachu Roll: {factura['Pikachu Roll']}")
    print(f"Otaku Roll: {factura['Otaku Roll']}")
    print(f"Pulpo Venenoso Roll: {factura['Pulpo Venenoso Roll']}")
