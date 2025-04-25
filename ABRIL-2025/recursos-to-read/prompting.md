cinco elementos esenciales de la ingeniería de prompts para maximizar resultados con el mínimo esfuerzo.

# IDEAS:
- La selección del **modelo adecuado** tiene un impacto significativo en el rendimiento de tus prompts y resultados.
- Un **propósito claro** para tu prompt es crucial para lograr resultados deseados de manera efectiva.
- Las **variables dinámicas** permiten la reutilización de prompts y adaptabilidad en diferentes contextos y aplicaciones.
- Incluir **ejemplos** concretos en los prompts ayuda a especificar el **formato y estructura** de la salida deseada.
- Los tipos de **salida** pueden ser **texto o JSON**, lo que influye en la confiabilidad de los resultados generados.

- La combinación de modelo, propósito, variables, ejemplos y tipo de salida crea **prompts efectivos**.

- Los prompts de alta calidad pueden producir el 80% de los resultados con solo el 20% del esfuerzo invertido.
- Las **variables estáticas** se fijan durante el desarrollo, mientras que las variables dinámicas cambian según el contexto.
- El **chaining** de prompts permite la integración de salidas de un prompt como entradas para otro.
- Las salidas en formato **JSON** proporcionan datos estructurados, fundamentales para construir sistemas y flujos de trabajo de IA complejos.

# Marco de cuatro niveles para la ingeniería de prompts

## Nivel 1: Prompt ad hoc
- Prompts rápidos en lenguaje natural para prototipado ágil
- Perfecto para explorar capacidades y comportamientos del modelo
- Se pueden ejecutar en múltiples modelos para comparación
- Ideal para tareas puntuales y experimentación
```ejemplo
Resume el contenido con 3 opiniones a favor del autor y 3 opiniones en contra del autor

...pega el contenido aquí...
```

## Nivel 2: Prompt estructurado
- Prompts reutilizables con propósito e instrucciones claras
- Usa formato XML/estructurado para mejor rendimiento del modelo
- Contiene variables estáticas que se pueden modificar
- Resuelve problemas bien definidos y repetibles
```ejemplo
<proposito>
    Resume el contenido dado según las instrucciones y el ejemplo de salida
</proposito>

<instrucciones>
   <instruccion>Salida en formato markdown</instruccion>
   <instruccion>Resume en 4 secciones: Resumen general, Puntos principales, Sentimiento, y 3 opiniones a favor del autor y 3 opiniones en contra del autor</instruccion>
   <instruccion>Escribe el resumen en el mismo formato que el ejemplo de salida</instruccion>
</instrucciones>

<contenido>
    {...} <<< actualiza esto manualmente
</contenido>
```

## Nivel 3: Prompt estructurado con ejemplo de salida
- Se basa en el Nivel 2 añadiendo ejemplos de salida
- Los ejemplos guían al modelo para producir formatos específicos
- Aumenta la consistencia y confiabilidad de las salidas
- Perfecto cuando el formato de salida es importante
```ejemplo
<proposito>
    Resume el contenido dado según las instrucciones y el ejemplo de salida
</proposito>

<instrucciones>
   <instruccion>Salida en formato markdown</instruccion>
   <instruccion>Resume en 4 secciones: Resumen general, Puntos principales, Sentimiento, y 3 opiniones a favor del autor y 3 opiniones en contra del autor</instruccion>
   <instruccion>Escribe el resumen en el mismo formato que el ejemplo de salida</instruccion>
</instrucciones>

<ejemplo-salida>

    # Título

    ## Resumen General
    ...

    ## Puntos Principales
    ...

    ## Sentimiento
    ...

    ## Opiniones (a favor del autor)
    ...

    ## Opiniones (en contra del autor)
    ...
</ejemplo-salida>

<contenido>
    {...} <<< actualiza esto manualmente
</contenido>
```

## Nivel 4: Prompt estructurado con contenido dinámico
- Prompts listos para producción con variables dinámicas
- Se pueden integrar en código y aplicaciones
- Escalabilidad infinita mediante actualizaciones programáticas
- Base para construir herramientas y agentes potenciados por IA
```ejemplo
igual que el ejemplo del nivel 3 pero...

<contenido>
    {{contenido}} <<< actualiza esto dinámicamente con código
</contenido>
```

---

## Preparándote para el salto 100x en Modelos de Lenguaje Grande (LLMs)

### Resumen en una frase
**Domina la ingeniería de prompts y amplía tu alcance de resolución de problemas para aprovechar la inminente mejora 100x en los LLMs.**

---

## Ideas principales

- **La mejora 100x en los LLMs es inevitable**—el éxito depende de prepararse ahora.
- **Las herramientas de IA actuales son primitivas** comparadas con lo que viene.
- **Los prompts son el nuevo código**: dominarlos es esencial para la programación y el trabajo del conocimiento del futuro.
- **Expandir el alcance de los problemas** te prepara para usar modelos más potentes a medida que surgen.

---

## Estrategias accionables

### 1. **Domina la ingeniería de prompts**
- Trata **los prompts como la unidad fundamental** del desarrollo de software del futuro.
- Practica a diario: **apunta a escribir 100 prompts por día**.
- Evita depender demasiado de librerías—**entiende primero las capacidades crudas** de los modelos.
- Usa prompts para todo: **código, documentación, feedback**, y más.
- La práctica regular construye intuición y **revela los límites y el potencial del modelo**.

### 2. **Usa Rich Prompts**
- Crea prompts grandes y ricos llenos de **tu conocimiento único de dominio**.
- Resuelve problemas complejos que los prompts simples no pueden abordar.
- Usa Rich Prompts para **llevar al límite las capacidades** de los LLMs actuales y encontrar potencial oculto.

### 3. **Expande tu conjunto de problemas**
- Aborda **problemas reales y no resueltos** usando las herramientas de IA actuales.
- Experimenta con flujos de trabajo y **aplica IA de formas creativas y útiles**.
- Esto desarrolla habilidad y preparación para modelos futuros más capaces.

---

## Hábitos para el éxito a largo plazo

- **Escribe 100* prompts al día** para desarrollar fluidez y perspectiva.
- **Documenta los aprendizajes** de los experimentos con prompts para seguir tu crecimiento.
- Mantente proactivo **siguiendo tendencias de IA** y adaptándote temprano.
- Reflexiona regularmente para **identificar áreas de mejora** en tus habilidades de prompts.
- Retrasa la abstracción de herramientas—**primero domina los fundamentos**.

---

## Ideas clave

- Anticipar el futuro es una habilidad central en ingeniería.
- El **verdadero potencial de los modelos actuales** permanece en gran parte sin explotar.
- Entender los límites = desbloquear innovación.
- Practicar ahora = **ventaja competitiva** cuando lleguen los modelos 100x.

---

## Frases memorables

> “El LLM 100x está llegando; no es una cuestión de *si*, sino de *cuándo*.”

> “El prompt es la nueva unidad fundamental del trabajo del conocimiento y la programación.”

> “Un BAP es un prompt grande lleno de tus propios datos específicos de dominio.”

> “Apunta a 100 prompts al día; así evolucionamos al siguiente nivel de la ingeniería de software.”

> “Ni siquiera estás cerca de los límites de los modelos, prompts y cadenas de prompts actuales.”
