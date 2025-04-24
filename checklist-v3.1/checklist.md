## Checklist de Preparación y Contenido v2.1 (Acorde al Programa Mejorado)

- [x] **II. Etapa 1: Bienvenida y Alineación (10 min)**
    *   **Contenido Clave:** Bienvenida, Hook, Icebreaker, Objetivos, Agenda *ajustada*, Ref. pre-reading.
    *   **Materiales:** Slides (Bienvenida, Icebreaker, Objetivos, Agenda).
    *   **Notas:** Energía alta, concisión.

- [ ] **III. Etapa 2: Framework: Complejidad -> Modelo -> Estrategia (35 min)**
    *   **Contenido Clave:** Cynefin ultra-simplificado -> **CoT estimado**. Mapeo CoT -> Modelo -> **Estilo de Prompt (Minimalista vs Detallado)**. Ejemplos dev. Discusión JSON & adaptación prompt.
    *   **Materiales:** Slides (Diagrama Mapeo claro, Puntos clave `reasoning-prompt.md`), Board Interactivo (Miro/Figjam con 3 escenarios para clasificar CoT/Modelo/Estilo Prompt).
    *   **Notas:** **Enfatizar la conexión CoT -> Modelo -> Estilo Prompt**. Hacer la actividad interactiva dinámica.

- [ ] **IV. Etapa 3: Técnicas Fundamentales: Demos y Práctica Guiada (75 min)**
    *   **Objetivo:** Mostrar técnicas clave, permitir práctica más profunda, reforzar adaptación.
    *   **Materiales Generales:** Notebook `.ipynb` (con código **solo** para Demos 1, 2, 3), `metaprompt.xml`, `mp_input.txt`, API Keys (`getpass`), Slides (Transición, Instrucciones Hands-on, Snippets conceptuales `o1` prompt, Snippets Tool Use, Snippets Agentes/Memoria para Mención Avanzada). Script Instructor detallado.
    *   **Demo/Hands-on 1 (Prompting/JSON/Adaptación - 25 min):**
        *   **Código:** Listo en `.ipynb`.
        *   **Slides:** Explicación Nivel 1-4, Beneficios JSON, **Slide mostrando concepto prompt minimalista `o1`**. Instrucciones claras para hands-on (modificar schema + simplificar prompt).
        *   **Script:** Verbalizar diferencias `GPT-4o` vs `o1` prompts. Guiar el hands-on activamente.
    *   **Demo 2 (Workflows: Chaining/Tool Use Básico - 20 min):**
        *   **Código:** Chaining simple listo en `.ipynb`. *No* código complejo de tool use, solo estructura conceptual.
        *   **Slides:** Diagrama chaining, Slide conceptual Tool Use (input -> LLM -> tool -> LLM -> output).
        *   **Script:** Explicar paso a paso el chaining. Enfatizar control. Posicionar Tool Use como extensión lógica.
    *   **Demo 3 (Metaprompting - 15 min):**
        *   **Código:** Listo en `.ipynb` o script. Archivos `metaprompt.xml`, input `.txt`.
        *   **Slides:** Qué/Por qué/Cuándo Metaprompting.
        *   **Script:** Ejecutar, mostrar output. **Pregunta clave:** "¿Cómo cambiaríamos el *meta*prompt para un estilo `o1`?".
    *   **Mención Avanzada (5 min):**
        *   **Slides:** Screenshots/Snippets de Agentes (CrewAI/LangChain) y Memoria (`mem0ai`). Títulos claros: "Para >5 Pasos CoT / Dominio Complejo".
        *   **Script:** Solo mencionar, no explicar en detalle. Indicar que son temas para explorar después.
    *   **Notas Instructor:** **Probar TODO el código**. Gestionar tiempo del hands-on. Repetir mensaje adaptación modelo.

- [ ] **V. Etapa 4: Ejercicio Grupal (35 min)**
    *   **Contenido Clave:** 2 Escenarios realistas.
    *   **Materiales:** **Plantilla Diseño v2.1** (compartible, con campos: Escenario, Tarea+CoT, Modelo+Justificación, Estrategia, Prompt Esbozo Adaptado, Workflow?, Consideraciones). Instrucciones claras (slide). Breakout Rooms (si aplica).
    *   **Notas:** Circular y guiar. **Foco en la justificación Modelo/Prompt estilo**. Cronometrar pitches.

- [ ] **VI. Etapa 5: Mejores Prácticas Adaptativas (10 min)**
    *   **Contenido Clave:** Puntos *críticos* del checklist v2.1 (Adaptar prompt, CoT->Modelo, JSON, Documentar, Evitar X en `o1`).
    *   **Materiales:** Checklist v2.1 (link para compartir). Slide resumen con 4-5 puntos clave.
    *   **Notas:** Ser rápido y enfocado en lo accionable.

- [ ] **VII. Etapa 6: Q&A y Próximos Pasos (15 min)**
    *   **Contenido Clave:** Q&A, Parking Lot, Recap (adaptación modelo), Recursos, Call to Action/Reto v2.1 (diseñar 2 prompts), Comunidad/Certificado.
    *   **Materiales:** Slides (Q&A, Recursos compilados, Reto detallado), Board Parking Lot.
    *   **Notas:** Gestionar Q&A. Terminar con energía y claridad sobre próximos pasos.

- [ ] **VIII. Post-Taller**
    *   **Materiales:** Email Seguimiento (agradecimiento, links recursos, grabación?, Parking Lot respondido). Canal Comunidad preparado.
    *   **Acción:** Enviar email 24-48h. Monitorear canal, animar participación en el reto.
