# Changelog
Todos los cambios notables de este proyecto se documentarán en este archivo.
El formato está basado en https://keepachangelog.com/es-ES/1.0.0/,
y este proyecto se adhiere a https://semver.org/spec/v2.0.0.html.

## [2.0.0] - 2026-11-11
### Added
- Nueva zona de cobertura insular (San Andrés) con recargo del 70%.
- Restricción de negocio: Los envíos a zonas insulares bloquean el uso de cupones promocionales.
- Suite completa automatizada con `pytest` (22 casos) cubriendo el 100% de los caminos independientes.
- Implementación de patrón de diseño Estrategia (Strategy) para aislar la lógica de recargos por zona.

### Changed
- **[BREAKING CHANGE]** Se eliminó el parámetro `flag` de la función `calc()` (SRP).
- Migración de "números mágicos" a un diccionario de configuración global `CONFIG`.

### Fixed
- DEF-01: Límite de peso máximo (PMAX) corregido de 50 a 45 kg.
- DEF-02: Error tipográfico severo en la tarifa del tramo 3 (corregido de 900 a 9000).
- DEF-03: Lógica de recargo de fin de semana incompleta (`d >= 6`).
- DEF-04: Estructura de descuentos condicionales ajustada a `if/elif`.
- DEF-05: Redondeo matemático truncado corregido a múltiplo más cercano.
- DEF-06: Vulnerabilidad de cupones inexistentes; ahora lanzan explícitamente `ValueError`.