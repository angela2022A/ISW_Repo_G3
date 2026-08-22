\# Plan de Gestión de Configuración de Software (PlanSCM)



\*\*Materia:\*\* Ingeniería de Software

\*\*Grupo:\*\* G3

\*\*Repositorio:\*\* ISW\_Repo\_G3

\*\*URL del repositorio:\*\* https://github.com/angela2022A/ISW\_Repo\_G3

\*\*Integrantes:\*\* \_(completar con nombres y usuarios de cada integrante)\_



\---



\## 1. Objetivo



Definir los ítems de configuración de software (ICS) que se gestionarán durante el cursado de la materia, la regla de nombrado que se aplicará a cada uno, y el criterio utilizado para establecer líneas base a lo largo del proyecto.



\## 2. Estructura del repositorio



ISW\_Repo\_G3/

├── Material\_Bibliografico/

├── Practicos/

│   ├── 01\_UserStories/

│   ├── 02\_Estimaciones/

│   ├── 03\_EstimacionesMVP/

│   ├── 04\_HerramientaSCM/

│   ├── 05\_UsoRepositorio/

│   ├── 06\_TDD/

│   ├── 07\_SCRUM\_Aplicacion/

│   ├── 08\_TestingCajaNegra\_Parte1/

│   ├── 09\_TestingCajaNegra\_Parte2/

│   ├── 10\_Kanban\_Aplicacion/

│   ├── 11\_SCRUM\_Retrospectiva/

│   ├── 12\_DesignThinking\_Publicidad/

│   └── 13\_SCRUM\_ReleaseSprint/

├── Investigaciones/

│   ├── Despliegue\_Producto/

│   └── Frameworks\_LeanAgile/

├── Evaluables/

└── PlanSCM/



Cada carpeta agrupa un tipo de ítem de configuración según su naturaleza (material teórico, entregables prácticos, investigaciones, evaluaciones y documentación de gestión).



\## 3. Ítems de configuración identificados



| Categoría | Carpeta | Descripción |

|---|---|---|

| Material bibliográfico | Material\_Bibliografico/ | Apuntes y material teórico entregado por la cátedra, por unidad |

| Prácticos de clase | Practicos/0X\_Nombre/ | Entregables de cada práctico realizado en clase |

| Investigaciones | Investigaciones/Nombre/ | Trabajos de investigación e exposiciones grupales |

| Evaluables | Evaluables/ | Parciales y evaluaciones de la materia |

| Gestión del proyecto | PlanSCM/ | Documentación de gestión de configuración del repositorio |



\## 4. Regla de nombrado de ítems de configuración



Se utiliza la convención:



TIPO\_Nombre-del-item.md



Donde:

\- TIPO: identifica la naturaleza del archivo (U1, U2... para material bibliográfico por unidad; Clase\_Practico para entregables de clase; Exposicion\_Investigacion para investigaciones; Parcial\_Evaluables para evaluaciones; Estrategia para documentos de gestión).

\- Nombre-del-item: nombre descriptivo corto del contenido, sin espacios (se usa guion o guion bajo como separador).

\- Extensión: .md para todo el contenido textual del repositorio.



Ejemplos aplicados:

\- U1\_Material\_IngenieriaSoftware.md

\- Clase\_Practico-UserStories.md

\- Exposicion\_Investigacion-DespliegueProducto.md

\- Parcial\_Evaluables-Primero.md

\- Estrategia-PlanSCM.md



\## 5. Criterio de creación de línea base



Se establecerá una línea base (tag) en el repositorio en los siguientes momentos:



1\. Al finalizar la carga de una unidad completa de material bibliográfico y sus prácticos asociados.

2\. Al momento de entrega de cada TP evaluable por la cátedra (como el presente Práctico 4).

3\. Antes de una exposición o evaluación parcial, dejando congelado el estado del contenido presentado.



Cada línea base se identifica con el formato:



linea-base-N



y se documenta con un mensaje que indica qué contenido incluye y la fecha.



Ejemplo de comando (Git):

git tag -a linea-base-1 -m "Línea base tras completar Unidad 3 - SCM"

git push origin linea-base-1



\## 6. Control de acceso



El repositorio es de acceso público, permitiendo su consulta sin necesidad de autenticación. Cada integrante del grupo cuenta con una cuenta de usuario propia para realizar sus aportes (commits) de forma identificable.

