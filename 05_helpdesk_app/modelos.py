class Usuario:
    def __init__(self, id_usuario: int, nombre: str, email: str, rol: str):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"Usuario #{self.id}: {self.nombre} ({self.email}) - Rol: {self.rol}"


class Ticket:
    ESTADOS_VALIDOS = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, id_ticket: int, titulo: str, categoria: str, prioridad: str, solicitante: Usuario):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._status = "Open"

    @property
    def status(self):
        return self._status

    def cambiar_estado(self, nuevo_estado: str) -> bool:
        """Cambia el estado encapsulado si pertenece a la lista de estados válidos."""
        if nuevo_estado in Ticket.ESTADOS_VALIDOS:
            self._status = nuevo_estado
            return True
        return False

    def asignar_tecnico(self, tecnico: Usuario) -> bool:
        """Asigna el técnico solo si su rol corresponde a 'technician'."""
        if isinstance(tecnico, Usuario) and tecnico.rol.lower() == "technician":
            self.tecnico = tecnico
            return True
        return False

    def __str__(self):
        nombre_solicitante = self.solicitante.nombre if isinstance(self.solicitante, Usuario) else str(self.solicitante)
        nombre_tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"
        return (f"Ticket #{self.id} | Titulo: {self.titulo} | Categoria: {self.categoria} | "
                f"Prioridad: {self.prioridad} | Estado: {self._status} | "
                f"Solicitante: {nombre_solicitante} | Tecnico: {nombre_tecnico}")