# Sistema de Registro de Eventos y Participantes

Una aplicación web desarrollada en Django para la gestión y registro de eventos con sus respectivos participantes.

## Descripción del Proyecto

Este sistema permite crear y gestionar eventos, así como registrar participantes para cada evento. La aplicación implementa formularios con validaciones personalizadas, plantillas reutilizables y una interfaz intuitiva para la gestión completa del proceso de registro.

## Funcionalidades Principales

### 🎯 Gestión de Eventos
- **Registro de Eventos**: Crear nuevos eventos con información completa
- **Campos del Evento**:
  - Nombre del evento (obligatorio, máximo 100 caracteres)
  - Fecha del evento (obligatorio, debe ser fecha futura)
  - Ubicación del evento (opcional)
  - Descripción detallada (opcional)
- **Validaciones**:
  - La fecha no puede ser en el pasado
  - Validación de longitud de campos

### 👥 Gestión de Participantes
- **Registro de Participantes**: Inscribir participantes a eventos existentes
- **Campos del Participante**:
  - Nombre completo (obligatorio)
  - Correo electrónico (obligatorio, único en el sistema)
  - Número de teléfono (opcional)
  - Selección del evento al que se inscribe
- **Validaciones**:
  - Verificación de correo electrónico único
  - Formato válido de email
  - Asociación obligatoria con un evento

### 📊 Dashboard y Visualización
- **Página Principal**: Vista general de todos los eventos y participantes
- **Lista de Eventos**: Visualización de todos los eventos registrados
- **Lista de Participantes**: Visualización de todos los participantes registrados
- **Confirmación de Registro**: Página de éxito tras completar registros

## Tecnologías Utilizadas

- **Framework**: Django 5.2.6
- **Base de Datos**: SQLite3 (por defecto)
- **Frontend**: HTML5 con templates de Django
- **Lenguaje**: Python 3.x
- **ORM**: Django ORM

## Estructura del Proyecto

```
M6_AE4_grupal/
│
├── requirements.txt              # Dependencias del proyecto
├── README.md                    # Documentación del proyecto
│
└── registro_reservas/           # Proyecto Django principal
    ├── manage.py               # Comando principal de Django
    ├── db.sqlite3             # Base de datos SQLite
    │
    ├── eventos/               # Aplicación principal
    │   ├── models.py         # Modelos de datos (Evento, Participantes)
    │   ├── views.py          # Lógica de vistas
    │   ├── form.py           # Formularios con validaciones
    │   ├── urls.py           # URLs de la aplicación
    │   ├── admin.py          # Configuración del admin
    │   └── templates/        # Plantillas HTML
    │       ├── base.html                # Template base
    │       ├── index.html              # Página principal
    │       ├── registro_evento.html    # Formulario de eventos
    │       ├── registro_participantes.html # Formulario de participantes
    │       ├── registro_exitoso.html   # Página de confirmación
    │       ├── formulario_base.html    # Base para formularios
    │       └── footer.html            # Footer común
    │
    └── registro_reservas/     # Configuración del proyecto
        ├── settings.py       # Configuraciones principales
        ├── urls.py          # URLs principales del proyecto
        ├── wsgi.py          # Configuración WSGI
        └── asgi.py          # Configuración ASGI
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd M6_AE4_grupal
```

### 2. Crear Entorno Virtual
```bash
python -m venv env
```

### 3. Activar Entorno Virtual
**Windows:**
```bash
env\Scripts\activate
```

**macOS/Linux:**
```bash
source env/bin/activate
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar Base de Datos
```bash
cd registro_reservas
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor
```bash
python manage.py runserver
```

### 8. Acceder a la Aplicación
Abrir navegador en: `http://localhost:8000`

## Uso del Sistema

### Página Principal
- Acceder a `http://localhost:8000`
- Visualizar lista de eventos y participantes registrados
- Navegar a formularios de registro

### Registrar un Evento
1. Click en "Registrar Evento" o ir a `/registro_evento/`
2. Completar el formulario:
   - Nombre del evento
   - Fecha (debe ser futura)
   - Ubicación (opcional)
   - Descripción (opcional)
3. Click en "Registrar Evento"
4. Confirmación de registro exitoso

### Registrar un Participante
1. Click en "Registrar Participante" o ir a `/registro_participantes/`
2. Completar el formulario:
   - Seleccionar evento de la lista
   - Nombre del participante
   - Correo electrónico
   - Teléfono (opcional)
3. Click en "Registrar Participante"
4. Confirmación de registro exitoso

### Panel de Administración
- Acceder a `http://localhost:8000/admin/`
- Usar credenciales de superusuario
- Gestionar eventos y participantes desde interfaz administrativa

## Modelos de Datos

### Modelo Evento
```python
class Evento(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    fecha = models.DateField(null=False)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
```

### Modelo Participantes
```python
class Participantes(models.Model):
    evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False)
    correo = models.EmailField(unique=True, null=False)
    telefono = models.CharField(max_length=15, blank=True)
```

## Validaciones Implementadas

### Eventos
- **Fecha futura**: No se permite registrar eventos con fechas pasadas
- **Longitud de nombre**: Máximo 100 caracteres para el nombre del evento

### Participantes
- **Correo único**: Cada correo electrónico solo puede estar registrado una vez
- **Formato de email**: Validación automática del formato de correo electrónico
- **Asociación con evento**: Obligatorio seleccionar un evento existente

## URLs Disponibles

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | index | Página principal con listados |
| `/registro_evento/` | registro_evento | Formulario de registro de eventos |
| `/registro_participantes/` | registro_participantes | Formulario de registro de participantes |
| `/registro_exitoso/` | registro_exitoso | Página de confirmación |
| `/admin/` | admin | Panel de administración |

## Equipo de Desarrollo

**Grupo 4 - Bootcamp Python**
- Natalia
- Felipe  
- Daniel
- Cecilia

## Objetivos Académicos

Este proyecto fue desarrollado como parte del **Módulo 6** del Bootcamp Python, con los siguientes objetivos de aprendizaje:

✅ Creación y validación de formularios en Django  
✅ Uso de plantillas reutilizables con herencia  
✅ Implementación de modelos con relaciones ForeignKey  
✅ Manejo de vistas basadas en funciones  
✅ Validaciones personalizadas en formularios  
✅ Procesamiento de solicitudes GET y POST  
✅ Configuración de URLs y routing  
✅ Uso de mensajes de error y confirmación

## 📋 Registro de Cambios (Changelog)

### [1.1.0] - 2025-01-03

#### ✨ Añadido
- **requirements.txt**: Archivo de dependencias del proyecto con todas las librerías necesarias
  - Django 5.2.6 como framework principal
  - pytz para manejo de zonas horarias
  - whitenoise para archivos estáticos
  - python-decouple para configuraciones
  - email-validator para validaciones de correo

#### 📝 Actualizado
- **README.md**: Documentación completa del proyecto incluyendo:
  - Descripción detallada del sistema y sus funcionalidades
  - Guía de instalación paso a paso
  - Instrucciones de uso completas
  - Documentación de modelos de datos
  - Estructura del proyecto actualizada
  - URLs disponibles y su descripción
  - Validaciones implementadas
  - Objetivos académicos del proyecto

#### 🔧 Mejorado
- Documentación técnica con ejemplos de código
- Instrucciones claras para diferentes sistemas operativos
- Tabla de URLs con descripciones detalladas
- Sección de tecnologías utilizadas
- Guía de uso del sistema completa

### [1.0.0] - Versión Inicial

#### ✨ Características Principales
- Sistema de registro de eventos con validaciones
- Registro de participantes vinculados a eventos
- Formularios Django con validaciones personalizadas
- Plantillas HTML reutilizables con herencia
- Modelos con relaciones ForeignKey
- Panel de administración de Django
- Base de datos SQLite integrada
- Validación de fechas futuras para eventos
- Validación de correos electrónicos únicos
- Páginas de confirmación de registro
- Vista principal con listado de eventos y participantes

#### 🏗️ Estructura Implementada
- Modelos: Evento y Participantes
- Formularios: EventoForm y ParticipantesForm  
- Vistas: index, registro_evento, registro_participantes, registro_exitoso
- Templates: base.html, formulario_base.html, y templates específicos
- URLs configuradas para navegación completa
- Configuración Django estándar con app 'eventos'

---

**Notas**: Este proyecto forma parte del ejercicio grupal M6_AE4 del Bootcamp Python, desarrollado por el Grupo 4.