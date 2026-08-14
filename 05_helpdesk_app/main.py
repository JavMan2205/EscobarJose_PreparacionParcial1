from modelos import Usuario, Ticket
import servicios


def ejecutar_menu():
    tickets = []

    solicitante_defecto = Usuario(1, "Ana Lopez", "ana.lopez@email.com", "user")
    tecnico_defecto = Usuario(2, "Carlos Gomez", "carlos.gomez@email.com", "technician")

    print("SISTEMA HELPDESK EDU (MODULAR)")
    print(f"Solicitante predeterminado : {solicitante_defecto.nombre}")
    print(f"Tecnico predeterminado     : {tecnico_defecto.nombre}")

    while True:
        print("\n" + "=" * 45)
        print("                 MENU PRINCIPAL              ")
        print("=" * 45)
        print("1. Registrar ticket")
        print("2. Listar tickets")
        print("3. Buscar ticket")
        print("4. Asignar tecnico")
        print("5. Cambiar estado")
        print("6. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opcion (1-6): ").strip()

        if opcion == "1":
            print("\nREGISTRAR TICKET")
            try:
                id_t = int(input("Ingrese ID del ticket: ").strip())
            except ValueError:
                print("[ERROR] El ID debe ser un numero entero.")
                continue

            titulo = input("Ingrese el titulo: ").strip()
            categoria = input("Ingrese categoria (General/Hardware/Software/Network): ").strip()
            prioridad = input("Ingrese prioridad (Low/Medium/High/Critical): ").strip()

            if not titulo or not categoria or not prioridad:
                print("[ERROR] Todos los campos son obligatorios.")
                continue

            servicios.registrar_ticket(tickets, id_t, titulo, categoria, prioridad, solicitante_defecto)

        elif opcion == "2":
            servicios.listar_tickets(tickets)

        elif opcion == "3":
            print("\nBUSCAR TICKET")
            criterio = input("Ingrese ID, titulo o solicitante a buscar: ").strip()
            if not criterio:
                print("[ERROR] Debe ingresar un criterio de busqueda.")
                continue

            encontrados = servicios.buscar_ticket(tickets, criterio)
            if encontrados:
                print(f"[EXITO] Se encontraron {len(encontrados)} coincidencia(s):")
                for t in encontrados:
                    print(t)
            else:
                print(f"[INFO] No se encontraron tickets con el criterio '{criterio}'.")

        elif opcion == "4":
            print("\nASIGNAR TECNICO")
            try:
                id_t = int(input("Ingrese el ID del ticket a asignar: ").strip())
            except ValueError:
                print("[ERROR] El ID debe ser un numero entero.")
                continue

            encontrados = servicios.buscar_ticket(tickets, id_t)
            if encontrados:
                servicios.asignar_tecnico(encontrados[0], tecnico_defecto)
            else:
                print(f"[ERROR] No existe el ticket #{id_t}.")

        elif opcion == "5":
            print("\nCAMBIAR ESTADO")
            try:
                id_t = int(input("Ingrese el ID del ticket: ").strip())
            except ValueError:
                print("[ERROR] El ID debe ser un numero entero.")
                continue

            encontrados = servicios.buscar_ticket(tickets, id_t)
            if encontrados:
                nuevo_est = input(f"Ingrese nuevo estado ({', '.join(Ticket.ESTADOS_VALIDOS)}): ").strip()
                servicios.cambiar_estado(encontrados[0], nuevo_est)
            else:
                print(f"[ERROR] No existe el ticket #{id_t}.")

        elif opcion == "6":
            print("\nSaliendo del sistema HelpDesk EDU")
            break
        else:
            print("[ERROR] Opcion no valida. Seleccione un numero entre 1 y 6.")


if __name__ == "__main__":
    ejecutar_menu()