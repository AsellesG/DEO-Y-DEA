# Regalidea Backend · DEA/DEO Recommender

Este backend está desarrollado con **FastAPI** y expone un endpoint inteligente para recomendar productos personalizados, según el perfil emocional (**DEA**) o lógico (**DEO**) del usuario.

---

## 🎯 Características

- Recomendaciones basadas en edad, género, ocasión, presupuesto y gustos.
- Personalización emocional (DEA) o práctica (DEO).
- Filtrado por presupuesto con tolerancia.
- Catálogo cargado desde un archivo JSON optimizado.

---

## 🚀 Endpoint principal

**POST** `/recomendar`

### Request JSON:
```json
{
  "ia": "DEA",
  "edad": 30,
  "genero": "MUJER",
  "ocasion": "CUMPLEAÑOS",
  "presupuesto": 25.00,
  "gustos": ["arte", "mar", "relax"]
}
```

### Response JSON (ejemplo):
```json
{
  "ia": "DEA",
  "recomendaciones": [
    {
      "titulo": "Cámara Digital 4K",
      "descripcion": "...",
      "precio": 49.99,
      "url": "https://regalidea.es/products/camara-digital-4k"
    }
  ],
  "mensaje_final": "🌟 Gracias por confiar en regalidea.es..."
}
```

---

## 📦 Estructura del proyecto

```
main.py                    # Código principal FastAPI
catalogo_regalidea.json    # Catálogo de productos
requirements.txt           # Dependencias
Procfile                   # Comando para Railway
README.md                  # Este archivo
```

---

## 🛠️ Deployment recomendado

- Railway: conecta este repo y despliega automáticamente.
- Configura `Procfile` con:
  ```
  web: uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

---

## 🧠 Autores y créditos

Desarrollado por Antonio Selles y LOGIX (IA backend @ REGALIDEA.ES)