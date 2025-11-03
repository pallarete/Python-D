# Python-D
Curso Python
<h1 align="center">🐍✨ Tipos de Datos Compuestos en Python</h1>
<p align="center">
  Guía visual rápida para entender <b>listas</b>, <b>tuplas</b>, <b>sets</b> y <b>diccionarios</b>.<br>
  Aprender Python nunca fue tan visual 🧠💡
</p>

---

## 📘 Tabla resumen

| Tipo | Imagen mental | Características clave | Ejemplo |
|------|----------------|-----------------------|----------|
| 🧳 **Lista (`list`)** | Mochila flexible | ✅ Ordenada<br>✅ Mutable<br>✅ Duplicados | ```python\nfrutas = ['🍎', '🍌', '🍎']``` |
| 📦 **Tupla (`tuple`)** | Caja sellada | ✅ Ordenada<br>❌ Inmutable<br>✅ Duplicados | ```python\npos = (40.4, -3.7)``` |
| 🧺 **Conjunto (`set`)** | Cesta sin duplicados | ❌ No ordenada<br>✅ Mutable<br>❌ Sin duplicados | ```python\ncolores = {'🔴', '🟢', '🔴'}``` |
| 🗂️ **Diccionario (`dict`)** | Archivador con etiquetas | ✅ Ordenado (desde 3.7+)<br>✅ Mutable<br>❌ Claves únicas | ```python\npersona = {'👤': 'Ana', '🎂': 30}``` |

---

## 🧠 Cuándo usar cada uno

| Necesito... | Uso... | Emoji |
|--------------|--------|-------|
| Una colección que puedo **editar** y mantener **ordenada** | 🧳 Lista | ✅ |
| Datos **fijos**, que **no deben cambiar** | 📦 Tupla | 🛑 |
| **Eliminar duplicados** o **comparar conjuntos** | 🧺 Set | 🔁 |
| Buscar valores por **clave o etiqueta** | 🗂️ Diccionario | 🔍 |

---

## 💡 Ejemplo práctico

```python
# 🧳 Lista
tareas = ['limpiar', 'comprar', 'dormir']

# 📦 Tupla
coordenadas = (40.4, -3.7)

# 🧺 Conjunto
colores = {'rojo', 'azul', 'rojo'}  # {'rojo', 'azul'}

# 🗂️ Diccionario
persona = {'nombre': 'Ana', 'edad': 30}
