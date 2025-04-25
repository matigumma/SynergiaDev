## Plantilla de Diseño: Solución con LLM para Escenario de Desarrollo

**Grupo #:** [Nombre de Grupo]
**Fecha:** [Fecha del Taller]

**Instrucciones:** Analiza el escenario de desarrollo que has elegido. Completa cada una de las siguientes secciones, discutiendo y justificando tus decisiones como grupo. El objetivo es diseñar una solución LLM efectiva y adaptada.

---

### 1. Escenario de ejemplo:

*   [ ] **Generador de Documentación Automática** (Desde código JS/PHP)
*   [ ] **Asistente de Triaje de Bugs** (Desde reportes de usuario)
*   [ ] **Otro** (en que escenario agregarian IA generativa dentro de su empresa?)
*   *(Brevemente, ¿cuál es el objetivo principal que buscan resolver con el LLM en este escenario?)*

---

### 2. Análisis de Complejidad:

*   **Tarea Central:** (Describe la acción principal que debe realizar el LLM)
*   **Estimación de Pasos CoT (Chain-of-Thought):**
    *   [ ] **< 3 Pasos** (Simple/Claro)
    *   [ ] **3-5 Pasos** (Complicado)
    *   [ ] **> 5 Pasos** (Complejo)
*   **Justificación del CoT Estimado:** (¿Por qué creen que requiere esa cantidad de pasos de razonamiento? ¿Qué lógica debe seguir el LLM?)

---

### 3. Selección del Modelo LLM:

*   **Modelo Recomendado:**
    *   [ ] `GPT-4.1` / `Gemini 2.0` (o similar no-razonamiento)
    *   [ ] `o3` / `Gemini 2.5` / `Claude 3.7 sonnet` (o similar de razonamiento)
    *   [ ] Otro (Especificar: Ej. `GPT-4.1-mini / o3-mini / Claude 3.5 haiku / Gemini flash series` por costo/velocidad)
*   **Justificación de la Elección del Modelo:** (Basado en:
    *   *Pasos CoT estimados:* ¿Necesita razonamiento profundo o es más directo?
    *   *Tipo de Tarea:* ¿Es creativa, analítica, requiere seguir reglas estrictas?
    *   *Necesidad de Formato de Salida:* ¿Es crítico un formato JSON/Markdown estricto?
    *   *Consideraciones Prácticas:* ¿Importa más el costo, la latencia o la máxima capacidad?)

---

### 4. Estrategia LLM Principal:

*   (Selecciona la estrategia dominante que usarán)
    *   [ ] **Prompting Estructurado** (Nivel 3-4)
    *   [ ] **Chaining Minimalista** (Secuencia de prompts simples)
    *   [ ] **Tool Use Básico** (LLM necesita llamar a una función/API externa)
    *   [ ] **Metaprompting** (Para generar variantes o prompts complejos)
    *   [ ] Otra (Especificar)
*   **Breve Justificación de la Estrategia:** (¿Por qué esta estrategia es la más adecuada para la tarea y el modelo elegido?)

---

### 5. Diseño del Prompt Principal (o Prompts Clave si hay Chaining):

*   **Estilo del Prompt (¡Adaptado al Modelo Elegido!):**
    *   [ ] **Detallado** (Estilo `non-reasoning`: Instrucciones específicas, ejemplos claros)
    *   [ ] **Minimalista** (Estilo `reasoning`: Objetivo claro, pocas instrucciones directas, sin ejemplos o muy pocos)
*   **Esbozo del Prompt:** (Usa una estructura similar a esta, reemplazando [[...]] con placeholders o descripciones)

    ```xml
    <purpose>
        [[Describe aquí el objetivo claro y conciso del prompt]] 
    </purpose>

    <instructions>
        <instruction>[[Instrucción esencial 1]]</instruction>
        <instruction>[[Instrucción esencial 2 (si aplica)]]</instruction>
        <!-- Añadir más si es Estilo Detallado -->
        <!-- Quitar/Minimizar si es Estilo Minimalista -->
    </instructions>

    <!-- <examples> -->
        <!-- Añadir si es Estilo Detallado (GPT-4o) y ayuda al formato/estilo -->
        <!-- <example> ... </example> -->
    <!-- </examples> -->

    <input_context> 
        <!-- ¿Qué información necesita el prompt? -->
        [[Placeholder para el input principal, ej. código fuente, reporte de bug]] 
    </input_context>

    <output_format>
        <!-- ¿Cómo debe ser la salida? Si es JSON, describir el schema aquí -->
        [[Describe el formato esperado. Ej: "Salida en Markdown JSDoc", "Salida en JSON con schema { 'severidad': ..., 'componentes': ... }"]]
    </output_format> 
    ```

---

### 6. Diseño del Workflow (Opcional):

*   **¿Se necesita un Workflow / Chaining?:** [Sí / No]
*   **Si SÍ, Pasos Lógicos:** (Describe la secuencia. Ej: )
    1.  `Prompt 1 (Input: Reporte Bug) -> Output: JSON Estructurado`
    2.  `Código (Parsear JSON)`
    3.  `Prompt 2 (Input: Info Extraída + Contexto Arq.) -> Output: Componentes Sugeridos`
    4.  `Código (Combinar resultados)`

---

### 7. Necesidad de Agente / Tools (Opcional):

*   **¿Se necesita capacidad de Agente (planificación, autonomía) o Tools?:** [Sí / No]
*   **Si SÍ, Tools Necesarias (Conceptuales):** (Ej: `buscar_en_documentacion(query)`, `obtener_historial_bug(id)`)

---

### 8. Consideraciones Clave y Riesgos:

*   **Formato de Salida:** ¿Qué tan crítico es? ¿Cómo asegurar consistencia? (JSON estricto?)
*   **Manejo de Errores/Ambigüedad:** ¿Qué pasa si el input es malo (código roto, reporte incompleto)?
*   **Evaluación:** ¿Cómo sabrían si la salida es "buena" o correcta?
*   **Contexto Adicional:** ¿Necesita el LLM más información que la del input directo? ¿Cómo se la darían?
*   **Otros Riesgos:** (Ej. Alucinaciones, costos inesperados, latencia)

---

**Preparado por:** [Nombres de los miembros del grupo]