# Práctica Django 7 - API REST Dockerizada

Este proyecto consiste en una **API RESTful** construida con **Django REST Framework (DRF)** y **PostgreSQL**, totalmente dockerizada mediante **Docker Compose**. Incluye gestión de autenticación JWT, control de usuarios, productos, un sistema personalizado de logs, documentación interactiva con **Swagger UI** y soporte para **CORS**.

---

## Tecnologías y Herramientas

* **Lenguaje:** Python 3.12
* **Framework:** Django 5.x & Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL
* **Contenedores:** Docker & Docker Compose
* **Documentación:** Swagger UI / OpenAPI (`drf_yasg`)
* **Autenticación:** JSON Web Tokens (JWT)
* **Testing:** Django Test Suite

---

## Estructura del Proyecto

```text
.
├── autentificacion/     # Módulo de autenticación JWT y vistas de logs
├── gestion_usuarios/    # Módulo para administración de usuarios
├── gestion_productos/   # Módulo para catálogo de productos
├── logs/                # Archivos de registros del sistema
│   ├── auditoria.log    # Trazabilidad de operaciones de usuario/negocio
│   └── tecnico.log      # Excepciones, errores del servidor e infraestructura
├── Dockerfile           # Configuración del contenedor Django
├── docker-compose.yml   # Orquestación de servicios (Django + PostgreSQL)
├── manage.py            # Script de gestión de Django
└── requirements.txt     # Dependencias del proyecto Python
