# FANGIO TELECOM - Aplicación Web

## Descripción
Aplicación web para el llenado automático de documentos de FANGIO TELECOM.

## Despliegue en Render.com

### Configuración automática
Esta aplicación está configurada para desplegarse automáticamente en Render.com.

### Archivos de configuración
- `app_render.py` - Aplicación Flask principal
- `requirements.txt` - Dependencias de Python
- `render.yaml` - Configuración de Render.com

### URL de la aplicación
Una vez desplegada, la aplicación estará disponible en:
`https://fangio-telecom-app.onrender.com`

## Estructura del proyecto
```
├── app_render.py          # Aplicación principal
├── requirements.txt       # Dependencias
├── render.yaml           # Configuración Render
├── static/               # Archivos estáticos
├── templates/            # Plantillas HTML
├── site_survey/          # Archivos de ejemplo
└── llenado-automatico.html
```

## Tecnologías utilizadas
- Flask (Python web framework)
- Pandas (manipulación de datos)
- OpenPyXL (Excel)
- Render.com (hosting)
