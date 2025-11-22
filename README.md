# TODO Application - Django

Aplicación web de gestión de tareas (TODOs) desarrollada con Django como parte del AI Dev Tools Zoomcamp 2025.

## 📋 Características

- ✅ **Crear TODOs**: Añade nuevas tareas con título, descripción y fecha de vencimiento
- ✏️ **Editar TODOs**: Modifica tareas existentes
- 🗑️ **Eliminar TODOs**: Borra tareas que ya no necesitas
- ⏰ **Fechas de vencimiento**: Asigna fechas límite a tus tareas
- ✓ **Marcar como resuelto**: Cambia el estado de tus tareas entre pendiente y resuelto
- 📅 **Ordenamiento**: Las tareas se muestran ordenadas por fecha de creación (más recientes primero)
- 🎨 **Interfaz moderna**: Diseño responsivo y amigable con gradientes y efectos visuales

## 🛠️ Tecnologías

- **Framework**: Django 5.2.8
- **Python**: 3.13.5
- **Gestor de paquetes**: uv
- **Base de datos**: SQLite (desarrollo)
- **Testing**: Django TestCase

## 📦 Instalación

### Prerrequisitos

- Python 3.13+
- uv (gestor de paquetes Python)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/ayoquiroga/aidevtools-zoomcamp_2025.git
   cd aidevtools-zoomcamp_2025
   ```

2. **Crear entorno virtual con uv**
   ```bash
   uv venv
   ```

3. **Instalar dependencias**
   ```bash
   uv pip install django
   ```

4. **Aplicar migraciones**
   ```bash
   uv run python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   uv run python manage.py createsuperuser
   ```

6. **Iniciar el servidor**
   ```bash
   uv run python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## 🧪 Testing

La aplicación incluye 15 pruebas automatizadas que cubren:

- Pruebas del modelo (creación, validaciones, ordenamiento)
- Pruebas de vistas (CRUD completo)
- Pruebas de integración (flujo completo)

**Ejecutar las pruebas:**
```bash
uv run python manage.py test todos
```

**Resultado esperado:**
```
Ran 15 tests in 0.088s
OK
```

## 📁 Estructura del Proyecto

```
aidevtools-zoomcamp_2025/
├── todoproject/           # Configuración del proyecto Django
│   ├── settings.py       # Configuraciones
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # WSGI configuration
├── todos/                # Aplicación de TODOs
│   ├── models.py        # Modelo TODO
│   ├── views.py         # Vistas CRUD
│   ├── forms.py         # Formularios personalizados
│   ├── urls.py          # URLs de la app
│   ├── tests.py         # Pruebas unitarias
│   ├── admin.py         # Configuración del admin
│   ├── templates/       # Plantillas HTML
│   │   └── todos/
│   │       ├── base.html
│   │       ├── todo_list.html
│   │       ├── todo_form.html
│   │       └── todo_confirm_delete.html
│   └── migrations/      # Migraciones de base de datos
├── manage.py            # Utilidad de Django
├── db.sqlite3          # Base de datos SQLite
└── README.md           # Este archivo
```

## 🗄️ Modelo de Datos

### TODO Model

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | Integer | Identificador único (auto-generado) |
| `title` | CharField(200) | Título del TODO (requerido) |
| `description` | TextField | Descripción detallada (opcional) |
| `due_date` | DateField | Fecha de vencimiento (opcional) |
| `resolved` | BooleanField | Estado: resuelto/pendiente (default: False) |
| `created_at` | DateTimeField | Fecha de creación (auto) |
| `updated_at` | DateTimeField | Última actualización (auto) |

## 🎯 Funcionalidades Detalladas

### Crear TODO
- Formulario con validación HTML5
- Selector de fecha con calendario visual
- Campos opcionales para descripción y fecha de vencimiento

### Listar TODOs
- Vista de tarjetas con información completa
- Indicadores visuales de estado (pendiente/resuelto)
- Botones de acción rápida en cada tarjeta

### Editar TODO
- Pre-carga de datos existentes
- Posibilidad de cambiar todos los campos incluido el estado

### Marcar como Resuelto/Pendiente
- Toggle rápido sin entrar al formulario de edición
- Cambio visual inmediato con estilos diferenciados

### Eliminar TODO
- Confirmación antes de eliminar
- Vista previa del TODO a eliminar

## 🔐 Panel de Administración

Django proporciona un panel de administración automático donde puedes gestionar los TODOs de forma más avanzada.

**Acceso:** http://127.0.0.1:8000/admin/

Requiere crear un superusuario con: `uv run python manage.py createsuperuser`

## 🚀 Comandos Útiles

```bash
# Crear migraciones después de cambios en modelos
uv run python manage.py makemigrations

# Aplicar migraciones
uv run python manage.py migrate

# Ejecutar pruebas
uv run python manage.py test

# Iniciar servidor de desarrollo
uv run python manage.py runserver

# Crear superusuario
uv run python manage.py createsuperuser

# Abrir shell interactivo de Django
uv run python manage.py shell
```

## 📝 Notas de Desarrollo

- Las migraciones están incluidas en el repositorio
- El archivo `db.sqlite3` está en `.gitignore` (no se sube al repositorio)
- El entorno virtual `.venv/` también está ignorado
- Se usa `uv` para gestión de dependencias más rápida que pip

## 🤝 Contribuciones

Este proyecto fue desarrollado como parte del AI Dev Tools Zoomcamp 2025.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 👤 Autor

**ayoquiroga**
- GitHub: [@ayoquiroga](https://github.com/ayoquiroga)
- Repositorio: [aidevtools-zoomcamp_2025](https://github.com/ayoquiroga/aidevtools-zoomcamp_2025)

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub