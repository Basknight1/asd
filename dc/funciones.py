
CARGOS = ['ceo', 'analista', 'desarrollador']


def registrar_trabajadores(trabajadores):
    # PREGUNTAMOS EL NOMBRE
    nombre = input("ingrese nombre del trabajador: ").capitalize()
    # VERIFICAMOS QUE EL USUARIO INGRESE SOLO LETRAS.
    apellido = input("ingrese apellido del trabajador: ").capitalize()
    cargo = input(
        "ingrese cargo del trabajador: (ceo/analista/desarrollador): ").lower()
    # ESTABLECEMOS QUE SI EL CARGO NO ESTÁ EN CARGOS, PREGUNTAR NUEVAMENTE EL CARGO.
    while cargo not in CARGOS:
        cargo = input(
            "\nCargo ingresado no existe. Porf favor, intente nuevamente\nIngrese el cargo del trabajador: (ceo/analista/desarrollador): ").lower()
        # PREGUNTAMOS SUELDO BRUTO PARA LUEGO HACER LOS DESCUENTOS DE SALUD Y AFP Y DAR EL VALOR LIQUIDO DE PAGO.
    sueldo_bruto = int(input("ingrese sueldo bruto del trabajador: "))
    # DESCUENTOS
    descuento_salud = sueldo_bruto * 0.07
    descuento_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - descuento_salud - descuento_afp
    # LA LISTA DE TRABAJADORES QUE CREAMOS EN EL PRINCIPAL LE AGREGAMOS LOS DATOS EN UN DICCIONARIO.
    trabajadores.append({
        'Nombre': nombre,
        'Apellido': apellido,
        'Cargo': cargo,
        'Sueldo bruto': sueldo_bruto,
        'Descuento de salud': sueldo_bruto,
        'Descuento de afp': descuento_afp,
        'Liquido a pagar': liquido_pagar
    })


def listar_trabajadores(trabajadores):
    # CREAMOS UN PRINT CON NOMBRE DE LA LISTA.
    print("LISTA DE TRABAJADORES")
    # RECORREMOS EN TRABAJADORES Y MOSTRAMOS EL TRABAJADOR CON UN FOR.
    for trabajador in trabajadores:
        print(trabajador)


def imprimir_planilla(trabajadores):
    # PREGUNTAR SI QUIERE IMPRIMIR UN CARGO ESPECIFICO O TODOS LOS CARGOS.
    cargo_seleccionado = input(
        "Ingrese un cargo para imprimir la planilla o presione ENTER para imprimir todos: ").lower()
    # VERIFICAMOS SI ES UN CARGO ESPCIFICO O TODOS.
    if cargo_seleccionado == "":
        # CREAMOS UNA NUEVA LISTA Y CREAMOS EL ARCHIVO .TXT
        imprimir_trabajadores = trabajadores
        nombre_archivo = f'planilla_todos.txt'
        # VERIFICAMOS SI CARGO SELECCIONADO ESTÁ EN LA LISTA DE CARGOS.
    elif cargo_seleccionado in CARGOS:
        # CREAMOS UNA NUEVA LISTA
        imprimir_trabajadores = []
        # RECORREMOS EN TRABAJADORES PARA VER EL CARGO SEA EL INGRESADO POR EL USUARIO Y AGREGARLO A LA LISTA QUE CREAMOS.
        for trabajador in trabajadores:
            # EL TRABAJADOR CON LA CLAVE VERIFICA EL CARGO SELECCIONADO POR EL USUARIO.
            if trabajador['Cargo'] == cargo_seleccionado:
                # AGREGAMOS EL TRABAJADOR CON LA CLAVE,VALOR DEL CARGO INGRESADO POR EL USUARIO.
                imprimir_trabajadores.append(trabajador)
                # CREAMOS EL NOMBRE DEL ARCHIVO TXT CON EL INPUT DEL CARGO SELECCIONADO.
        nombre_archivo = f'planilla_{cargo_seleccionado}.txt'
    else:
        print("cargo no válido.")
        return

    with open(nombre_archivo, 'w') as archivo:
        for trabajador in imprimir_trabajadores:
            archivo.write(f"Nombre: {trabajador['Nombre']}\n")
            archivo.write(f"Apellido: {trabajador['Apellido']}\n")
            archivo.write(f"Cargo: {trabajador['Cargo']}\n")
            archivo.write(f"Sueldo bruto: {trabajador['Sueldo bruto']}\n")
            archivo.write(
                f"Descuento de salud: {trabajador['Descuento de salud']}\n")
            archivo.write(
                f"Descuento de afp: {trabajador['Descuento de afp']}\n")
            archivo.write(
                f"Liquido a pagar: {trabajador['Liquido a pagar']}\n")
