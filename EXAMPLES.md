# 💬 EJEMPLOS DE INTERACCIONES PARA LA DEMO
# Casos de uso completos para MEDI-IA-LEGAL

## 🎯 CASO 1: Flujo Completo Exitoso

### Escenario
Pareja con hijos menores que desea divorciarse de manera amigable.

### Conversación

**Usuario 1:**
```
Hola, mi esposa y yo queremos divorciarnos de mutuo acuerdo. Tenemos dos hijos menores.
```

**Respuesta esperada del sistema:**
- Bienvenida cordial
- Explicación de los 3 puntos nodales
- Comenzar con el Punto 1: Bienes

---

**Usuario 2:**
```
Entendido. Para los bienes, tenemos una casa valorada en 300 millones, dos vehículos por 80 millones, y ahorros por 50 millones. Tenemos una deuda hipotecaria de 100 millones.
```

**Respuesta esperada:**
- Cálculo del total: Activos = 430M, Deudas = 100M
- Invocación de `calculate_society_split`
- Resultado: 330M netos → 165M para cada uno

---

**Usuario 3:**
```
De acuerdo con la división 50/50. ¿Cómo seguimos con los alimentos?
```

**Respuesta esperada:**
- Confirmación del acuerdo en Punto 1
- Transición al Punto 2: Obligaciones Alimentarias
- Preguntas sobre ingresos de cada cónyuge

---

**Usuario 4:**
```
Yo gano 8 millones mensuales y mi esposa gana 6 millones.
```

**Respuesta esperada:**
- Reconocimiento de los ingresos
- Explicación sobre obligaciones alimentarias mutuas (si aplica)
- Transición al Punto 3: Hijos Menores

---

**Usuario 5:**
```
Tenemos dos hijos de 8 y 12 años. Acordamos custodia compartida y cada uno cubrirá los gastos cuando los tenga.
```

**Respuesta esperada:**
- Posible invocación de `legal_analyst_tool` para verificar "Interés Superior del Menor"
- Sugerencia de formalizar gastos (educación, salud, etc.)
- Validación del acuerdo

---

**Usuario 6:**
```
Entendido, formalizaremos los gastos. ¿Está completa la propuesta?
```

**Respuesta esperada:**
- Resumen final de los 3 puntos:
  1. Bienes: División 50/50 (165M c/u)
  2. Alimentos: No aplica entre cónyuges
  3. Hijos: Custodia compartida con gastos compartidos
- Felicitación por el acuerdo
- Fin de la mediación

---

## 🚨 CASO 2: Activación de Barrera Ética (División Injusta)

### Escenario
Una parte intenta obtener una división desigual de bienes.

### Conversación

**Usuario 1:**
```
Tenemos bienes por 600 millones sin deudas. Quiero 400 millones para mí y 200 para mi cónyuge.
```

**Respuesta esperada:**
- ⚠️ Detección de inequidad (67% vs 33%)
- Rechazo de la propuesta
- Invocación de `legal_analyst_tool`
- Cita del Código Civil: División 50/50
- Solicitud de reconsideración

---

**Usuario 2:**
```
¿Por qué? Yo aporté más durante el matrimonio.
```

**Respuesta esperada:**
- Explicación legal sobre la sociedad conyugal
- Cita: "Bienes adquiridos durante el matrimonio pertenecen a la sociedad conyugal"
- Mención de excepciones (herencias, donaciones)
- Invitación a reconsiderar

---

**Usuario 3:**
```
Está bien, acepto la división 50/50. 300 millones para cada uno.
```

**Respuesta esperada:**
- ✅ Confirmación de la propuesta justa
- Invocación de `calculate_society_split` (600M, 0 deudas)
- Resultado: 300M para cada cónyuge
- Avance al siguiente punto

---

## 🚨 CASO 3: Barrera Ética en Alimentos para Hijos

### Escenario
Una parte intenta evadir responsabilidad alimentaria.

### Conversación

**Usuario 1:**
```
Tenemos un hijo de 5 años. Mi esposa se quedará con la custodia, así que ella debe pagar todo.
```

**Respuesta esperada:**
- ⚠️ Detección de posible inequidad
- Invocación de `legal_analyst_tool`
- Cita sobre obligaciones alimentarias de ambos padres
- Explicación del "Interés Superior del Menor"

---

**Usuario 2:**
```
¿Cuánto debería aportar entonces?
```

**Respuesta esperada:**
- Pregunta sobre ingresos de ambas partes
- Explicación de criterios (necesidades del menor, capacidad económica)
- Sugerencia de porcentajes razonables

---

**Usuario 3:**
```
Yo gano 10 millones y ella gana 5 millones. Propongo aportar 2 millones mensuales.
```

**Respuesta esperada:**
- Análisis de la propuesta (20% del ingreso)
- Validación o sugerencia de ajuste
- Confirmación del acuerdo

---

## 💡 CASO 4: Consulta Legal Específica

### Conversación

**Usuario 1:**
```
¿Qué dice la ley sobre el divorcio unilateral?
```

**Respuesta esperada:**
- Invocación de `legal_analyst_tool`
- Cita de la Ley 2442 de 2024
- Explicación: "La sola voluntad de uno de los cónyuges es suficiente"

---

**Usuario 2:**
```
¿Las herencias entran en la división de bienes?
```

**Respuesta esperada:**
- Invocación de `legal_analyst_tool`
- Cita del Código Civil
- Explicación: "Las herencias y donaciones NO entran en la sociedad conyugal"

---

## 🔧 CASO 5: Cálculo Financiero Complejo

### Conversación

**Usuario 1:**
```
Tenemos:
- Casa: 500 millones
- Apartamento: 300 millones  
- Vehículos: 150 millones
- Inversiones: 200 millones
- Hipoteca casa: 180 millones
- Préstamo vehículo: 50 millones
¿Cuánto le corresponde a cada uno?
```

**Respuesta esperada:**
- Sumatoria de activos: 500 + 300 + 150 + 200 = 1,150M
- Sumatoria de deudas: 180 + 50 = 230M
- Invocación de `calculate_society_split(1150, 230)`
- Resultado: 920M netos → 460M para cada cónyuge

---

## 🎭 CASO 6: Desacuerdo y Re-negociación

### Conversación

**Usuario 1:**
```
Quiero la casa completa (500M) y que mi cónyuge se quede con el apartamento (300M) y los vehículos (150M).
```

**Respuesta esperada:**
- Cálculo: 500M vs 450M
- Detección de leve desequilibrio
- Sugerencia de compensación económica de 50M

---

**Usuario 2:**
```
¿Puedo quedarme con la casa y compensar con dinero en efectivo?
```

**Respuesta esperada:**
- ✅ Aceptación de propuestas creativas
- Validación: Casa (500M) - Compensación (40M) ≈ 460M cada uno
- Solicitud de confirmación de ambas partes

---

## 📊 MÉTRICAS DE INTERACCIONES

### Promedio de mensajes por punto nodal:
- Punto 1 (Bienes): 3-5 mensajes
- Punto 2 (Alimentos): 2-4 mensajes  
- Punto 3 (Hijos): 3-6 mensajes
- **Total:** ~10-15 mensajes para mediación completa

### Frecuencia de uso de herramientas:
- `calculate_society_split`: 1-2 veces por sesión
- `legal_analyst_tool`: 2-4 veces por sesión

---

## 🎯 TIPS PARA LA DEMO

### Preparar estos mensajes:
1. **Inicio rápido:**
   ```
   Hola, queremos iniciar un divorcio de mutuo acuerdo.
   ```

2. **Trigger financiero:**
   ```
   Tenemos activos por 500 millones y deudas por 100 millones.
   ```

3. **Trigger ético:**
   ```
   Quiero el 80% de los bienes.
   ```

4. **Corrección:**
   ```
   Acepto la división 50/50.
   ```

### Variantes para mostrar flexibilidad:
- Números diferentes (200M, 1,000M, etc.)
- Diferentes configuraciones familiares (sin hijos, 1 hijo, 3 hijos)
- Casos con/sin deudas
- Propuestas creativas (trueque de bienes)

---

## ⚡ INTERACCIONES RÁPIDAS PARA TIEMPO LIMITADO

Si solo tienes 5 minutos para la demo:

**Secuencia mínima:**
1. "Hola" → Bienvenida del sistema
2. "Activos 500M, deudas 100M" → Invoca calculator
3. "Quiero 80%" → Activa barrera ética + RAG
4. "Acepto 50/50" → Confirma acuerdo
5. "¿Qué dice la ley sobre divorcio unilateral?" → Muestra RAG puro

✅ Esta secuencia demuestra **TODOS** los componentes clave en 5 minutos.
