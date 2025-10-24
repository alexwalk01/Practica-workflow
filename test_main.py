#!/usr/bin/env python3
"""
Tests unitarios para el programa principal
"""

import unittest
import sys
import os

# Agregar el directorio actual al path para importar main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import saludar, calcular_suma

class TestPrograma(unittest.TestCase):
    """Clase de pruebas para las funciones del programa"""
    
    def test_saludar_default(self):
        """Prueba la función saludar con valor por defecto"""
        resultado = saludar()
        self.assertEqual(resultado, "¡Hola, Mundo! Bienvenido a la automatización con GitHub Actions.")
    
    def test_saludar_personalizado(self):
        """Prueba la función saludar con nombre personalizado"""
        resultado = saludar("Alex")
        self.assertEqual(resultado, "¡Hola, Alex! Bienvenido a la automatización con GitHub Actions.")
    
    def test_calcular_suma_positivos(self):
        """Prueba la función calcular_suma con números positivos"""
        resultado = calcular_suma(5, 3)
        self.assertEqual(resultado, 8)
    
    def test_calcular_suma_negativos(self):
        """Prueba la función calcular_suma con números negativos"""
        resultado = calcular_suma(-5, -3)
        self.assertEqual(resultado, -8)
    
    def test_calcular_suma_mixtos(self):
        """Prueba la función calcular_suma con números mixtos"""
        resultado = calcular_suma(10, -3)
        self.assertEqual(resultado, 7)
    
    def test_calcular_suma_decimales(self):
        """Prueba la función calcular_suma con números decimales"""
        resultado = calcular_suma(2.5, 1.5)
        self.assertEqual(resultado, 4.0)

if __name__ == "__main__":
    # Ejecutar las pruebas
    unittest.main(verbosity=2)
