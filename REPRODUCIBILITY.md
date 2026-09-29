# Ayuda numérica y verificación de archivos

El PDF es el archivo de lectura de esta distribución. Esta versión distribuye la ayuda numérica y la vista de cubierta; no incluye fuentes para reconstruir el PDF.

La ayuda requiere Python 3 y no necesita paquetes adicionales:

```sh
python3 computation/mallas.py E0049 > E0049.csv
python3 computation/mallas.py E0068 > E0068.csv
```

El primer comando genera la malla RK4 del sistema de poblaciones. El segundo genera tres mallas de Euler para el sistema equivalente a la ecuación de tercer orden. Los resultados se escriben en CSV, con cabecera de variables.

Para comprobar que los archivos descargados coinciden con los de la versión, utiliza el manifiesto `SHA256SUMS.txt`:

```sh
# macOS
shasum -a 256 -c SHA256SUMS.txt
# GNU/Linux
sha256sum -c SHA256SUMS.txt
```

El manifiesto identifica los archivos distribuidos; no sustituye la comprobación matemática de un resultado.
