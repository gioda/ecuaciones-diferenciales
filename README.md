# Ecuaciones diferenciales: problemas, modelos y métodos

<p align="center">
  <img src="assets/readme-hero-ec-diff.png"
       alt="Ecuaciones diferenciales: problemas, modelos y métodos"
       width="100%">
</p>

Libro de problemas en español para el aprendizaje y la práctica autónoma de las ecuaciones diferenciales, con aplicaciones en ciencias e ingeniería. La edición del estudiante reúne 370 ejercicios, respuestas de comprobación, 51 soluciones desarrolladas seleccionadas, nueve pistas y 42 recordatorios teóricos breves.

**Giovanni Dalmasso · Joaquín Menacho**. Departamento de Matemáticas y Analítica de Datos y Departamento de Ingeniería Industrial, respectivamente, IQS School of Engineering, Universitat Ramon Llull. Las afiliaciones son factuales y no implican aval institucional.

El recorrido comienza con modelos de primer orden y continúa con ecuaciones lineales, oscilaciones, transformada de Laplace y sistemas. Incluye Fourier, Sturm–Liouville y una introducción a las ecuaciones del calor, de ondas y de Laplace. Los problemas piden formular hipótesis, elegir métodos, comprobar resultados e interpretar soluciones. Las aproximaciones numéricas apoyan ese razonamiento.

## Libro del estudiante

**[Descargar el PDF del estudiante](books/ecuaciones-diferenciales-v1.0.0-DAU-provisional.pdf)** · versión 1.0.0 · 218 páginas. [Vista de la cubierta](assets/cover-preview.png).

Esta copia provisional está preparada para Biblioteca IQS. El PDF contiene por ahora el marcador [HANDLE DAU PENDIENTE]; Biblioteca creará el registro provisional. Una vez asignado el Handle, los autores entregarán el PDF definitivo para sustituirlo en el mismo registro. El repositorio permanece privado durante esta preparación.

## Fuentes y construcción

[src/](src/) contiene las fuentes LaTeX, las figuras y los activos necesarios para reproducir esta edición del estudiante. [BUILD.md](BUILD.md) detalla LuaLaTeX, las fuentes tipográficas, los paquetes y los comandos. Desde la raíz:

```sh
sh scripts/build_publication.sh build
```

El resultado se genera en src/build/main.pdf. La bibliografía se incluye directamente mediante references.tex; no necesita BibTeX ni Biber.

## Ayuda numérica

[scripts/mallas.py](scripts/mallas.py) acompaña los dos ejercicios que remiten a una ayuda para mallas largas. Requiere Python 3 y únicamente su biblioteca estándar:

```sh
python3 scripts/mallas.py E0049
python3 scripts/mallas.py E0068
```

La salida es CSV. Las hipótesis, la comprobación y la interpretación forman parte del trabajo del estudiante.

## Cita

Dalmasso, G. y Menacho, J. (2026). *Ecuaciones diferenciales: problemas, modelos y métodos*. Edición del estudiante, versión 1.0.0. Los datos de cita están en [CITATION.cff](CITATION.cff).

Repositorio de fuentes y apoyo: https://github.com/gioda/ecuaciones-diferenciales. El identificador institucional se añadirá cuando Biblioteca lo asigne.

## Bibliografía, atribuciones y licencias

Las nueve referencias aprobadas están normalizadas en [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md); los créditos, en [ATTRIBUTION.md](ATTRIBUTION.md). Imagen generada con inteligencia artificial bajo dirección de los autores.

Libro, fuentes LaTeX/TikZ, figuras educativas y documentación: [CC BY-SA 4.0](LICENSE), sobre los derechos disponibles. Software designado: [MIT](LICENSES/MIT.txt). Los retratos y las tipografías mantienen sus exclusiones o condiciones propias. [Alcance y exclusiones](LICENSES.md). La descripción de las imágenes generadas mediante IA no afirma derechos exclusivos sobre ellas.

## Organización

```text
books/       PDF del estudiante
src/         fuentes Student y activos de construcción
assets/      hero del README y vista de la cubierta
scripts/     construcción y ayuda numérica
LICENSES/    licencia del software designado
```

SHA256SUMS.txt identifica los archivos distribuidos. Para comunicar una errata, indica la versión del PDF, el capítulo, el ejercicio, la página y una explicación breve. Evita incluir datos personales o copias de material protegido de terceros.

## Derechos, atribuciones y erratas

Canal público para consultas sobre derechos, atribuciones y erratas: [CONTACTO PÚBLICO PARA DERECHOS Y ERRATAS PENDIENTE].

Esta preparación local conserva el marcador DAU indicado arriba. El canal de contacto y el identificador institucional deben completarse antes de la publicación definitiva.
