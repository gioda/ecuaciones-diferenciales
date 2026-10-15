# Construcción y ayuda numérica

## Requisitos

LuaLaTeX y una distribución TeX que incluya babel (español), fontspec, amsmath, amssymb, unicode-math, geometry, graphicx, xcolor, enumitem, needspace, microtype, fancyhdr, hyperref y TikZ. Se emplean TeX Gyre Pagella, TeX Gyre Heros, TeX Gyre Pagella Math y Latin Modern Mono. La construcción de referencia utiliza TeX Live 2025, LuaHBTeX 1.22.0. Un intérprete POSIX sh ejecuta el script de construcción.

## PDF del estudiante

Desde la raíz del repositorio:

```sh
sh scripts/build_publication.sh build
```

El script adapta el método existente: entra en src/, crea src/build/ y sus cachés locales, y ejecuta tres pasadas de LuaLaTeX sobre main.tex con --no-shell-escape, -halt-on-error y -recorder. Resultado: src/build/main.pdf. El nombre opcional del directorio debe contener solo letras, números, guiones o guiones bajos. No se necesita BibTeX/Biber: references.tex contiene la bibliografía. Las figuras incluidas ya están preparadas; no hay una etapa de generación adicional.

Las fuentes y activos requeridos están en src/. Los archivos .aux, .toc, .out y las cachés se generan durante la construcción. Las fuentes tipográficas y paquetes pertenecen a la distribución TeX y conservan sus propias licencias. Los registros .log y .fls permiten comprobar advertencias y entradas; no forman parte del material distribuido.

El PDF de books/ es la edición definitiva del estudiante v1.0.0, revisión editorial r2, publicada por Biblioteca IQS en el repositorio institucional DAU: https://hdl.handle.net/20.500.14342/7219.

Archivo distribuido: books/ecuaciones-diferenciales-v1.0.0-DAU-7219.pdf. SHA-256: `62bfd4e5f084162f8d6e4826cf5b6f32efd9a4fa787e0853ea1dbe3802f35505`.

La reproducción de referencia conserva todas las páginas, textos, objetos, destinos y enlaces. Al comparar los bytes se normalizan exclusivamente /CreationDate, /ModDate y el /ID del tráiler PDF, tal como se documentó en la verificación anterior. No se permiten otras normalizaciones de contenido. SHA256SUMS.txt identifica las copias distribuidas; el hash bruto de una reconstrucción puede variar por esos metadatos.

## Ayuda numérica

Python 3, sin paquetes adicionales. Desde la raíz:

```sh
python3 scripts/mallas.py E0049 > E0049.csv
python3 scripts/mallas.py E0068 > E0068.csv
```

El primer comando genera la malla RK4 del sistema de poblaciones; el segundo, las tres mallas de Euler de la ecuación de tercer orden. Las tablas CSV apoyan las hipótesis, el razonamiento y la interpretación del estudiante.

## Integridad

```sh
# macOS
shasum -a 256 -c SHA256SUMS.txt
# GNU/Linux
sha256sum -c SHA256SUMS.txt
```
