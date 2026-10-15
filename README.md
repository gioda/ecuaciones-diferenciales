# Ecuaciones diferenciales: problemas, modelos y métodos

<p align="center">
  <img src="assets/readme-hero-ec-diff.png"
       alt="Ecuaciones diferenciales: problemas, modelos y métodos"
       width="100%">
</p>

**Información del libro**

[![Versión: 1.0](https://img.shields.io/badge/Versi%C3%B3n-1.0-596579?style=flat)](https://hdl.handle.net/20.500.14342/7219)
[![DAU: Handle](https://img.shields.io/badge/DAU-Handle-0B5C7A?style=flat)](https://hdl.handle.net/20.500.14342/7219)
[![PDF: Estudiante](https://img.shields.io/badge/PDF-Estudiante-167D8D?style=flat)](https://dau.url.edu/bitstream/20.500.14342/7219/4/Ecuaciones_diferenciales_Student.pdf)
[![Contenido: CC BY-SA 4.0](https://img.shields.io/badge/Contenido-CC_BY--SA_4.0-596579?style=flat)](LICENSE)
[![Código: MIT](https://img.shields.io/badge/C%C3%B3digo-MIT-596579?style=flat)](LICENSES/MIT.txt)
[![Idioma: español](https://img.shields.io/badge/Idioma-espa%C3%B1ol-596579?style=flat)](https://hdl.handle.net/20.500.14342/7219)
[![Python: 3](https://img.shields.io/badge/Python-3-3776AB?style=flat)](scripts/mallas.py)

CC BY-SA se aplica al contenido designado, con sus exclusiones; MIT, únicamente a los dos scripts públicos. Consulta los [ámbitos y exclusiones de las licencias](LICENSES.md).

**Actividad en GitHub**

[![Estrellas](https://img.shields.io/github/stars/gioda/ecuaciones-diferenciales?style=flat&label=Estrellas&color=596579)](https://github.com/gioda/ecuaciones-diferenciales/stargazers)
[![Forks](https://img.shields.io/github/forks/gioda/ecuaciones-diferenciales?style=flat&label=Forks&color=596579)](https://github.com/gioda/ecuaciones-diferenciales/forks)
[![Incidencias abiertas](https://img.shields.io/github/issues/gioda/ecuaciones-diferenciales?style=flat&label=Incidencias%20abiertas&color=596579)](https://github.com/gioda/ecuaciones-diferenciales/issues)
[![Contribuidores](https://img.shields.io/github/contributors/gioda/ecuaciones-diferenciales?style=flat&label=Contribuidores&color=596579)](https://github.com/gioda/ecuaciones-diferenciales/graphs/contributors)

Si no hay datos disponibles, los indicadores de actividad no representan un recuento de cero.

Libro de problemas en español para el aprendizaje y la práctica autónoma de las ecuaciones diferenciales, con aplicaciones en ciencias e ingeniería. La edición del estudiante reúne 370 ejercicios, respuestas de comprobación, 51 soluciones desarrolladas seleccionadas, nueve pistas y 42 recordatorios teóricos breves.

**Giovanni Dalmasso · Joaquín Menacho**. Departamento de Matemáticas y Analítica de Datos y Departamento de Ingeniería Industrial, respectivamente, IQS School of Engineering, Universitat Ramon Llull. Las afiliaciones son factuales y no implican aval institucional.

El recorrido comienza con modelos de primer orden y continúa con ecuaciones lineales, oscilaciones, transformada de Laplace y sistemas. Incluye Fourier, Sturm–Liouville y una introducción a las ecuaciones del calor, de ondas y de Laplace. Los problemas piden formular hipótesis, elegir métodos, comprobar resultados e interpretar soluciones. Las aproximaciones numéricas apoyan ese razonamiento.

## Libro del estudiante

**[Descargar el PDF del estudiante](books/ecuaciones-diferenciales-v1.0.0-DAU-7219.pdf)** · versión 1.0.0 · 219 páginas. [Vista de la cubierta](assets/cover-preview.png).

Esta es la edición definitiva del estudiante, publicada por Biblioteca IQS en el repositorio institucional DAU: [https://hdl.handle.net/20.500.14342/7219](https://hdl.handle.net/20.500.14342/7219).

SHA-256 del PDF: `62bfd4e5f084162f8d6e4826cf5b6f32efd9a4fa787e0853ea1dbe3802f35505`. Las fuentes corresponden a la revisión editorial aceptada r2 de la versión 1.0.0; esa revisión no cambia la numeración de versión del libro.

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

Dalmasso, G. y Menacho, J. (2026). *Ecuaciones diferenciales: problemas, modelos y métodos*. Edición del estudiante, versión 1.0.0. https://hdl.handle.net/20.500.14342/7219. Los datos de cita están en [CITATION.cff](CITATION.cff).

Repositorio de fuentes y apoyo: https://github.com/gioda/ecuaciones-diferenciales. Identificador de la edición del estudiante: [https://hdl.handle.net/20.500.14342/7219](https://hdl.handle.net/20.500.14342/7219).

## Bibliografía, atribuciones y licencias

Las nueve referencias aprobadas están normalizadas en [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md); los créditos y la declaración de uso de herramientas de IA, en [ATTRIBUTION.md](ATTRIBUTION.md). Imagen generada con inteligencia artificial bajo dirección de los autores.

Libro, fuentes LaTeX/TikZ, figuras educativas y documentación: [CC BY-SA 4.0](LICENSE), sobre los derechos disponibles. Software designado: [MIT](LICENSES/MIT.txt). Los retratos y las tipografías mantienen sus exclusiones o condiciones propias. [Alcance y exclusiones](LICENSES.md). La descripción de las imágenes generadas mediante IA no afirma derechos exclusivos sobre ellas.

## Organización

```text
books/       PDF del estudiante
src/         fuentes Student y activos de construcción
assets/      hero del README y vista de la cubierta
scripts/     construcción y ayuda numérica
LICENSES/    licencia del software designado
```

[SHA256SUMS.txt](SHA256SUMS.txt) identifica los archivos distribuidos.

## Derechos, atribuciones y erratas

Para comunicar erratas, utiliza [GitHub Issues](https://github.com/gioda/ecuaciones-diferenciales/issues) y la [plantilla de erratas](.github/ISSUE_TEMPLATE/errata.md). Indica la versión del PDF, el capítulo o sección, el número de ejercicio o la página y una explicación breve; puedes proponer una corrección. Las sugerencias y las cuestiones de atribución que puedan tratarse públicamente pueden comunicarse por la misma vía. Evita incluir datos personales o copias de material protegido de terceros.

GitHub Issues no es un canal confidencial para cuestiones de derechos. No publiques allí datos personales ni documentación reservada. Esta documentación no designa un canal privado para esa correspondencia.
