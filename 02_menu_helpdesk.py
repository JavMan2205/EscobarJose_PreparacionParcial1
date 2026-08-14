CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]

def pedir_opcion():
    """Muestra las opciones del menú principal y captura la elección del usuario."""
    print("\n" + "=" * 45)
    print("         SISTEMA HELPDESK EDU - MENÚ         ")
    print("=" * 45)
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Resumen por prioridad")
    print("5. Salir")
    print("=" * 45)
    opcion = input("Seleccione una opción (1-5): ").strip()
    return opcion

def registrar_ticket(tickets):
    """Solicita los datos de un nuevo ticket, los valida y lo agrega a la lista."""
    print("\nREGISTRO DE NUEVO TICKET")
    
    while True:
        entrada_num = input("Ingrese el número de ticket: ").strip()
        try:
            numero = int(entrada_num)
            if numero <= 0:
                print("El número debe ser un entero positivo.")
                continue
            if any(t["numero"] == numero for t in tickets):
                print(f"Ya existe un ticket registrado con el ID #{numero}.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    while True:
        solicitante = input("Ingrese el nombre del solicitante: ").strip()
        if solicitante:
            break
        print("El campo 'solicitante' no puede estar vacío.")

    while True:
        titulo = input("Ingrese el título del ticket: ").strip()
        if titulo:
            break
        print("El campo 'título' no puede estar vacío.")

    while True:
        descripcion = input("Ingrese la descripción del problema: ").strip()
        if descripcion:
            break
        print("El campo 'descripción' no puede estar vacío.")

    while True:
        cat_input = input(f"Ingrese categoría ({', '.join(CATEGORIAS_VALIDAS)}): ").strip()
        categoria = next((c for c in CATEGORIAS_VALIDAS if c.lower() == cat_input.lower()), None)
        if categoria:
            break
        print("Categoría no válida. Intente de nuevo.")

    while True:
        prio_input = input(f"Ingrese prioridad ({', '.join(PRIORIDADES_VALIDAS)}): ").strip()
        prioridad = next((p for p in PRIORIDADES_VALIDAS if p.lower() == prio_input.lower()), None)
        if prioridad:
            break
        print("Prioridad no válida. Intente de nuevo.")

    nuevo_ticket = {
        "numero": numero,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    tickets.append(nuevo_ticket)
    print(f"Ticket #{numero} registrado con éxito.")

def listar_tickets(tickets):
    """Muestra en pantalla todos los tickets guardados hasta el momento."""
    print("\nLISTADO GENERAL DE TICKETS")
    if len(tickets) == 0:
        print("No hay tickets registrados en el sistema.")
        return

    print(f"Total de tickets registrados: {len(tickets)}\n")
    for t in tickets:
        print(f"[#{t['numero']}] {t['titulo']}")
        print(f"   Solicitante: {t['solicitante']} | Categoría: {t['categoria']} | Prioridad: {t['prioridad']} | Estado: {t['status']}")
        print("-" * 45)

def buscar_por_solicitante(tickets):
    """Filtra y muestra los tickets que coincidan con el solicitante buscado."""
    print("\nBUSCAR TICKETS POR SOLICITANTE")
    if len(tickets) == 0:
        print("No hay tickets registrados para realizar la búsqueda.")
        return

    busqueda = input("Ingrese el nombre (o parte) del solicitante a buscar: ").strip().lower()
    coincidencias = []

    for t in tickets:
        if busqueda in t["solicitante"].lower():
            coincidencias.append(t)

    if len(coincidencias) == 0:
        print(f"No se encontraron tickets para el solicitante '{busqueda}'.")
    else:
        print(f"\nSe encontraron {len(coincidencias)} ticket(s):")
        for t in coincidencias:
            print(f"[#{t['numero']}] {t['titulo']} - Solicitante: {t['solicitante']} ({t['prioridad']})")

def mostrar_resumen(tickets):
    """Cuenta y muestra la cantidad de tickets clasificados por cada nivel de prioridad."""
    print("\nRESUMEN DE TICKETS POR PRIORIDAD")
    if len(tickets) == 0:
        print("No hay tickets registrados para mostrar resumen.")
        return

    conteo = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}

    for t in tickets:
        prio = t["prioridad"]
        if prio in conteo:
            conteo[prio] += 1

    print(f"Total acumulado: {len(tickets)} tickets")
    for prioridad, cantidad in conteo.items():
        print(f"Prioridad {prioridad:8}: {cantidad}")

def ejecutar_menu():
    """Función principal que mantiene el ciclo de ejecución del menú."""
    tickets = []
    
    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_ticket(tickets)
        elif opcion == "2":
            listar_tickets(tickets)
        elif opcion == "3":
            buscar_por_solicitante(tickets)
        elif opcion == "4":
            mostrar_resumen(tickets)
        elif opcion == "5":
            print("\nSaliendo del sistema HelpDesk EDU.")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    ejecutar_menu()