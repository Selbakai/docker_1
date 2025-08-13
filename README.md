# Docker Learning Project 🐳

[![CI Pipeline](https://github.com/Selbakai/docker_1/actions/workflows/ci.yml/badge.svg)](https://github.com/Selbakai/docker_1/actions/workflows/ci.yml)

Este proyecto es para aprender Docker con Python, incluyendo integración continua (CI/CD).

## 🚀 Características

- Aplicación Python básica
- Tests automatizados con pytest
- Integración continua con GitHub Actions
- Linting de código con flake8
- Cobertura de código

## 🔧 Configuración Local

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación
```bash
python docker.py
```

### 3. Ejecutar tests
```bash
pytest
```

### 4. Ejecutar linting
```bash
flake8 .
```

## 🔄 Integración Continua

El proyecto incluye un pipeline de CI/CD que se ejecuta automáticamente en GitHub Actions cuando:

- Haces push a las ramas `main` o `develop`
- Abres un Pull Request hacia `main`

### El pipeline incluye:

- ✅ **Tests**: Ejecuta todos los tests con pytest
- 🔍 **Linting**: Verifica la calidad del código con flake8 (después de tests)
- 🐍 **Múltiples versiones**: Prueba en Python 3.9, 3.10, 3.11, 3.12
- 🐳 **Docker**: Intenta construir imagen Docker (si existe Dockerfile)
- 📊 **Cobertura**: Genera reportes de cobertura de código

## 📁 Estructura del Proyecto

```
docker_1/
├── .github/
│   └── workflows/
│       └── ci.yml          # Configuración CI/CD
├── tests/
│   ├── __init__.py
│   └── test_docker.py      # Tests del proyecto
├── docker.py               # Aplicación principal
├── requirements.txt        # Dependencias
├── pytest.ini            # Configuración de pytest
├── .gitignore             # Archivos a ignorar
├── .env.example           # Plantilla de variables
└── README.md              # Este archivo
```

## 🔒 Seguridad

- Las variables de entorno se manejan de forma segura
- Los tokens nunca se commitean al repositorio
- Usa `.env` para configuración local (no incluido en Git)