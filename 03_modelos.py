class Usuario:
    def __init__(self, id_usuario, nombre, email, rol):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"Usuario #{self.id}: {self.nombre} ({self.email}) - Rol: {self.rol}"


class Ticket:
    ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, id_ticket, titulo, categoria, prioridad, solicitante, tecnico=None):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante  
        self.tecnico = tecnico         
        self._status = "Open"           

    def cambiar_estado(self, nuevo_estado):
        """Valida que el nuevo estado sea permitido antes de modificar _status."""
        if nuevo_estado in Ticket.ESTADOS_VALIDOS:
            self._status = nuevo_estado
            print(f"[EXITO] Ticket #{self.id}: Estado actualizado a '{self._status}'.")
        else:
            print(f"[ERROR] Ticket #{self.id}: '{nuevo_estado}' no es un estado valido. Estados permitidos: {', '.join(Ticket.ESTADOS_VALIDOS)}.")

    def asignar_tecnico(self, tecnico):
        """Asigna un técnico al ticket solo si su rol es 'technician'."""
        if isinstance(tecnico, Usuario) and tecnico.rol.lower() == "technician":
            self.tecnico = tecnico
            print(f"[EXITO] Ticket #{self.id}: Tecnico '{tecnico.nombre}' asignado correctamente.")
        else:
            nombre = tecnico.nombre if isinstance(tecnico, Usuario) else str(tecnico)
            print(f"[ERROR] Ticket #{self.id}: No se pudo asignar a '{nombre}'. El usuario debe tener el rol 'technician'.")

    def __str__(self):
        nombre_solicitante = self.solicitante.nombre if isinstance(self.solicitante, Usuario) else str(self.solicitante)
        nombre_tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return (f"Ticket #{self.id} | Titulo: {self.titulo} | Categoria: {self.categoria} | "
                f"Prioridad: {self.prioridad} | Estado: {self._status} | "
                f"Solicitante: {nombre_solicitante} | Tecnico: {nombre_tecnico}")


if __name__ == "__main__":
    print("CREACION DE USUARIOS Y TICKETS")

    usuario_1 = Usuario(1, "Ana Lopez", "ana.lopez@email.com", "user")
    usuario_2 = Usuario(2, "Carlos Gomez", "carlos.gomez@email.com", "technician")

    tickets = [
        Ticket(101, "Fallo de red en laboratorio", "Network", "High", usuario_1),
        Ticket(102, "Error de impresion", "Hardware", "Medium", usuario_1),
        Ticket(103, "Solicitud de software", "Software", "Low", usuario_1)
    ]

    print("\nEstado Inicial de los Tickets")
    for ticket in tickets:
        print(ticket)

    print("\nEJECUCION DE PRUEBAS MINIMAS")

    tickets[0].asignar_tecnico(usuario_2)

    tickets[1].asignar_tecnico(usuario_1)

    tickets[0].cambiar_estado("In Progress")

    tickets[2].cambiar_estado("EstadoInvalido")

    print("\nEstado Final de los Tickets")
    for ticket in tickets:
        print(ticket)