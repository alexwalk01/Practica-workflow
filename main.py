#!/usr/bin/env python3
"""
Programa principal de ejemplo para la práctica de GitHub Actions
"""

import sys
import os
from datetime import datetime

def saludar(nombre="Mundo"):
    """Función que saluda a una persona"""
    return f"¡Hola, {nombre}! Bienvenido a la automatización con GitHub Actions."

def calcular_suma(a, b):
    """Función que suma dos números"""
    return a + b

def main():
    """Función principal del programa"""
    print("=" * 50)
    print("🚀 Programa de ejemplo para GitHub Actions")
    print("=" * 50)
    
    # Saludo personalizado
    nombre = "GitHub Actions"
    mensaje = saludar(nombre)
    print(f"\n{mensaje}")
    
    # Ejemplo de cálculo
    print(f"\n📊 Ejemplo de cálculo:")
    num1 = 10
    num2 = 5
    resultado = calcular_suma(num1, num2)
    print(f"La suma de {num1} + {num2} = {resultado}")
    
    # Información del sistema
    print(f"\n📋 Información del sistema:")
    print(f"Python versión: {sys.version}")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"\n✅ Programa ejecutado exitosamente!")
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
