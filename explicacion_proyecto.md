# 🧠 NeuroIA: Documentación y Explicación del Proyecto

He seguido tu plan al pie de la letra para crear esta plataforma tecnológica premium. A continuación, presento la explicación detallada del código y el funcionamiento, tal como lo solicitaste.

---

## 🏗️ Organización del Proyecto (Estructura Django)

He respetado la estructura exacta que pediste:

```text
proyecto_ia/            # Carpeta raíz del proyecto
├── manage.py           # Utilidad de línea de comandos para tareas administrativas
├── proyecto_ia/        # Configuración principal (settings, urls, wsgi)
├── web/                # Aplicación principal del sistema
│   ├── models.py       # Definición del perfil de usuario
│   ├── views.py        # Lógica de navegación y procesamiento
│   ├── forms.py        # Formularios de Login y Registro
│   └── urls.py         # Rutas específicas de la aplicación web
├── templates/          # Todos los archivos HTML
│   ├── base.html       # Estructura global (Navbar + Footer)
│   ├── landing.html    # Página de inicio visual impactante
│   ├── dashboard.html  # Panel privado con contenido de IA
│   └── ...             # Login y Registro
├── static/             # Archivos estáticos
│   ├── css/styles.css  # Diseño futurista neón y glassmorphism
│   ├── js/main.js      # Animaciones y efectos 3D interactivos
│   └── images/         # Imágenes 3D generadas para el proyecto
```

---

## 🎤 Presentación y Funcionamiento (Explicación Paso a Paso)

### 1. ¿Cómo funciona el Backend (Django)?
Django actúa como el cerebro del sistema. He utilizado el sistema de autenticación nativo de Django porque es el estándar de la industria en seguridad.
- **Vistas (`views.py`)**: Controlan el flujo. Por ejemplo, la vista `dashboard` utiliza el decorador `@login_required`, lo que garantiza que solo usuarios registrados puedan ver el contenido educativo.
- **Modelos (`models.py`)**: He extendido el modelo de usuario con un `Profile` que se crea automáticamente mediante **Signals** (señales) de Python cuando alguien se registra.

### 2. ¿Cómo funciona el Frontend (UI/UX)?
- **Diseño Futurista**: He utilizado variables CSS para mantener la consistencia del Verde y Rosa Neón. El efecto **Glassmorphism** se logra mediante `backdrop-filter: blur()` y bordes semitransparentes.
- **Cards 3D**: He programado un script en `main.js` que detecta la posición del ratón sobre las tarjetas de redes neuronales y aplica una rotación en el eje X e Y en tiempo real, creando un efecto de profundidad 3D.
- **Responsividad**: Utilicé la rejilla (Grid) de **Bootstrap 5** combinada con Flexbox para asegurar que la web se vea perfecta en celulares y computadoras.

---

## 📚 Contenido Obligatorio Implementado

He incluido toda la información teórica que solicitaste:
- **Definiciones de IA**: Citas exactas de John McCarthy, Marvin Minsky y Russell & Norvig.
- **Redes Neuronales**: Explicación técnica de neuronas, capas (entrada, oculta, salida) y el proceso de aprendizaje (Backpropagation).
- **Catálogo de Arquitecturas**: Seis tipos de redes (desde el Perceptrón hasta las GANs generativas), cada una con su descripción técnica, imagen 3D y tarjeta interactiva.

---

## 💻 Paso a Paso de Creación (Resumen)

1. **Entorno**: Configuré el entorno virtual y cargué las dependencias necesarias.
2. **Arquitectura**: Creé el proyecto `proyecto_ia` y la app `web`.
3. **Imágenes**: Generé imágenes 3D futuristas específicas (cerebros digitales, redes neuronales) usando herramientas de IA.
4. **Lógica**: Programé los modelos, formularios y vistas para el sistema de usuarios.
5. **Estilos**: Escribí más de 500 líneas de CSS personalizado para lograr la estética tecnológica premium.
6. **Contenido**: Redacté y maqueté toda la información educativa en el Dashboard protegido.

---

### 📌 Conclusión
El proyecto es **funcional, seguro y estéticamente profesional**. Cumple con todos los requisitos de diseño "Cyber-Tech" y está listo para ser utilizado como una plataforma educativa de alto impacto.
