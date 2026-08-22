\# Plan de Gestión de Configuración de Software (PlanSCM)



**\*\*Materia:\*\*** Ingeniería y Calidad de Software

**\*\*Grupo**: 3

**\*\*Repositorio:** ISW\_Repo\_G3

**\*\*URL del repositorio:\*\*** https://github.com/angela2022A/ISW\_Repo\_G3

**\*\*Integrantes:\*\*** 



* Bisio Juan Martin - 401571
* Caffaratti, Máximo David - 401609
* Crovato Agustin - 403878 
* Lavini Alejandro Raul - 402745
* Fava, Augusto - 95058
* Giorgi, Lorenzo - 403852
* Maldonado Alberich Gonzalo - 404483
* Mansur, Nicolas - 402774
* Martínez, Joaquín - 96110
* Matos, Kevin Lionel - 400734
* Pereyra, Santiago - 404539
* Portalupi Matías - 403916
* Ques, Fermín - 402066
* Quintana Tomás - 402992
* Tarifa, Angela - 94599





**## 1. Objetivo**



Definir los ítems de configuración de software (ICS) que se gestionarán durante el cursado de la materia, la regla de nombrado que se aplicará a cada uno, y el criterio utilizado para establecer líneas base a lo largo del proyecto.



**## 2. Estructura del repositorio**



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

```



**## 3. Ítems de configuración identificados**



\### 3.1 Material Bibliográfico (`Material\_Bibliografico/`)

Apuntes teóricos entregados por la cátedra, uno por cada unidad de la materia.



| Ítem | Descripción |

|---|---|

| U1\_Material-IngenieriaSoftware.md | Conceptos generales de Ingeniería de Software (Unidad 1) |

| U2\_Material-LeanAgileProducto.md | Frameworks Lean y Agile aplicados a producto (Unidad 2) |

| U3\_Material-GestionSoftwareProducto.md | Gestión del software como producto (Unidad 3) |

| U4\_Material-SCMCalidadProducto.md | Gestión de configuración y calidad de producto (Unidad 4) |



\### 3.2 Prácticos de clase (`Practicos/0X\_NombreSubcarpeta/`)

Entregables resueltos en cada clase práctica, uno por carpeta numerada según el orden de cursado.



| Ítem | Descripción |

|---|---|

| 01\_UserStories/Clase\_Practico\_UserStories.md | Redacción de historias de usuario |

| 02\_Estimaciones/Clase\_Practico\_Estimaciones.md | Técnicas de estimación de tareas |

| 03\_EstimacionesMVP/Clase\_Practico\_EstimacionesMVP.md | Estimación aplicada a un MVP |

| 04\_HerramientaSCM/Clase\_Practico\_HerramientaSCM.md | Implementación de la herramienta de SCM (este TP) |

| 05\_UsoRepositorio/Clase\_Practico\_UsoRepositorio.md | Uso práctico del repositorio de configuración |

| 06\_TDD/Clase\_Practico\_TDD.md | Desarrollo guiado por pruebas |

| 07\_SCRUM\_Aplicacion/Clase\_Practico\_SCRUMAplicacion.md | Aplicación del marco de trabajo SCRUM |

| 08\_TestingCajaNegra\_Parte1/Clase\_Practico\_TestingCajaNegra-Parte1.md | Testing de caja negra, primera parte |

| 09\_TestingCajaNegra\_Parte2/Clase\_Practico\_TestingCajaNegra-Parte2.md | Testing de caja negra, segunda parte |

| 10\_Kanban\_Aplicacion/Clase\_Practico\_KanbanAplicacion.md | Aplicación del método Kanban |

| 11\_SCRUM\_Retrospectiva/Clase\_Practico\_SCRUMRetrospectiva.md | Retrospectiva de sprint en SCRUM |

| 12\_DesignThinking\_Publicidad/Clase\_Practico\_DesignThinking-Publicidad.md | Design Thinking aplicado a un caso de publicidad |

| 13\_SCRUM\_ReleaseSprint/Clase\_Practico\_SCRUMReleaseSprint.md | Planificación de release sprint en SCRUM |



\### 3.3 Investigaciones (`Investigaciones/Nombre\_subcarpeta/`)

Trabajos de investigación grupal preparados para exposición en clase.



| Ítem | Descripción |

|---|---|

| Despliegue\_Producto/Exposicion\_Investigacion\_DespliegueProducto.md | Investigación sobre estrategias de despliegue de producto |

| Frameworks\_LeanAgile/Exposicion\_Investigacion\_FrameworksLeanAgile.md | Investigación sobre frameworks Lean y Agile |



\### 3.4 Evaluables (`Evaluables/`)

Instancias de evaluación parcial de la materia.



| Ítem | Descripción |

|---|---|

| Parcial\_Evaluable\_Primero.md | Primer parcial de la materia |

| Parcial\_Evaluable\_Segundo.md | Segundo parcial de la materia |



\### 3.5 Gestión del proyecto (`PlanSCM/`)

Documentación de gestión de configuración del propio repositorio.



| Ítem | Descripción |

|---|---|

| Estrategia\_PlanSCM.md | Definición de ítems de configuración, regla de nombrado y criterio de línea base |



**## 4. Regla de nombrado de ítems de configuración**



**### 4.1 Nombrado de carpetas**



Las carpetas se nombran en formato `PascalCase` o palabras separadas por guion bajo (`\_`), sin espacios ni tildes. Las carpetas de `Practicos/` llevan además un prefijo numérico de dos dígitos que indica el orden de temas dados durante el transcurso de la cursada:



```

0X\_NombreDelPractico/

```



Ejemplo: `04\_HerramientaSCM/`, `08\_TestingCajaNegra\_Parte1/`



**### 4.2 Nombrado de archivos**



Se utiliza la convención general:



```

TIPO\_NombreDelItem.md

```



Donde:



**| Elemento | Descripción |**

|---|---|

| **\*\*TIPO\*\*** | Prefijo que identifica la categoría del ítem de configuración |

| **\*\*Separador TIPO–Nombre\*\*** | Guion bajo (`\_`), siempre |

| **\*\*NombreDelItem\*\*** | Nombre descriptivo del contenido, en formato `PascalCase`; si tiene varias palabras o partes, se separan con guion medio (`-`) |

| **\*\*Extensión\*\*** | `.md` para todo el contenido textual del repositorio (Markdown) |



**### 4.3 Prefijos TIPO según categoría**



**| Categoría | Prefijo TIPO | Ejemplo completo |**

|---|---|---|

| Material bibliográfico | **`U1`, `U2`, `U3`, `U4**` (según unidad) | `U1\_Material-IngenieriaSoftware.md` |

| Prácticos de clase | `**Clase**\_Practico` | `Clase\_Practico-UserStories.md` |

| Investigaciones | `**Exposicion**\_Investigacion` | `Exposicion\_Investigacion-DespliegueProducto.md` |

| Evaluables | `**Parcial**\_Evaluables` | `Parcial\_Evaluables-Primero.md` |

| Gestión del proyecto | `**Estrategia**` | `Estrategia\_PlanSCM.md` |





**## 5. Criterio de creación de línea base**



Se establecerá una línea base (tag) en el repositorio en los siguientes momentos:



1\. Al finalizar la carga de una unidad completa de material bibliográfico y sus prácticos asociados.

2\. Al momento de entrega de cada TP evaluable por la cátedra (como el presente Práctico 4).

3\. Antes de una exposición o evaluación parcial, dejando congelado el estado del contenido presentado.



**Cada línea base se identifica con el formato:**



```

**linea-base-N**

```



y se documenta con un mensaje que indica qué contenido incluye y la fecha.



**\*\*Ejemplo de comando (Git):\*\***

```bash

**git tag -a** **linea-base-1** -m "Línea base tras completar practico 4 de la unidad 3 - SCM"

**git push origin linea-base-1**

```



**## 6. Control de acceso**



El repositorio es de acceso público, permitiendo su consulta sin necesidad de autenticación. Cada integrante del grupo cuenta con una cuenta de usuario propia para realizar sus aportes (commits) de forma identificable para GitHub de sus avances y cambios generados durante el cursado.

