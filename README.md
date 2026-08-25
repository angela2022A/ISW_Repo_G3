# ISW_Repo_G3

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=500&color=FF2C2C&vCenter=true&center=true&width=900&lines=Ingenier%C3%ADa+de+Software+2026" alt="Typing SVG" />
</p>

---

🏫 Universidad: Universidad Tecnológica Nacional, Facultad Regional Córdoba </br>
🎓 Carrera: Ingeniería en Sistemas de Información </br>
📚 Grupo: N°3 </br>
✏️ Curso: 4K2 </br>
📌 Tema: SCM (Gestión de Configuración de Software)

**Docentes:**
- Ing. Cecilia Massano
- Ing. Meles, Judith
- Ezequiel Izaguirre
- Marcos Pomenich

---

## Integrantes

| Apellido, Nombre | Legajo |
|--------|----------|
|Bisio, Juan Martín|401571|
|Caffaratti, Máximo David|401609|
|Crovato, Agustín|403878|
|Lavini, Alejandro Raúl|402745|
|Fava, Augusto|95058|
|Giorgi, Lorenzo|403852|
|Maldonado Alberich, Gonzalo|404483|
|Mansur, Nicolás|402774|
|Martínez, Joaquín|96110|
|Matos, Kevin Lionel|400734|
|Pereyra, Santiago|404539|
|Portalupi, Matías|403916|
|Ques, Fermín|402066|
|Quintana, Tomás|402992|
|Tarifa, Angela|94599|

---

## Estructura general

```
ISW_Repo_G3/
├── 📂 Administracion_Materia/
├── 📂 Material_Bibliografico/
│   ├── 📂 Ingeniería_de_Software/
│   ├── 📂 SCM_Gestión_de_Configuración_de_Software/
│   ├── 📂 Testing_de_Software/
│   ├── 📂 Test_Driven_Development/
│   ├── 📂 Agilismo/
│   └── 📂 Lean_y_Kanban/
├── 📂 Presentaciones_Clases/
│   ├── 📂 Unidad_1/
│   ├── 📂 Unidad_2/
│   ├── 📂 Unidad_3/
│   └── 📂 Unidad_4/
├── 📂 Trabajos_Practicos_Grupales/
│   ├── 📂 TP04_SCM/
│   ├── 📂 TP06_Test_Driven_Development/
│   ├── 📂 TP07_Dinamica_Scrum/
│   ├── 📂 TP09_Testing/
│   ├── 📂 TP10_Retrospectiva/
│   ├── 📂 TP11_Design_Thinking/
│   └── 📂 Trabajo_Investigacion/
│       ├── 📂 Trabajo_Investigacion_Grupal_1/
│       └── 📂 Trabajo_Investigacion_Grupal_2/
├── 📂 Parciales/
│   ├── 📂 Parcial_01/
│   └── 📂 Parcial_02/
└── 📂 Documentacion_Gestion/
```

---

## Tipos de ítem de configuración

Se definieron cuatro tipos de ítem de configuración, elegidos de modo tal que cada uno se corresponda con una o más carpetas del repositorio y determine unívocamente dónde debe ubicarse cada ítem:

| Tipo | Descripción | Carpeta(s) asociada(s) |
|------|-------------|-------------------------|
|Administrativo|Documentación de gestión de la cursada, producida por la cátedra (programa, presentación institucional, lineamientos de TPs).|Administracion_Materia|
|Soporte|Material de referencia y de apoyo al cursado: bibliografía externa, presentaciones de clase y material de estudio para parciales.|Material_Bibliografico, Presentaciones_Clases, Parciales|
|Entregable|Resoluciones de Trabajos Prácticos grupales y del Trabajo de Investigación, producidas activamente por el grupo.|Trabajos_Practicos_Grupales|
|GestionSCM|Meta-documentación: describe cómo se gestiona la configuración del propio repositorio.|Documentacion_Gestion|

---

## Ítems de configuración

Cada fila define una familia de ítems de configuración, no un archivo puntual: los textos entre `< >` son placeholders que se completan según el ítem concreto, siguiendo el Glosario. Todos los nombres llevan el prefijo fijo `G3_` que identifica al grupo. Las ubicaciones son relativas a la raíz del repositorio público.

| Nombre del ítem de configuración | Regla de nombrado | Ubicación | Tipo |
|------|-------------|---------|-----|
|Presentación de Cátedra|`G3_ADM_PresCatedra.pdf`|`ISW_Repo_G3/Administracion_Materia`|Administrativo|
|Programa de la Materia|`G3_ADM_ProgramaMateria.pdf`|`ISW_Repo_G3/Administracion_Materia`|Administrativo|
|Lineamiento de Trabajos Prácticos Grupales|`G3_ADM_LineamientoTPs.docx`|`ISW_Repo_G3/Administracion_Materia`|Administrativo|
|Material de Apoyo para Parciales|`G3_PARC_MatApoyo_<NN>.pdf`|`ISW_Repo_G3/Parciales/Parcial_<NN>`|Soporte|
|Material Bibliográfico|`G3_BIB_<UNIDAD_TEMATICA>_<AUTOR_O_TEMA>.pdf`|`ISW_Repo_G3/Material_Bibliografico/<Unidad_Tematica>`|Soporte|
|Presentación de Clase|`G3_PRES_U<N>_<TEMA>.pdf`|`ISW_Repo_G3/Presentaciones_Clases/Unidad_<N>`|Soporte|
|Entregable de Trabajo Práctico Grupal|`G3_TP<NN>_Entregable.pdf`|`ISW_Repo_G3/Trabajos_Practicos_Grupales/TP<NN>_<Tema>`|Entregable|
|Entregable de Trabajo de Investigación|`G3_TPINV<NN>_<TEMA>.pdf`|`ISW_Repo_G3/Trabajos_Practicos_Grupales/Trabajo_Investigacion/Trabajo_Investigacion_<NN>`|Entregable|
|Plan de Gestión de Configuración de Software|`G3_SCM_PlanGestionConfiguracion_<VERSION>.pdf`|`ISW_Repo_G3/Documentacion_Gestion`|GestionSCM|
|Consigna Trabajo Práctico|`G3_TP<NN>_Consigna.pdf`|`ISW_Repo_G3/Trabajos_Practicos_Grupales/TP<NN>_<Tema>`|Soporte|
|Consigna Trabajo Práctico Investigación|`G3_TPINV<NN>_<TEMA>_Consigna.pdf`|`ISW_Repo_G3/Trabajos_Practicos_Grupales/Trabajo_Investigacion/Trabajo_Investigacion_<NN>`|Soporte|

---

## Glosario

| Sigla | Significado |
|------------|-------------|
|`G3_`|Prefijo fijo que identifica al Grupo 3. Presente al inicio de todos los nombres de ítems de configuración del repositorio.|
|`<NN>`|Número correlativo (de Parcial o de Trabajo Práctico), de dos dígitos con cero a la izquierda. Ej.: 01, 04, 11.|
|`<N>`|Número de unidad temática de la cursada (1 a 4).|
|`<UNIDAD_TEMATICA>`|Nombre corto del área bibliográfica a la que pertenece el material, en mayúsculas y sin espacios ni tildes. Ej.: ISW, SCM, TESTING, TDD, AGIL, LEAN.|
|`<AUTOR_O_TEMA>`|Apellido del autor principal o nombre corto del tema del material bibliográfico, en mayúsculas y sin espacios ni tildes. Ej.: SOMMERVILLE, SWEBOK.|
|`<TEMA>`|Nombre corto y descriptivo del contenido del ítem, en mayúsculas y sin espacios ni tildes. Ej.: SCRUM, LEAN_KANBAN, DESPLIEGUE, POSTER.|
|`<Unidad_Tematica>` (en ubicación)|Nombre de la subcarpeta de Material_Bibliografico a la que pertenece el ítem, tal como figura en el árbol de carpetas. Ej.: Ingeniería_de_Software, Testing_de_Software.|
|`<Tema>` (en ubicación)|Nombre corto del TP tal como figura en el nombre de su carpeta. Ej.: SCM, Test_Driven_Development.|
|`<VERSION>`|Número de versión del documento de gestión de configuración|
|KvsS|Abreviación destinada al libro Kanban VS Scrum.|
|LeUX|Abreviación destinada al libro Lean UX.|
|TDD|Abreviación en inglés de Test Driven Development.|

---

## Definición y justificación de líneas base (Baselines)

Para asegurar un control de versiones riguroso y mantener la integridad del repositorio, el equipo estableció dos niveles de líneas base a lo largo del ciclo de vida del proyecto:

**1. Línea Base de Gestión (Configuración y Estructura)**

Ítem asociado: archivo correspondiente al tipo de ítem GestionSCM (Plan de Gestión de Configuración de Software).

Justificación: este documento contiene la meta-documentación del proyecto, estableciendo reglas críticas como la estructura de carpetas, la clasificación de los ítems de configuración y la regla de nombrado unificada. Establecerlo como línea base congela las reglas estructurales del repositorio: cualquier modificación futura sobre cómo se gestiona la configuración requerirá un control de cambios formal, evitando alteraciones no planificadas que puedan desorganizar el repositorio del grupo.

**2. Líneas Base de Producto (Hitos de Evaluación)**

Ítems asociados: archivos correspondientes al tipo de ítem Entregable, alojados dentro del directorio Trabajos_Practicos_Grupales.

Justificación: las resoluciones de los Trabajos Prácticos grupales y del Trabajo de Investigación representan el trabajo del equipo. Al no admitir re-entrega, cada entregable (por ejemplo, los archivos nombrados bajo la regla `G3_TP<NN>_Entregable.pdf` o `G3_TPINV<NN>_<TEMA>.pdf`) se establece como línea base en el momento exacto de su envío, "congelando" esa versión específica. Esta práctica garantiza la trazabilidad absoluta de la versión evaluada por la cátedra y proporciona un punto de restauración seguro y auditable: si se requieren correcciones futuras, los nuevos cambios se iteran sobre una versión posterior, manteniendo intacta la integridad histórica de la entrega original.

---

## Enlace público al repositorio

[Repositorio ISW_Repo_G3](https://github.com/angela2022A/ISW_Repo_G3)
