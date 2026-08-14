from modelos import Usuario, Ticket


def registrar_ticket(tickets, id_ticket, titulo, categoria, prioridad, solicitante):
    if any(t.id == id_ticket for t in tickets):
        print(f"[ERROR] Ya existe un ticket con el ID #{id_ticket}.")
        return None

    nuevo_ticket = Ticket(id_ticket, titulo, categoria, prioridad, solicitante)
    tickets.append(nuevo_ticket)
    print(f"[EXITO] Ticket #{id_ticket} registrado correctamente.")
    return nuevo_ticket


def listar_tickets(tickets):
    print("\nLISTADO GENERAL DE TICKETS")
    if not tickets:
        print("[INFO] No hay tickets registrados en el sistema.")
        return

    print(f"Total de tickets: {len(tickets)}")
    for t in tickets:
        print(t)


def buscar_ticket(tickets, criterio):
    """Busca coincidencias por ID o texto en título/solicitante."""
    resultados = []
    criterio_str = str(criterio).strip().lower()

    for t in tickets:
        if str(t.id) == criterio_str:
            resultados.append(t)
        elif criterio_str in t.solicitante.nombre.lower() or criterio_str in t.titulo.lower():
            resultados.append(t)

    return resultados


def asignar_tecnico(ticket, tecnico):
    if ticket is None:
        print("[ERROR] El ticket especificado no existe.")
        return False

    exito = ticket.asignar_tecnico(tecnico)
    if exito:
        print(f"[EXITO] Tecnico '{tecnico.nombre}' asignado al Ticket #{ticket.id}.")
    else:
        print(f"[ERROR] No se pudo asignar. El usuario '{tecnico.nombre}' debe tener rol 'technician'.")
    return exito


def cambiar_estado(ticket, nuevo_estado):
    if ticket is None:
        print("[ERROR] El ticket especificado no existe.")
        return False

    exito = ticket.cambiar_estado(nuevo_estado)
    if exito:
        print(f"[EXITO] Ticket #{ticket.id}: Estado cambiado a '{nuevo_estado}'.")
    else:
        print(f"[ERROR] '{nuevo_estado}' no es un estado valido. Permitidos: {', '.join(Ticket.ESTADOS_VALIDOS)}.")
    return exito