**Encuentro Práctico e Intensivo: Integrando IA en tu Código con LLMs**

**Duración:** 3 horas

**Público objetivo:** Desarrolladores con experiencia en programación, interesados en integrar herramientas de IA, como LLMs, en sus proyectos, sin necesidad de experiencia previa en IA.

**Objetivo del Encuentro:**
Capacitar a los desarrolladores para que:
*   Identifiquen la complejidad de un problema de desarrollo usando un marco conceptual (inspirado en Cynefin).
*   Seleccionen y apliquen la estrategia LLM más adecuada (desde prompting básico hasta agentes con memoria).
*   Desarrollen prompts efectivos utilizando un enfoque progresivo (4-Level Framework).
*   **Dominen el Metaprompting para generar prompts de alta calidad de forma escalable.**
*   Implementen workflows y chaining de manera práctica, entendiendo los enfoques minimalistas y basados en librerías.
*   Construyan y evalúen agentes LLM básicos siguiendo buenas prácticas.
*   Apliquen estos conceptos en ejercicios prácticos y vean demostraciones con código real.

**Estructura del Programa Detallada:**

**1. Introducción: El Ecosistema LLM y el Salto 100x (15 minutos)**
    *   **Contenido:**
        *   Bienvenida y objetivos del taller.
        *   ¿Qué son los LLMs y por qué son relevantes *ahora*? (Mencionar "Salto 100x").
        *   Marco Conceptual 1: Niveles de Complejidad (Cynefin Simplificado).
        *   Marco Conceptual 2: Progresión del Prompting (4-Level Framework).
        *   Importancia de empezar simple y escalar.
    *   **Metodología:** Presentación visual, ejemplo rápido de prompt Nivel 1.

**2. Alineando Estrategias LLM con la Complejidad del Problema (40 minutos)**
    *   **Contenido:**
        *   **Dominio Claro:** Prompting Básico (Niveles 1-2).
        *   **Dominio Complicado:** Prompting Estructurado (Niveles 3-4), Function Calling, Structured Output (JSON), Workflows y Chaining. Énfasis en JSON y Minimalist Chaining.
        *   **Dominio Complejo:** Agentes LLM, Chaining Iterativo, Memoria. Introducción a Agentes.
        *   **Dominio Caótico/Desorden:** Prompts directivos/exploratorios.
    *   **Metodología:** Discusión guiada, mapeo visual Cynefin <-> Estrategias LLM.

**3. Demostración Práctica: Del Prompt al Agente (¡Ahora con Metaprompting!) (60 minutos)**
    *   **Contenido:** Implementaciones en vivo.
        *   **(5 min) Herramientas:** Breve mención (OpenAI API, LangChain, Agno, Mem0).
        *   **(10 min) Demo 1: Prompting Efectivo y Salida Estructurada (JSON):**
            *   Progresión Nivel 1 -> 4.
            *   Ejemplo `calendar_event` o `math_reasoning` (`.ipynb`), destacando `json_schema`.
        *   **(15 min) Demo 2: Workflows y Chaining (Minimalista vs. Librería):**
            *   Simular chaining manual simple.
            *   Mostrar ejemplo LangChain (`template_prompt | model`) (`.ipynb`). Discutir pros/contras (`chains.md`).
        *   **(15 min) Demo 3: Metaprompting – El Prompt que Escribe Prompts:**
            *   **Explicación:** ¿Qué es? ¿Por qué es útil? (Productividad asimétrica, consistencia, escalabilidad – basado en video/`README.md`).
            *   **Mostrar:** La estructura de `metaprompt.xml` (purpose, instructions, examples, variables...).
            *   **Ejecutar:** Usar `metaprompt.xml` con una entrada como `mp_code_review_input.txt` o `mp_hn_perspective_input.txt`.
            *   **Resultado:** Mostrar el prompt XML generado automáticamente. Explicar cómo este prompt ahora está listo para ser usado para su tarea específica (revisión de código o análisis de HN).
            *   **Conexión:** Relacionarlo con la necesidad de crear muchos prompts estructurados (Dominio Complicado/Complejo).
        *   **(10 min) Demo 4: Agente Básico con Tool Use y Human-in-the-Loop:**
            *   Implementar ejemplo `agno` (Hacker News) (`.ipynb`).
            *   Mostrar `pre_hook` para confirmación. Relacionar con Dominio Complejo.
        *   **(5 min) Demo Opcional/Rápida: Agregando Memoria:**
            *   Mostrar `mem0ai` (`.ipynb`) y su utilidad para agentes.
    *   **Metodología:** Código en vivo, explicación paso a paso, código disponible.

**4. Ejercicio Práctico: Diseñando la Solución Correcta (30 minutos)**
    *   **Contenido:** Presentar 2-3 escenarios.
    *   **Tarea Grupal:** Para cada escenario:
        1.  Clasificar complejidad (Cynefin simplificado).
        2.  Elegir estrategia LLM (¿Necesita Metaprompting para generar variantes?).
        3.  Esbozar diseño (Prompts Nivel X, Chaining, Agente, ¿entrada para un Metaprompt?).
    *   **Metodología:** Grupos pequeños, discusión, presentación rápida. Foco en diseño.

**5. Mejores Prácticas y Desafíos Comunes (20 minutos)**
    *   **Contenido:** Resumen de puntos críticos.
        *   Empezar Simple (4-Level Framework, Minimalist Chaining).
        *   Claridad y Especificidad (Instrucciones > Constraints).
        *   El Poder de los Ejemplos.
        *   JSON para Fiabilidad.
        *   **Metaprompting para Escalabilidad:** Cuándo considerar generar prompts programáticamente.
        *   Transparencia del Agente.
        *   Evaluación, Costos, Latencia.
        *   Documentación (¡Incluir Metaprompts!).
        *   Ética.
    *   **Metodología:** Discusión interactiva, "Do's and Don'ts".

**6. Sesión de Preguntas y Respuestas (10 minutos)**
    *   **Contenido:** Espacio abierto.
    *   **Metodología:** Preguntas abiertas.

**7. Conclusión y Próximos Pasos (10 minutos)**
    *   **Contenido:**
        *   **Recap:** El viaje completo, incluyendo la generación de prompts con Metaprompting.
        *   **Key Takeaway:** Elegir la herramienta/estrategia correcta, *y saber cómo construirla (o generarla)*.
        *   **Recursos Adicionales:** Añadir `metaprompt.xml` y ejemplos `mp_*.txt`.
        *   **Llamada a la Acción:** "Experimenta con el Metaprompt: intenta definir y generar un prompt para una de tus tareas repetitivas".
    *   **Metodología:** Cierre motivacional, entrega de recursos.

---

**Ajustes Realizados para Incluir Metaprompting:**

*   **Objetivo Actualizado:** Se añadió explícitamente "Dominar el Metaprompting".
*   **Demo Dedicada:** Se insertó una demo específica de 15 minutos en la Sección 3 para explicar y mostrar el Metaprompting en acción, usando los archivos proporcionados.
*   **Ajuste de Tiempos:** Se redistribuyeron ligeramente los tiempos de las otras demos en la Sección 3 para acomodar la nueva demo de Metaprompting.
*   **Ejercicio Práctico:** Se sugiere considerar si Metaprompting sería útil en el diseño de la solución.
*   **Mejores Prácticas:** Se incluyó una mención a Metaprompting como una técnica para la escalabilidad.
*   **Recursos:** Se añadieron los archivos `metaprompt.xml` y `mp_*.txt` a la lista de materiales.
