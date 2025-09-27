# M6_AE4_grupal

## Ejercicio grupal: Aplicación de Registro de Eventos en Django

### Participantes

**Grupo 4**
- Natalia
- Felipe
- Daniel
- Cecilia

### Objetivo

Desarrollar una aplicación web en Django que permita a los usuarios registrar eventos y participantes, practicando la creación, validación y procesamiento de formularios, el uso de plantillas reutilizables y la vinculación con modelos.

### Contexto

La aplicación permite registrar eventos con información relevante y una lista de participantes. Cada evento incluye nombre, fecha, ubicación y participantes (nombre y correo electrónico).

### Requisitos

#### Formulario de Registro de Eventos

- **Campos:**
  - Nombre del Evento (`CharField`, obligatorio, máx. 100 caracteres)
  - Fecha (`DateField`, obligatorio, debe ser futura)
  - Ubicación (`CharField`, opcional)
- **Validaciones:**
  - La fecha debe ser futura.
  - El nombre no debe superar los 100 caracteres.

#### Formulario para Participantes

- Permite agregar múltiples participantes por evento.
- **Campos:**
  - Nombre del Participante (`CharField`, obligatorio)
  - Correo Electrónico (`EmailField`, obligatorio)

#### Uso de FormClass de Django

- Crear una `FormClass` para el formulario de eventos.
- Crear una `FormClass` para el formulario de participantes.
- Enlazar ambos formularios con la vista correspondiente.

#### Vistas y Templates

- Vista para manejar solicitudes GET (mostrar formularios) y POST (procesar datos).
- Mostrar errores de validación debajo de los campos incorrectos.
- Utilizar plantillas reutilizables para los formularios de eventos y participantes.
- Template base para los formularios, usando bloques para modificar el contenido de cada formulario específico.

#### Validación y Manejo de Errores

- Mostrar mensajes de error adecuados si el formulario no es válido.
- Mostrar mensaje de confirmación si el registro es exitoso.

### Estructura del Proyecto

- `env/`: Entorno virtual con dependencias.
- `registro_reservas/`: App principal con modelos, formularios, vistas y templates.
- `README.md`: Este archivo.
- `requerimientos.txt`: Instrucciones del proyecto.

M6_AE4_grupal/
│
├─ env/
│   ├─ pyvenv.cfg
│   ├─ Include/
│   ├─ Lib/
│   └─ Scripts/
├─ registro_reservas/
│   ├─ db.sqlite3
│   ├─ manage.py
│   ├─ eventos/
│   │   ├─ __init__.py
│   │   ├─ admin.py
│   │   ├─ apps.py
│   │   ├─ form.py
│   │   ├─ models.py
│   │   ├─ tests.py
│   │   ├─ urls.py
│   │   ├─ views.py
│   │   ├─ migrations/
│   │   │   ├─ __init__.py
│   │   └─ templates/
│   │       ├─ base.html
│   │       ├─ footer.html
│   │       ├─ formulario_base.html
│   │       ├─ index.html
│   │       ├─ registro_evento.html
│   │       ├─ registro_exitoso.html
│   │       └─ registro_participantes.html
│   └─ registro_reservas/
│       ├─ __init__.py
│       ├─ asgi.py
│       ├─ settings.py
│       ├─ urls.py
│       └─ wsgi.py
├─ README.md
└─ requerimientos.txt

### Cómo ejecutar

1. Instala las dependencias en el entorno virtual.
2. Ejecuta las migraciones:  
   ```sh
   python manage.py migrate
3. Inicia el servidor de desarrollo:
    python manage.py runserver
4. Accede a la aplicación en http://localhost:8000.

Trabajo grupal para el módulo 6 del Bootcamp Python.