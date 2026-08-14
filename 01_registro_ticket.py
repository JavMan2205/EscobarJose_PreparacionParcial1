CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]

def obtener_numero_ticket():
    """Solicita y valida que el número de ticket sea un entero válido."""
    while True:
        entrada = input("Ingrese el número de ticket: ").strip()
        if not entrada:
            print("Error: El número de ticket no puede estar vacío.")
            continue
        try:
            numero = int(entrada)
            if numero <= 0:
                print("Error: El número de ticket debe ser un entero positivo.")
                continue
            return numero
        except ValueError:
            print("Error: Debe ingresar un valor numérico entero válido (ej. 101).")

def obtener_texto_no_vacio(mensaje_prompt, nombre_campo):
    """Solicita un texto y valida que no esté vacío."""
    while True:
        texto = input(mensaje_prompt).strip()
        if texto:
            return texto
        print(f"Error: El campo '{nombre_campo}' es obligatorio y no puede estar vacío.")

def obtener_opcion_valida(mensaje_prompt, opciones_validas, nombre_campo):
    """Solicita una opción y valida que pertenezca a la lista de opciones permitidas."""
    menciones = ", ".join(opciones_validas)
    while True:
        entrada = input(f"{mensaje_prompt} ({menciones}): ").strip()
        coincidencia = next((opt for opt in opciones_validas if opt.lower() == entrada.lower()), None)
        if coincidencia:
            return coincidencia
        print(f"Error: '{entrada}' no es una {nombre_campo} válida. Opciones permitidas: {menciones}")

def registrar_ticket():
    print("=" * 50)
    print("      SISTEMA DE REGISTRO DE TICKETS     ")
    print("=" * 50)

    numero = obtener_numero_ticket()
    solicitante = obtener_texto_no_vacio("Ingrese el nombre del solicitante: ", "Solicitante")
    titulo = obtener_texto_no_vacio("Ingrese el título del ticket: ", "Título")
    descripcion = obtener_texto_no_vacio("Ingrese la descripción del problema: ", "Descripción")
    categoria = obtener_opcion_valida("Seleccione la categoría", CATEGORIAS_VALIDAS, "categoría")
    prioridad = obtener_opcion_valida("Seleccione la prioridad", PRIORIDADES_VALIDAS, "prioridad")

    ticket = {
        "numero": numero,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    print("\n" + "=" * 50)
    print("        RESUMEN DEL TICKET REGISTRADO CON ÉXITO     ")
    print("=" * 50)
    print(f"Ticket ID   : #{ticket['numero']}")
    print(f"Solicitante : {ticket['solicitante']}")
    print(f"Título      : {ticket['titulo']}")
    print(f"Descripción : {ticket['descripcion']}")
    print(f"Categoría   : {ticket['categoria']}")
    print(f"Prioridad   : {ticket['prioridad']}")
    print(f"Estado      : {ticket['status']}")
    print("=" * 50)

    return ticket

if __name__ == "__main__":
    registrar_ticket()