**Checklist de Preparación y Contenido por Etapa (PRD)**

- [ ] **I. Pre-Taller**

*   **Objetivo:** Nivelar conocimientos básicos, optimizar tiempo introductorio, generar expectativa.
*   **Contenido Clave:**
    *   Resumen Cynefin simplificado (definiciones + ejemplo dev por dominio).
    *   Resumen 4-Level Prompting Framework (Nivel 1 a 4, breve descripción + mini-ejemplo).
    *   Introducción Modelos Razonamiento (`o1`) vs. No-Razonamiento (`GPT-4o`) (Cuándo considerar cada uno, diferencias clave en prompting según artículo `reasoning-prompt.md`).
    *   (Opcional) Link a video/artículo externo "LLM Basics" (máx 5 min).
*   **Materiales Requeridos:**
    *   **Documento PDF/Google Doc (1-2 páginas):** Crear y diseñar el resumen conciso con los 3 puntos clave. Debe ser visualmente claro y fácil de digerir.
    *   **Email de Convocatoria/Recordatorio:** Redactar email claro explicando la importancia del pre-reading, adjuntando/linkeando el documento y el video opcional. Establecer expectativas.
*   **Metodología/Acción:** Enviar el email con el material al menos 3-4 días antes del taller.

- [ ] **II. Etapa 1: Bienvenida y Alineación (10 minutos)**

*   **Objetivo:** Enganchar, conectar con audiencia, revisar agenda y objetivos.
*   **Contenido Clave:**
    *   Mensaje de bienvenida energético.
    *   Hook: Mencionar "Salto 100x" y relevancia actual de IA en desarrollo.
    *   Icebreaker: Pregunta "¿Mayor desafío/oportunidad IA en tu flujo actual?".
    *   Repaso visual rápido de objetivos y agenda del taller.
    *   Referencia al pre-reading ("Como vimos en el material...").
*   **Materiales Requeridos:**
    *   **Slides (3-4):**
        *   Título del Taller + Bienvenida.
        *   Diapositiva Icebreaker (con instrucción para Mentimeter/Slido).
        *   Diapositiva Objetivos del Taller.
        *   Diapositiva Agenda Visual.
    *   **Herramienta de Votación Online (Mentimeter/Slido):** Configurar previamente la pregunta del icebreaker (tipo nube de palabras o similar). Tener listo el link/código para compartir.
*   **Metodología/Actividades:** Presentación + Interacción con herramienta de votación. Mostrar resultados en vivo.
*   **Notas del Instructor:** Mantener alta energía. Ser conciso. Validar que todos tengan acceso a la herramienta de votación.

- [ ] **III. Etapa 2: Mapeando Complejidad, Estrategias y Tipos de Modelo (35 minutos)**

*   **Objetivo:** Establecer el framework Cynefin-Estrategia-Modelo. Introducir adaptación de prompting.
*   **Contenido Clave:**
    *   Explicación Cynefin simplificado (aplicado a dev).
    *   Mapeo detallado: Claro (<3 CoT) -> GPT-4o, Prompt Básico; Complicado (3-5 CoT) -> GPT-4o (detallado) / o1 (minimalista), JSON, Chaining; Complejo (>5 CoT) -> o1 (ideal), Agentes, Memoria, Metaprompting, Prompt Minimalista; Caótico/Desorden -> Prompt Directivo.
    *   Discusión: ¿Por qué JSON? ¿Por qué Minimalist Chaining vs. Librerías? (Ref. `chains.md`).
    *   *Punto Crítico:* Enfatizar por qué el *prompting* debe cambiar entre `o1` y `GPT-4o` (basado en `reasoning-prompt.md`).
*   **Materiales Requeridos:**
    *   **Slides:** Diagrama visual claro del mapeo Cynefin <-> Estrategia <-> Modelo <-> Tipo de Prompt. Ejemplos conceptuales de tareas dev en cada dominio. Resumen de pros/contras Chaining Minimalista. Puntos clave del artículo `reasoning-prompt.md`.
    *   **Board Interactivo (Miro/Figjam/etc.):** Preparar 3 mini-escenarios de desarrollo (ej. "Refactorizar función legada", "Crear API simple", "Diagnosticar bug intermitente"). Preparar plantilla para que asistentes clasifiquen y sugieran modelo/estrategia.
*   **Metodología/Actividades:** Presentación + Discusión guiada + Actividad interactiva en board virtual.
*   **Notas del Instructor:** Asegurarse que la diferencia de prompting entre modelos quede clara. Fomentar discusión en la actividad interactiva.

- [ ] **IV. Etapa 3: Demos y Práctica Guiada (70 minutos)**

*   **Objetivo:** Mostrar implementación práctica, permitir experimentación guiada, reforzar adaptación al modelo.
*   **Contenido Clave:** Ver desglose demo por demo.
*   **Materiales Requeridos Generales:**
    *   **Entorno de Ejecución:** Jupyter Notebook (`.ipynb`) preparado y probado, con todo el código necesario, claramente dividido por demo. Asegurarse que las API Keys (OpenAI) estén configuradas (usar `getpass` o variables de entorno como en el notebook). `pip install` necesarios comentados o ejecutados al inicio.
    *   **Archivos de Apoyo:** `metaprompt.xml`, `mp_code_review_input.txt` (o similar), archivos de imagen (si se usan en `mp_script_to_blog`).
    *   **Slides:** Diapositivas de transición entre demos, diapositivas con instrucciones claras para cada micro-hands-on. Diapositivas con snippets conceptuales JS/PHP (opcional).
    *   **Script/Notas del Instructor:** Puntos clave a mencionar en cada demo, especialmente los *comentarios* sobre adaptación de prompts a `o1` vs `GPT-4o`. Tiempos estimados por sección.
*   **Materiales Específicos por Demo/Hands-on:**
    *   **Demo 1 (Prompting+JSON):** Código listo (`.ipynb`). Slide explicando beneficios JSON. *Script:* "Para `o1`, podríamos simplificar este prompt..."
    *   **Hands-on 1 (JSON Mod):** Instrucción clara (ej. "Añade 'location': {'type': 'string'} al schema y re-ejecuta").
    *   **Demo 2 (Chaining):** Código listo (manual y LangChain) (`.ipynb`). Slide comparativo. *Script:* "Control vs conveniencia...".
    *   **Hands-on 2 (Chain Sketch):** Instrucción clara (ej. "Dibuja/escribe: Prompt1(input)->Output1; Prompt2(Output1)->FinalOutput").
    *   **Demo 3 (Metaprompting):** Archivos `metaprompt.xml`, `mp_*.txt` listos. Código para ejecutarlo (`.ipynb` o script). Slide explicando *qué/por qué/cuándo*. *Script:* "Este prompt generado es bueno para `GPT-4o`...".
    *   **Demo 4 (Agente+HITL):** Código `agno` listo (`.ipynb`). *Script:* "Importancia HITL, `o1` aquí sería potente...".
    *   **Demo 5 (Memoria):** Código `mem0ai` listo (`.ipynb`). *Script:* "Clave para agentes con contexto...".
*   **Metodología/Actividades:** Live coding claro, transiciones suaves, verbalizar el "por qué", ejecución de hands-on cronometrada.
*   **Notas del Instructor:** ¡Probar todo el código y flujo antes! Tener soluciones listas para los hands-on. Gestionar el tiempo estrictamente.

- [ ] **V. Etapa 4: Ejercicio Grupal (35 minutos)**

*   **Objetivo:** Aplicar el framework completo (Cynefin -> Modelo -> Estrategia -> Prompt) en un diseño colaborativo.
*   **Contenido Clave:** 2 escenarios de desarrollo realistas (Generador Docs, Triaje Bugs).
*   **Materiales Requeridos:**
    *   **Plantilla de Diseño v2 (Google Doc/Notion):** Crear plantilla compartible con las secciones definidas (Escenario, Complejidad+CoT, Modelo Rec., Estrategia, Prompt Esbozo Adaptado, Chaining?, Metaprompting?, Agente/Tools?, Opc. Avanzado).
    *   **Instrucciones Claras:** Slide explicando la tarea, el uso de la plantilla y el tiempo (ej. 20 min diseño + 3 min pitch + 2 min feedback por grupo).
    *   **Configuración Breakout Rooms** (si aplica).
*   **Metodología/Actividades:** Trabajo en grupos, instructor circula para dudas, pitches cronometrados, feedback constructivo enfocado en la justificación de las elecciones.
*   **Notas del Instructor:** Fomentar la discusión sobre la *elección del modelo y la adaptación del prompt*.

- [ ] **VI. Etapa 5: Mejores Prácticas Adaptativas (15 minutos)**

*   **Objetivo:** Consolidar aprendizajes en guías accionables.
*   **Contenido Clave:** Principales "Do's & Don'ts" del checklist, enfatizando adaptación al modelo, JSON, Metaprompting, documentación.
*   **Materiales Requeridos:**
    *   **Checklist v2 (Google Sheet/Notion):** Crear y tener listo el link para compartir. Debe incluir los puntos clave adaptados (ej. "Adapta prompt a o1/GPT-4o").
    *   **Slides:** Resumen visual de los 3-4 puntos más críticos del checklist.
*   **Metodología/Actividades:** Discusión interactiva guiada por el checklist compartido.
*   **Notas del Instructor:** Enfocar en lo más práctico y aplicable.

- [ ] **VII. Etapa 6: Q&A y Cierre (15 minutos)**

*   **Objetivo:** Resolver dudas finales, proveer recursos, inspirar acción post-taller.
*   **Contenido Clave:** Q&A, Parking Lot, Recap final, Lista de Recursos, Call to Action + Reto Post-Evento, Info Comunidad/Certificado.
*   **Materiales Requeridos:**
    *   **Slide Q&A.**
    *   **Board Parking Lot (Miro/Trello/etc.):** Crear board y tener link listo.
    *   **Slide de Recursos:** Compilar TODOS los links útiles (Repo código, Pre-reading, Slides, Artículo Reasoning, Herramientas: OpenAI, LangChain, Agno, Mem0, Canal Comunidad, etc.).
    *   **Slide Detallando el Reto Post-Evento:** Instrucciones claras para el reto de generar prompts diferenciados + cómo compartir.
*   **Metodología/Actividades:** Q&A facilitado, presentación clara de recursos y próximos pasos.
*   **Notas del Instructor:** Ser claro sobre cómo se gestionará el Parking Lot. Terminar con energía y motivación.

- [ ] **VIII. Post-Taller**

*   **Objetivo:** Asegurar acceso a materiales, responder preguntas pendientes, fomentar comunidad.
*   **Materiales Requeridos:**
    *   **Email de Seguimiento:** Redactar email con agradecimiento, link a grabación (si existe), link a TODOS los recursos compartidos, link al Parking Lot (con respuestas si ya están).
    *   **Canal Comunidad (Slack/Discord):** Preparar canal, postear bienvenida y recordatorio del reto.
*   **Metodología/Acción:** Enviar email 24-48h post-taller. Monitorear canal y responder dudas/feedback del reto.
