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

## Reglas de Nombrado

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

## 1. Momentos de Creación (Hitos de Línea Base)

La estrategia de congelamiento de versiones se divide en dos instancias fundamentales a lo largo del ciclo de vida del proyecto:

*   **Línea Base Inicial:** Se establecerá la primera línea base en el momento en que la totalidad de los recursos provistos por la cátedra (definidos como ítems de tipo *Administrativo* y *Soporte*) se encuentren efectivamente subidos al repositorio. Esto justifica la creación de un entorno de trabajo base sólido antes de iniciar la producción del equipo.
*   **Líneas Base Evolutivas:** Se generarán nuevas líneas base de forma incremental cada vez que se concrete la entrega oficial de un Trabajo Práctico (correspondiente a los ítems de tipo *Entregable*) o cuando se alcance la fecha de un examen parcial. Esto asegura que el estado del repositorio quede auditable e inalterable justo en las instancias críticas de evaluación.

---

## 2. Nomenclatura y Trazabilidad

Para la identificación unívoca de las líneas base, se adopta una convención de nombrado basada estrictamente en el número de versión. 

*   **Formato de ejemplo:** `V1.0`, `V2.0`, `V3.0`

**Justificación:** La simplicidad de este enfoque permite mantener un seguimiento secuencial y claro sobre la evolución temporal de todos los ítems de configuración, facilitando enormemente la auditoría del repositorio.

---

## 3. Criterios de Aceptación para Ítems de Configuración

La robustez de nuestras líneas base se sostiene mediante un riguroso control de calidad previo. Un ítem de configuración solo será incorporado a una línea base si cumple **obligatoriamente** con el siguiente checklist:

- [x] **Ubicación estructural:** El archivo debe encontrarse alojado en el directorio exacto que le corresponde dentro del árbol de carpetas del repositorio.
- [x] **Conformidad de formato:** El archivo debe respetar escrupulosamente las reglas de nombrado definidas para su familia de ítems en la Sección 3 del Plan SCM.
- [x] **Revisión técnica de pares:** El ítem debe haber superado una instancia de verificación de calidad. Para garantizar la objetividad, no basta con la revisión del integrante creador; se exige explícitamente que al menos **un integrante distinto del grupo** audite y valide que el documento se encuentra en óptimas condiciones.


---

## Enlace público al repositorio

[Repositorio ISW_Repo_G3](https://github.com/angela2022A/ISW_Repo_G3)
