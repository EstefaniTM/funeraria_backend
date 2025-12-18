# Sistema de Gestión de Funeraria - API REST

API REST desarrollada con Django REST Framework para la gestión integral de servicios funerarios. Incluye gestión de clientes, servicios, vehículos, empleados, materiales, ubicaciones, servicios contratados y facturación.

## Tabla de Contenido

- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Endpoints de la API](#endpoints-de-la-api)
- [Autenticación](#autenticación)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Sistema de Permisos](#sistema-de-permisos)
- [Manejo de Errores](#manejo-de-errores)
- [Autor](#autor)

## Características

- **CRUD completo** para 8 entidades del sistema (Clientes, Servicios, Vehículos, Materiales, Empleados, Ubicaciones, Servicios Contratados, Facturas)
- **Autenticación Token** (Django REST Framework Token Authentication)
- **Sistema de permisos**: usuarios normales y administradores
- **Filtros y búsquedas avanzadas** por nombre, descripción, cliente, etc.
- **Paginación automática** de resultados (10 por página por defecto)
- **Validaciones de datos** y manejo de errores estructurado
- **Base de datos SQLite** (desarrollo) / PostgreSQL (producción)
- **Arquitectura modular**: ViewSets separados por entidad para mejor mantenibilidad

## Tecnologías

- **Django 5.2** - Framework web
- **Django REST Framework 3.14** - API REST
- **Django REST Framework Token Authentication** - Autenticación por Token
- **SQLite 3** - Base de datos (desarrollo)
- **Python 3.9+** - Lenguaje de programación

## Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- virtualenv (recomendado)

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd funeraria_backend
```

### 2. Crear y activar entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

### 1. Configurar variables de entorno (opcional)

Crear un archivo `.env` en la raíz del proyecto (aunque actualmente el proyecto usa valores por defecto):

```env
DEBUG=True
SECRET_KEY=tu-clave-secreta-muy-segura
```

### 2. Ejecutar migraciones

```bash
cd funeraria
python manage.py makemigrations
python manage.py migrate
```

### 3. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

Seguir las instrucciones para crear un usuario administrador. Ejemplo:

```
Username: admin
Email: admin@funeraria.com
Password: admin123
```

### 4. Cargar datos de prueba (opcional)

Si hay archivo de fixtures:

```bash
python manage.py loaddata initial_data
```

## Ejecución

### Iniciar el servidor de desarrollo

```bash
cd funeraria
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

### Acceder al panel de administración

URL: `http://localhost:8000/admin`

Usar las credenciales del superusuario creado anteriormente.

## Endpoints de la API

**Base URL:** `http://localhost:8000/api/`

### Autenticación

| Método | Endpoint | Descripción | Público |
|--------|----------|-------------|---------|
| POST | `/auth/login/` | Obtener token | ✅ |
| POST | `/auth/registro/` | Registrar usuario | ✅ |

### Entidades Principales (CRUD Completo)

Todas las entidades tienen los siguientes endpoints:

| Método | Endpoint | Descripción | Auth Requerida |
|--------|----------|-------------|----------------|
| GET | `/api/{entidad}/` | Listar todos | No |
| GET | `/api/{entidad}/{id}/` | Obtener detalle | No |
| POST | `/api/{entidad}/` | Crear nuevo | Sí |
| PUT | `/api/{entidad}/{id}/` | Actualizar completo | Sí |
| PATCH | `/api/{entidad}/{id}/` | Actualizar parcial | Sí |
| DELETE | `/api/{entidad}/{id}/` | Eliminar | Sí (solo Admin) |

### Listado de Entidades

- **clientes** - Clientes de la funeraria
- **servicios** - Servicios disponibles
- **vehiculos** - Vehículos/carrozas
- **materiales** - Inventario de materiales
- **empleados** - Personal de la funeraria
- **ubicaciones** - Ubicación del servicio
- **servicios-contratados** - Servicios contratados por clientes
- **facturas** - Facturas de servicios

## Autenticación

### 1. Obtener Token

**Request:**

```bash
POST http://localhost:8000/api/auth/login/
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**

```json
{
  "token": "e582032d71cf30ca985dbf2b33be9c6928679a74",
  "usuario": "admin",
  "email": "admin@funeraria.com"
}
```

### 2. Usar Token en Requests

Incluir el token en el header `Authorization`:

```bash
Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74
```

### 3. Registrar Nuevo Usuario

**Request:**

```bash
POST http://localhost:8000/api/auth/registro/
Content-Type: application/json

{
  "username": "nuevo_usuario",
  "password": "password123",
  "email": "usuario@funeraria.com"
}
```

**Response:**

```json
{
  "token": "nuevo_token_generado",
  "usuario": "nuevo_usuario"
}
```

## Ejemplos de Uso

### Ejemplo 1: Listar clientes

```bash
curl -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  http://localhost:8000/api/clientes/
```

**Response:**

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "nombre": "Juan",
      "apellido": "García",
      "fecha_funeral": "2025-12-25",
      "habitacion": "101",
      "velatorio": "Central"
    }
  ]
}
```

### Ejemplo 2: Crear un cliente

```bash
curl -X POST \
  -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "PruebaPostman",
    "apellido": "Usuario",
    "fecha_funeral": "2025-12-31",
    "habitacion": "200",
    "velatorio": "Central"
  }' \
  http://localhost:8000/api/clientes/
```

### Ejemplo 3: Crear un servicio

```bash
curl -X POST \
  -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Entierro Completo",
    "precio": 5000.00,
    "descripcion": "Servicio completo de entierro"
  }' \
  http://localhost:8000/api/servicios/
```

### Ejemplo 4: Actualizar cliente (PUT)

```bash
curl -X PUT \
  -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Updated",
    "apellido": "García",
    "fecha_funeral": "2025-12-26",
    "habitacion": "102",
    "velatorio": "Central"
  }' \
  http://localhost:8000/api/clientes/1/
```

### Ejemplo 5: Actualizar parcial (PATCH)

```bash
curl -X PATCH \
  -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  -H "Content-Type: application/json" \
  -d '{"habitacion": "303"}' \
  http://localhost:8000/api/clientes/1/
```

### Ejemplo 6: Buscar clientes

```bash
curl -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  "http://localhost:8000/api/clientes/?search=juan"
```

### Ejemplo 7: Crear factura

```bash
curl -X POST \
  -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  -H "Content-Type: application/json" \
  -d '{
    "cliente": 1,
    "total": 5000.00,
    "estado": "pendiente"
  }' \
  http://localhost:8000/api/facturas/
```

### Ejemplo 8: Eliminar cliente (solo admin)

```bash
curl -X DELETE \
  -H "Authorization: Token e582032d71cf30ca985dbf2b33be9c6928679a74" \
  http://localhost:8000/api/clientes/1/
```

## Estructura del Proyecto

```
funeraria_backend/
├── funeraria/                          # Proyecto Django
│   ├── funeraria/                      # Configuración principal
│   │   ├── settings.py                # Configuración del proyecto
│   │   ├── urls.py                    # URLs principales
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── api/                            # Aplicación principal
│   │   ├── models.py                  # Modelos de datos
│   │   ├── serializers.py             # Serializers de DRF
│   │   ├── views/                     # ViewSets separados por entidad
│   │   │   ├── __init__.py
│   │   │   ├── auth.py                # Endpoints de autenticación
│   │   │   ├── cliente.py             # ViewSet de Cliente
│   │   │   ├── servicio.py            # ViewSet de Servicio
│   │   │   ├── vehiculo.py            # ViewSet de Vehículo
│   │   │   ├── material.py            # ViewSet de Material
│   │   │   ├── empleado.py            # ViewSet de Empleado
│   │   │   ├── ubicacion.py           # ViewSet de Ubicación
│   │   │   ├── servicio_contratado.py # ViewSet de ServicioContratado
│   │   │   ├── factura.py             # ViewSet de Factura
│   │   │   └── pagination.py          # Configuración de paginación
│   │   ├── urls.py                    # URLs de la app
│   │   ├── exceptions.py              # Manejador de excepciones personalizado
│   │   ├── admin.py                   # Configuración del admin
│   │   └── migrations/                # Migraciones de base de datos
│   ├── manage.py                       # Script de gestión de Django
│   ├── requirements.txt                # Dependencias del proyecto
│   ├── db.sqlite3                      # Base de datos SQLite
│   └── .env.example                    # Ejemplo de variables de entorno
├── Funeraria_API_Complete.postman_collection.json  # Colección Postman para testing
├── README.md                           # Este archivo
└── .gitignore                          # Archivos ignorados por git
```

## Sistema de Permisos

### Permisos por Endpoint

| Acción | Usuario Anónimo | Usuario Autenticado | Administrador |
|--------|-----------------|-------------------|---------------|
| GET (Listar) | ✅ | ✅ | ✅ |
| GET (Detalle) | ✅ | ✅ | ✅ |
| POST (Crear) | ❌ | ✅ | ✅ |
| PUT (Actualizar) | ❌ | ✅ | ✅ |
| PATCH (Actualizar Parcial) | ❌ | ✅ | ✅ |
| DELETE (Eliminar) | ❌ | ❌ | ✅ |

**Notas:**
- Las lecturas (GET) son públicas
- Las creaciones y ediciones requieren autenticación
- Las eliminaciones solo están permitidas para administradores (`is_staff=True`)

## Manejo de Errores

La API devuelve códigos de estado HTTP apropiados:

| Código | Significado | Ejemplo |
|--------|-------------|---------|
| 200 | OK - Solicitud exitosa | GET exitoso |
| 201 | Created - Recurso creado | POST exitoso |
| 400 | Bad Request - Datos inválidos | Campos requeridos faltantes |
| 401 | Unauthorized - No autenticado | Sin token en el header |
| 403 | Forbidden - Sin permisos | Usuario intenta eliminar sin ser admin |
| 404 | Not Found - Recurso no encontrado | ID no existe |
| 500 | Internal Server Error | Error del servidor |

### Ejemplo de error de validación

```json
{
  "error": "Datos inválidos",
  "detalles": {
    "nombre": ["Este campo es requerido."],
    "fecha_funeral": ["Formato de fecha inválido."]
  }
}
```

### Ejemplo de error de autenticación

```json
{
  "error": "No autenticado",
  "detalles": "Authentication credentials were not provided."
}
```

### Ejemplo de error de permisos

```json
{
  "error": "Solo administradores pueden eliminar"
}
```

## Testing

### Usando Postman

Se incluye una colección Postman (`Funeraria_API_Complete.postman_collection.json`) que contiene todos los endpoints. Para usarla:

1. Abrir Postman
2. Importar la colección
3. Configurar la variable `token` con el token obtenido del login
4. Ejecutar los requests

### Usando curl

Ver sección [Ejemplos de Uso](#ejemplos-de-uso) para ejemplos con curl.

## Notas de Desarrollo

### Agregar un nuevo endpoint

1. Crear un archivo en `api/views/` (ej. `nueva_entidad.py`)
2. Definir el ViewSet
3. Importarlo en `api/views/__init__.py`
4. Registrarlo en `api/urls.py` con el router

Ejemplo:

```python
# api/views/nueva_entidad.py
from rest_framework import viewsets
from ..models import NuevaEntidad
from ..serializers import NuevaEntidadSerializer

class NuevaEntidadViewSet(viewsets.ModelViewSet):
    queryset = NuevaEntidad.objects.all()
    serializer_class = NuevaEntidadSerializer
```

Luego en `api/urls.py`:

```python
from .views import NuevaEntidadViewSet
router.register(r'nueva-entidad', NuevaEntidadViewSet, basename='nueva-entidad')
```

## Autor

**Estefani Tipantuña**

---

Última actualización: 27 de Noviembre de 2025
