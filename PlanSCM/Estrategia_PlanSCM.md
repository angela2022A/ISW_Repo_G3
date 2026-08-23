Plan de Gestion de Configuracion de Software (PlanSCM)

Materia: Ingenieria y Calidad de Software

Grupo: 3

Repositorio: ISW_Repo_G3

URL del repositorio: https://github.com/angela2022A/ISW_Repo_G3

Integrantes:
- Bisio Juan Martin - 401571
- Caffaratti, Maximo David - 401609
- Crovato Agustin - 403878
- Lavini Alejandro Raul - 402745
- Fava, Augusto - 95058
- Giorgi, Lorenzo - 403852
- Maldonado Alberich Gonzalo - 404483
- Mansur, Nicolas - 402774
- Martinez, Joaquin - 96110
- Matos, Kevin Lionel - 400734
- Pereyra, Santiago - 404539
- Portalupi Matias - 403916
- Ques, Fermin - 402066
- Quintana Tomas - 402992
- Tarifa, Angela - 94599


1. Objetivo

Definir los items de configuración de software (ICS) que se gestionaran durante el cursado de la materia, la regla de nombrado que se aplicara a cada uno, y el criterio utilizado para establecer líneas base a lo largo del proyecto.


2. Estructura del repositorio

ISW_Repo_G3/
├── Material_Bibliografico/
├── Practicos/
│   ├── 01_UserStories/
│   ├── 02_Estimaciones/
│   ├── 03_EstimacionesMVP/
│   ├── 04_HerramientaSCM/
│   ├── 05_UsoRepositorio/
│   ├── 06_TDD/
│   ├── 07_SCRUM_Aplicacion/
│   ├── 08_TestingCajaNegra_Parte1/
│   ├── 09_TestingCajaNegra_Parte2/
│   ├── 10_Kanban_Aplicacion/
│   ├── 11_SCRUM_Retrospectiva/
│   ├── 12_DesignThinking_Publicidad/
│   └── 13_SCRUM_ReleaseSprint/
├── Investigaciones/
│   ├── Despliegue_Producto/
│   └── Frameworks_LeanAgile/
├── Evaluables/
└── PlanSCM/

--------------------------------------------------

3. Items de configuración identificados

3.1 Material Bibliografico (Material_Bibliografico/)
Apuntes teóricos entregados por la catedra, uno por cada unidad de la materia.

| Item | Descripción |
|---|---|
| U1_Material_IngenieriaSoftware.md | Conceptos generales de Ingeniería de Software (Unidad 1) |
| U2_Material_LeanAgileProducto.md | Frameworks Lean y Agile aplicados a producto (Unidad 2) |
| U3_Material_GestionSoftwareProducto.md | Gestión del software como producto (Unidad 3) |
| U4_Material_SCMCalidadProducto.md | Gestión de configuración y calidad de producto (Unidad 4) |

3.2 Practicos de clase (Practicos/0X_NombreSubcarpeta/)
Entregables resueltos en cada clase practica, uno por carpeta numerada según el orden de dictado.

| Item | Descripción |
|---|---|
| 01_UserStories/Clase_Practico_UserStories.md | Redacción de historias de usuario |
| 02_Estimaciones/Clase_Practico_Estimaciones.md | Técnicas de estimación de tareas |
| 03_EstimacionesMVP/Clase_Practico_EstimacionesMVP.md | Estimación aplicada a un MVP |
| 04_HerramientaSCM/Clase_Practico_HerramientaSCM.md | Implementación de la herramienta de SCM (este TP) |
| 05_UsoRepositorio/Clase_Practico_UsoRepositorio.md | Uso practico del repositorio de configuración |
| 06_TDD/Clase_Practico_TDD.md | Desarrollo guiado por pruebas |
| 07_SCRUM_Aplicacion/Clase_Practico_SCRUM_Aplicacion.md | Aplicación del marco de trabajo SCRUM |
| 08_TestingCajaNegra_Parte1/Clase_Practico_TestingCajaNegra_Parte1.md | Testing de caja negra, primera parte |
| 09_TestingCajaNegra_Parte2/Clase_Practico_TestingCajaNegra_Parte2.md | Testing de caja negra, segunda parte |
| 10_Kanban_Aplicacion/Clase_Practico_Kanban_Aplicacion.md | Aplicación del método Kanban |
| 11_SCRUM_Retrospectiva/Clase_Practico_SCRUM_Retrospectiva.md | Retrospectiva de sprint en SCRUM |
| 12_DesignThinking_Publicidad/Clase_Practico_DesignThinking_Publicidad.md | Design Thinking aplicado a un caso de publicidad |
| 13_SCRUM_ReleaseSprint/Clase_Practico_SCRUM_ReleaseSprint.md | Planificación de release sprint en SCRUM |

3.3 Investigaciones (Investigaciones/Nombre_subcarpeta/)
Trabajos de investigación grupal preparados para exposición en clase.

| Item | Descripción |
|---|---|
| Despliegue_Producto/Exposicion_Investigacion_DespliegueProducto.md | Investigación sobre estrategias de despliegue de producto |
| Frameworks_LeanAgile/Exposicion_Investigacion_FrameworksLeanAgile.md | Investigación sobre frameworks Lean y Agile |

3.4 Evaluables (Evaluables/)
Instancias de evaluación parcial de la materia.

| Item | Descripción |
|---|---|
| Parcial_Evaluable_Primero.md | Primer parcial de la materia |
| Parcial_Evaluable_Segundo.md | Segundo parcial de la materia |

3.5 Gestión del proyecto (PlanSCM/)

Documentación de gestión de configuración del propio repositorio.

| Item | Descripción |
|---|---|
| Estrategia_PlanSCM.md | Definición de items de configuración, regla de nombrado y criterio de linea base |


4. Regla de nombrado de items de configuración

4.1 Nombrado de carpetas

Las carpetas se nombran en formato Pascal-Case o palabras separadas por guion bajo (_), sin espacios ni tildes. Las carpetas de 'Practicos/' llevan además un prefijo numérico de dos dígitos que indica el orden de los temas dados durante el transcurso de la cursada:

0X_NombreDelPractico/

Ejemplo: 04_HerramientaSCM/, 08_TestingCajaNegra_Parte1/


4.2 Prefijos TIPO según categoría

| Categoría | Prefijo TIPO | Ejemplo completo |

| Material bibliográfico | U1, U2, U3, U4 (según unidad) | U1_Material_IngenieriaSoftware.md |
| Prácticos de clase | Clase_Practico | Clase_Practico_UserStories.md |
| Investigaciones | Exposicion_Investigacion | Exposicion_Investigacion_DespliegueProducto.md |
| Evaluables | Parcial_Evaluable | Parcial_Evaluable_Primero.md |
| Gestión del proyecto | Estrategia | Estrategia_PlanSCM.md |

Convenciones generales:
- El separador siempre es guion bajo (_).
- Los nombres van sin espacios ni tildes.
- Algunos de los items de configuración se versionan en formato Markdown (.md).

Criterios para nuevos avances:

Para la creación de nuevas configuraciones pueden aplicarse nuevos tipos de documentos o modificarse los actuales, siempre respetando la estructura general de esta regla de nombrado.


5. Criterio de creación de línea base

Se establecerá una línea base (tag) en el repositorio en los siguientes momentos:

1. Al finalizar la carga de una unidad completa de material bibliográfico y sus prácticos asociados.
2. Al momento de entrega de cada TP evaluable por la catedra (como el presente Practico 4).
3. Antes de una exposición o evaluación parcial, dejando congelado el estado del contenido presentado.

Cada línea base se identifica con el formato:

línea-base-N

y se documenta con un mensaje que indica que contenido incluye y la fecha.

Ejemplo de comando (Git):

git tag -a linea-base-1 -m "Linea base tras completar practico 4 de la unidad 4 - SCM"
git push origin linea-base-1



6. Control de acceso

El repositorio es de acceso publico, permitiendo su consulta sin necesidad de autenticación. Cada integrante del grupo cuenta con una cuenta de usuario propia para realizar sus aportes (commits) de forma identificable en GitHub, reflejando sus avances y cambios generados durante el cursado.

