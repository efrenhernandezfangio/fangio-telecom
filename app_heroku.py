#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FANGIO TELECOM - Versión Heroku
Optimizada para despliegue en la nube
"""

import os
import sys
from datetime import datetime

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar la aplicación original
from app import app

# Configuración para Heroku
if __name__ == '__main__':
    # Obtener puerto de Heroku o usar 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    
    print("🚀 INICIANDO FANGIO TELECOM EN HEROKU")
    print("=" * 50)
    print(f"🌐 Puerto: {port}")
    print(f"🌍 URL: https://fangio-telecom.herokuapp.com")
    print(f"🔧 Modo: Producción")
    print("=" * 50)
    
    # Agregar rutas adicionales para Heroku
    @app.route('/status')
    def status():
        return {
            'status': 'running',
            'timestamp': datetime.now().isoformat(),
            'version': 'FANGIO TELECOM - Heroku',
            'users': 'Equipo distribuido (CDMX, Guadalajara, etc.)',
            'access': 'Desde cualquier lugar',
            'platform': 'Heroku'
        }
    
    @app.route('/info')
    def info():
        return {
            'servidor': 'FANGIO TELECOM - Heroku',
            'ubicacion': 'Nube (Heroku)',
            'equipo': 'CDMX, Guadalajara, etc.',
            'funcionalidades': [
                'Site Survey',
                'Diseño de Solución', 
                'Subida de archivos',
                'Previsualización'
            ],
            'url': 'https://fangio-telecom.herokuapp.com'
        }
    
    # Ejecutar la aplicación
    app.run(host='0.0.0.0', port=port, debug=False) 