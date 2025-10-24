# Práctica 3: Automatización de Compilación con GitHub Actions

Este proyecto es un ejemplo de automatización de compilación usando GitHub Actions para un programa en Python.

## 📋 Descripción del Proyecto

Este repositorio contiene un programa simple en Python que demuestra cómo configurar un flujo de trabajo automatizado con GitHub Actions. El proyecto incluye:

- **main.py**: Programa principal con funciones de ejemplo
- **test_main.py**: Pruebas unitarias para verificar el funcionamiento
- **requirements.txt**: Dependencias del proyecto
- **.github/workflows/build.yml**: Configuración de GitHub Actions

## 🚀 Características del Workflow

El workflow automatizado incluye:

1. **Compilación y pruebas** en múltiples versiones de Python (3.8, 3.9, 3.10, 3.11, 3.12)
2. **Verificación de sintaxis** del código
3. **Ejecución de pruebas unitarias** con pytest
4. **Análisis de calidad de código** con flake8, black e isort
5. **Generación de reportes de cobertura**
6. **Notificaciones automáticas** en caso de fallo

## 📁 Estructura del Proyecto

```
Practica-workflow/
├── .github/
│   └── workflows/
│       └── build.yml          # Configuración de GitHub Actions
├── main.py                    # Programa principal
├── test_main.py              # Pruebas unitarias
├── requirements.txt          # Dependencias
└── README.md                 # Este archivo
```

## 🛠️ Instalación y Uso Local

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos para ejecutar localmente

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd Practica-workflow
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

4. **Ejecutar las pruebas:**
   ```bash
   python test_main.py
   ```

## 🔄 GitHub Actions

### ¿Qué hace el workflow?

El archivo `.github/workflows/build.yml` configura un workflow que se ejecuta automáticamente cuando:

- Se hace push a la rama `main`
- Se crea un pull request hacia `main`

### Pasos del workflow:

1. **Clonar el repositorio**
2. **Configurar Python** (múltiples versiones)
3. **Instalar dependencias**
4. **Verificar sintaxis** del código
5. **Ejecutar pruebas unitarias**
6. **Ejecutar el programa principal**
7. **Análisis de calidad de código**
8. **Generar reportes de cobertura**

## 📊 Verificar la Ejecución

1. Ve a la pestaña **Actions** en GitHub
2. Verás el workflow ejecutándose automáticamente
3. Al finalizar, verifica si la compilación fue exitosa
4. Revisa los logs para ver detalles de la ejecución

## 🧪 Experimentar

### Cambios que puedes hacer:

1. **Modificar el código** en `main.py` y hacer push
2. **Agregar nuevas pruebas** en `test_main.py`
3. **Cambiar las versiones de Python** en el workflow
4. **Agregar dependencias** en `requirements.txt`
5. **Configurar notificaciones** adicionales

### Ejemplo de modificación:

Puedes agregar una nueva función en `main.py`:

```python
def multiplicar(a, b):
    """Función que multiplica dos números"""
    return a * b
```

Y su correspondiente prueba en `test_main.py`:

```python
def test_multiplicar(self):
    """Prueba la función multiplicar"""
    resultado = multiplicar(3, 4)
    self.assertEqual(resultado, 12)
```

## 📚 Recursos Adicionales

- [Documentación de GitHub Actions](https://docs.github.com/en/actions)
- [Python Testing con pytest](https://docs.pytest.org/)
- [Configuración de workflows](https://docs.github.com/en/actions/using-workflows)

## 🎯 Objetivos de la Práctica

✅ Configurar un flujo de trabajo en GitHub Actions  
✅ Automatizar la compilación de un proyecto Python  
✅ Ejecutar pruebas automáticamente  
✅ Verificar la calidad del código  
✅ Generar reportes de cobertura  
✅ Configurar notificaciones en caso de fallo  

---

**Nota**: Este proyecto es parte de la Práctica 3 de automatización de compilación con GitHub Actions.