# Aplicación de Llenado Automático

Esta aplicación Flask permite llenar automáticamente plantillas de Excel con datos de una base de datos.

## Cómo iniciar el servidor

### Opción 1: Usando el archivo batch (más fácil)
1. Haz doble clic en `iniciar_servidor.bat`
2. El servidor se iniciará automáticamente
3. Abre tu navegador y ve a: http://127.0.0.1:5000

### Opción 2: Usando PowerShell
1. Abre PowerShell en esta carpeta
2. Ejecuta: `.\iniciar_servidor.ps1`
3. El servidor se iniciará automáticamente

### Opción 3: Manualmente
1. Abre una terminal en esta carpeta
2. Ejecuta: `python app.py`
3. El servidor estará disponible en: http://127.0.0.1:5000

## Solución de problemas

### Si el servidor se cierra automáticamente:
1. Verifica que Python esté instalado: `python --version`
2. Verifica que las dependencias estén instaladas:
   ```
   pip install flask pandas xlwings pywin32 openpyxl
   ```
3. Asegúrate de que todos los archivos estén en la misma carpeta

### Si hay errores de dependencias:
```bash
pip install --upgrade flask pandas xlwings pywin32 openpyxl python-docx dataframe-image
```

## Estructura de la aplicación

- **Página principal** (`/`) - Menú de opciones
- **Diseño de Solución** (`/diseño_solucion`) - Llenado automático de plantillas
- **Site Survey** (`/site_survey`) - Formulario de estudio de sitio (en construcción)
- **Reporte de Planeación** (`/reporte_planeacion`) - Reportes de planeación (en construcción)

## Archivos necesarios

- `app.py` - Servidor principal
- `llenado-automatico.html` - Formulario HTML
- `templates/index.html` - Página de inicio
- `base de datos.xlsx` - Base de datos con la información
- `hoja de datos .xlsx` - Plantilla a llenar

## Uso

1. Inicia el servidor usando cualquiera de los métodos anteriores
2. Abre tu navegador en http://127.0.0.1:5000
3. Haz clic en "Diseño de Solución" para acceder al llenado automático
4. Sube tu base de datos y plantilla
5. Llena el formulario con las imágenes y archivos necesarios
6. Descarga el archivo procesado

## Detener el servidor

Presiona `Ctrl+C` en la terminal donde está ejecutándose el servidor. 