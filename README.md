
# Preparación Parcial 1 - Sistema HelpDesk EDU

Este repositorio contiene la solución progresiva a los ejercicios prácticos de preparación para el Primer Parcial de Programación II. El proyecto abarca desde la captura básica de datos por consola hasta la implementación de una arquitectura de software modular orientada a objetos (POO) con modelado UML.

---

## Estructura del Repositorio

```text
Programacion-2-Parcial-1/
│
├── .gitignore
├── README.md
│
├── 01_registro_ticket.py
├── 02_menu_helpdesk.py
├── 03_modelos.py
│
├── 04_modelo_helpdesk.puml
├── 04_modelos_base.py
├── 04_justificacion_relaciones.md
│
└── 05_helpdesk_app/
    ├── modelos.py
    ├── servicios.py
    ├── main.py
    └── README.md

```

---

## Resumen de Ejercicios

### Ejercicio 1: Registro Básico de Tickets por Consola

* **Archivo:** `01_registro_ticket.py`
* **Descripción:** Captura de datos básicos de un ticket (ID, título, descripción, prioridad y solicitante) con validaciones de tipo de dato y campos obligatorios.

### Ejercicio 2: Menú Interactivo en Memoria

* **Archivo:** `02_menu_helpdesk.py`
* **Descripción:** Sistema basado en consolas con menú interactivo (`while` loop) que administra una estructura de datos en memoria para registrar, listar, buscar y cambiar el estado de múltiples tickets.

### Ejercicio 3: Programación Orientada a Objetos (POO)

* **Archivo:** `03_modelos.py`
* **Descripción:** Implementación de las clases `Usuario` y `Ticket` utilizando encapsulamiento (atributos privados/protegidos, `properties`), métodos de negocio para asignación de técnicos y manejo de estados válidos.

### Ejercicio 4: Diagramación UML y Relaciones de Dominio

* **Archivos:** `04_modelo_helpdesk.puml`, `04_modelos_base.py`, `04_justificacion_relaciones.md`
* **Descripción:**
* Diseño del modelo de clases en PlantUML representando `User`, `Ticket`, `Comment`, `History` y `Article`.
* Definición de multiplicidades y ciclo de vida de componentes:
* **Composiciones:** `Ticket` (1) con `Comment` (0..*) e `History` (0..*).
* **Asociaciones:** `User` (1) con `Ticket` (0..*) y `Article` (0..*).


* Justificación escrita en formato Markdown y esqueletos base en Python.



### Ejercicio 5: Miniaplicación HelpDesk Organizada por Módulos

* **Carpeta:** `05_helpdesk_app/`
* **Descripción:** Integración completa en una arquitectura por capas separando la responsabilidad de cada componente:
* `modelos.py`: Entidades POO del dominio (`Usuario` y `Ticket`).
* `servicios.py`: Lógica de negocio y funciones CRUD.
* `main.py`: Interfaz de usuario en consola con flujo completo.
* `README.md`: Documentación específica del módulo.



---

## Requisitos del Sistema

* **Python:** 3.10 o superior.
* **Git:** Para el control de versiones.
* **Visual Studio Code:** Recomendado para edición y ejecución.
* **Extensión PlantUML (VS Code):** Para la visualización del archivo `.puml`.

---

## Instrucciones de Ejecución

Para ejecutar cualquier script o la aplicación principal, abre una terminal en la raíz del proyecto:

### Ejecutar Ejercicios Individuales (1 al 3):

```bash
python 01_registro_ticket.py
python 02_menu_helpdesk.py
python 03_modelos.py

```

### Ejecutar la Aplicación Modular (Ejercicio 5):

```bash
cd 05_helpdesk_app
python main.py

```

---

## Flujo de Trabajo en Git y GitHub

El desarrollo de este repositorio sigue el patrón de trabajo basado en ramas (**Feature Branch Workflow**):

* `main`: Rama de producción con código estable.
* `develop`: Rama de integración para incorporar nuevas funcionalidades.
* `feature/<nombre>`: Ramas temporales destinadas a características o ejercicios específicos, integradas a `develop` mediante Pull Requests.

```

```
