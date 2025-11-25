# Funeraria Backend API

API REST para gestión de servicios funerarios desarrollada con Django y Django REST Framework.

## Requisitos

- Python 3.8+
- pip

## Instalación

```bash
# Crear y activar venv
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Hacer migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Correr servidor
python manage.py runserver
```

La API estará en `http://localhost:8000/api/`

### 7. Ejecutar servidor
```bash
python manage.py runserver
```

El servidor estará en: `http://127.0.0.1:8000/`

## Autenticación

### Registrar nuevo usuario
```bash
POST /api/auth/registro/

Body:
{
  "username": "usuario",
  "password": "contraseña",
  "email": "email@example.com"
}

Response:
{
  "token": "abc123xyz...",
  "usuario": "usuario"
}
```

### Login
```bash
POST /api/auth/login/

Body:
{
  "username": "usuario",
  "password": "contraseña"
}

Response:
{
  "token": "abc123xyz...",
  "usuario": "usuario"
}
```

### Usar el token
Agregar en headers de todas las peticiones:
```
Authorization: Token abc123xyz...
```

## Endpoints CRUD

Todos requieren autenticación.

### Clientes
- `GET /api/clientes/` - Listar todos
- `GET /api/clientes/?search=juan` - Buscar
- `GET /api/clientes/1/` - Obtener uno
- `POST /api/clientes/` - Crear
- `PUT /api/clientes/1/` - Actualizar
- `DELETE /api/clientes/1/` - Eliminar

### Servicios
- `GET /api/servicios/` - Listar todos
- `POST /api/servicios/` - Crear
- `PUT /api/servicios/1/` - Actualizar
- `DELETE /api/servicios/1/` - Eliminar

### Vehículos
- `GET /api/vehiculos/` - Listar todos
- `POST /api/vehiculos/` - Crear
- `PUT /api/vehiculos/1/` - Actualizar
- `DELETE /api/vehiculos/1/` - Eliminar

### Materiales
- `GET /api/materiales/` - Listar todos
- `POST /api/materiales/` - Crear
- `PUT /api/materiales/1/` - Actualizar
- `DELETE /api/materiales/1/` - Eliminar

### Empleados
- `GET /api/empleados/` - Listar todos
- `POST /api/empleados/` - Crear
- `PUT /api/empleados/1/` - Actualizar
- `DELETE /api/empleados/1/` - Eliminar

### Ubicaciones
- `GET /api/ubicaciones/` - Listar todas
- `POST /api/ubicaciones/` - Crear
- `PUT /api/ubicaciones/1/` - Actualizar
- `DELETE /api/ubicaciones/1/` - Eliminar

### Servicios Contratados
- `GET /api/servicios-contratados/` - Listar todos
- `POST /api/servicios-contratados/` - Crear
- `PUT /api/servicios-contratados/1/` - Actualizar
- `DELETE /api/servicios-contratados/1/` - Eliminar

### Facturas
- `GET /api/facturas/` - Listar todas
- `POST /api/facturas/` - Crear
- `PUT /api/facturas/1/` - Actualizar
- `DELETE /api/facturas/1/` - Eliminar

## Paginación

Por defecto: 10 resultados por página

```bash
GET /api/clientes/?page=1
GET /api/clientes/?page=2
```

## Búsqueda

Clientes: `?search=nombre` o `?search=apellido`
Servicios: `?search=nombre`
Empleados: `?search=nombre` o `?search=cargo`
Vehículos: `?search=placa` o `?search=modelo`

## Ejemplo en Postman

1. Registrar usuario: `POST /api/auth/registro/`
2. Obtener token: `POST /api/auth/login/`
3. Usar token en Authorization header
4. Hacer peticiones CRUD

## Estructura de proyecto

```
funeraria/
├── manage.py
├── requirements.txt
├── funeraria/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── urls.py
    └── migrations/
```

## Notas

- Base de datos: PostgreSQL
- Framework: Django 5.0
- API: Django REST Framework
- Autenticación: Token Authentication
- Paginación: 10 items por página

