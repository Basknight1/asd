import funciones as fn
# CREAMOS UNA LISTA PARA DESPUÉS REGISTRAR A LOS TRABAJADORES
trabajadores = []
# MENU
while True:
    try:
        print("\n***BIENVENIDO AL SISTEMA DE PAGO DE SUELDOS\n¿Qué necesita hacer?\n1. Registrar usuario\n2. Listar todos los trabajadores\n3. Imprimir planilla de sueldos\n4. Salir")
        opc = int(input("ingrese opción: "))
        # LLAMAMOS LA FUNCION CON FN. Y AGREGAMOS TRABAJADORES AL PARENTESIS.
        if opc == 1:
            fn.registrar_trabajadores(trabajadores)
        elif opc == 2:
            fn.listar_trabajadores(trabajadores)
        elif opc == 3:
            fn.imprimir_planilla(trabajadores)
        elif opc == 4:
            print("Saliendo del programa....")
        else:
            print("Opción no válida, intente nuevamente.")
    except ValueError:
        print("\n*******INGRESE UNA OPCIÓN VÁLIDA, INTENTE NUEVAMENTE*******\n")
