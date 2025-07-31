# Análisis de Enlaces Microondas - Documentación Técnica

## 📡 Descripción General

El análisis de microondas implementado en el sistema utiliza modelos de propagación basados en **ITU-R P.530** para evaluar la viabilidad y rendimiento de enlaces de radiofrecuencia. Este análisis proporciona métricas técnicas avanzadas y recomendaciones específicas para optimizar el diseño de redes microondas.

## 🔧 Parámetros de Configuración

### Clima
- **Tropical**: Alta humedad, lluvias intensas
- **Temperate**: Clima moderado, condiciones estándar
- **Arid**: Baja humedad, desierto
- **Cold**: Clima frío, nieve, hielo

### Parámetros Técnicos
- **Disponibilidad Objetivo**: Porcentaje de uptime deseado (ej: 99.9%)
- **Potencia TX**: Potencia de transmisión en dBm
- **Sensibilidad RX**: Sensibilidad del receptor en dBm

## 📊 Métricas Calculadas

### 1. Path Loss (Pérdidas de Propagación)
```
Path Loss = Lfs + Lclima - Laltura
```
- **Lfs**: Pérdidas en espacio libre
- **Lclima**: Pérdidas adicionales por condiciones climáticas
- **Laltura**: Ganancia por altura de antenas

### 2. SNR (Signal-to-Noise Ratio)
```
SNR = Potencia Recibida - Ruido Térmico
```
- **Ruido Térmico**: -174 dBm/Hz + 10*log10(Ancho de Banda)

### 3. BER (Bit Error Rate)
```
BER = 0.5 * erfc(sqrt(2 * 10^(SNR/10)) / sqrt(2))
```
- Calculado para modulación QPSK
- Función de error complementaria (erfc)

### 4. Zona de Fresnel
```
Fresnel = 17.3 * sqrt(Distancia / (4 * Frecuencia))
```
- Radio de la primera zona de Fresnel
- Importante para el clearance de obstáculos

### 5. Margen de Fading
```
Fade Margin = Distancia * Frecuencia * Factor_Clima
```
- Margen adicional para compensar desvanecimientos

### 6. Disponibilidad Real
```
Disponibilidad = 99.9% - Reducción_Clima
```
- Disponibilidad calculada vs objetivo

## 🎯 Criterios de Evaluación

### Estado del Enlace
- **Excelente**: Margen > 20dB, Disponibilidad ≥ Objetivo, SNR > 20dB
- **Bueno**: Margen > 10dB, Disponibilidad ≥ 99.5%, SNR > 15dB
- **Aceptable**: Margen > 0dB, SNR > 10dB
- **Crítico**: Margen ≤ 0dB o SNR ≤ 10dB

### Factores de Clima (ITU-R P.530)

#### Path Loss Adicional
| Clima | Lluvia | Humedad | Temperatura |
|-------|--------|---------|-------------|
| Tropical | 0.15 | 0.08 | 0.05 |
| Temperate | 0.10 | 0.05 | 0.03 |
| Arid | 0.05 | 0.02 | 0.08 |
| Cold | 0.08 | 0.03 | 0.12 |

#### Fade Margin
| Clima | Factor |
|-------|--------|
| Tropical | 0.12 |
| Temperate | 0.08 |
| Arid | 0.05 |
| Cold | 0.10 |

## 🔍 Detección de Interferencias

### Bandas de Frecuencia Analizadas
- **6, 8, 10 GHz**: Bandas bajas, mayor atenuación
- **15, 18, 23, 26 GHz**: Bandas medias, balanceadas
- **38, 60, 80 GHz**: Bandas altas, sensible a lluvia

### Criterios de Alerta
- Frecuencia < 15 GHz: "Banda baja - mayor atenuación"
- Frecuencia > 38 GHz: "Banda alta - sensible a lluvia"
- Distancia > 50 km: "Distancia crítica para frecuencia"

## 💡 Sistema de Recomendaciones

### Recomendaciones Automáticas
1. **Margen ≤ 0dB**: "Aumentar potencia TX o sensibilidad RX"
2. **SNR ≤ 10dB**: "Mejorar SNR con antenas de mayor ganancia"
3. **Disponibilidad < Objetivo**: "Considerar redundancia o cambio de frecuencia"
4. **Interferencias detectadas**: Alertas específicas por tipo de interferencia

### Visualización
- **Botón de alerta**: Muestra número de recomendaciones
- **Modal detallado**: Lista completa de recomendaciones por enlace
- **Iconos de estado**: Verde (✓), Amarillo (⚠️), Rojo (❌)

## 📈 Gráficos y Visualizaciones

### Gráfico de Rendimiento
- **Tipo**: Gráfico de barras
- **Datos**: Margen de cada enlace
- **Colores**: Verde (Excelente), Azul (Bueno), Amarillo (Aceptable)
- **Actualización**: Automática después del análisis

### Estadísticas Generales
- **Enlaces Viables**: Número de enlaces con margen positivo
- **Enlaces Críticos**: Número de enlaces con problemas
- **Disponibilidad Promedio**: Media de disponibilidad de todos los enlaces

## 🚀 Cómo Usar el Análisis

### 1. Configurar Parámetros
1. Seleccionar clima apropiado para la región
2. Establecer disponibilidad objetivo deseada
3. Configurar potencia TX del equipo
4. Definir sensibilidad RX del receptor

### 2. Ejecutar Análisis
1. Hacer clic en "Analizar Enlaces"
2. Revisar estadísticas generales
3. Examinar tabla detallada por enlace
4. Verificar recomendaciones específicas

### 3. Interpretar Resultados
1. **Enlaces Excelentes**: No requieren cambios
2. **Enlaces Buenos**: Monitorear periódicamente
3. **Enlaces Aceptables**: Considerar mejoras menores
4. **Enlaces Críticos**: Requieren intervención inmediata

### 4. Aplicar Recomendaciones
1. Revisar recomendaciones por enlace crítico
2. Implementar mejoras sugeridas
3. Re-ejecutar análisis después de cambios
4. Documentar modificaciones realizadas

## 🔬 Base Técnica

### Estándares Utilizados
- **ITU-R P.530**: Propagación de ondas de radio
- **ITU-R P.838**: Atenuación específica por lluvia
- **ITU-R P.840**: Atenuación por nubes y niebla

### Modelos Matemáticos
- **Path Loss**: Modelo de espacio libre + factores climáticos
- **Fade Margin**: Modelo estadístico de desvanecimiento
- **BER**: Función de error para QPSK
- **Fresnel**: Cálculo de zona de Fresnel

## 📋 Limitaciones y Consideraciones

### Limitaciones del Modelo
- No considera obstáculos específicos del terreno
- Asume condiciones atmosféricas promedio
- No incluye efectos de multipath complejos
- Basado en modelos estadísticos

### Recomendaciones de Uso
- Usar como herramienta de diseño inicial
- Complementar con mediciones de campo
- Considerar factores locales específicos
- Actualizar parámetros según condiciones reales

## 🔄 Monitoreo en Tiempo Real

### Métricas Monitoreadas
- **RSSI**: Potencia de señal recibida
- **SNR**: Relación señal-ruido
- **Temperatura**: Temperatura del equipo
- **Uptime**: Tiempo de funcionamiento
- **Alertas**: Notificaciones automáticas

### Actualización de Datos
- **Frecuencia**: Cada 5 segundos
- **Fuente**: Simulación de datos reales
- **Visualización**: Tarjetas individuales por enlace
- **Alertas**: Notificaciones en tiempo real

---

*Documentación actualizada para la versión 4.0 del Sistema de Enlaces Microondas Fangio Telecom* 