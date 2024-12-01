# 📧 MASSACRE TG SMTP

Este proyecto permite verificar, filtrar y utilizar servidores SMTP para el envío masivo de correos electrónicos. Utiliza autenticación segura y maneja reportes dinámicos para maximizar la eficiencia. 🚀

## 🛠️ Funcionalidades

| 🚩 Funcionalidad                     | 📋 Descripción                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------|
| 🔍 Verificación SMTP                | Comprueba credenciales y conectividad de servidores SMTP.                     |
| 🗂️ Agrupación de servidores         | Agrupa servidores válidos en lotes para facilitar la configuración.           |
| ✉️ Envío de correos dinámico         | Genera y envía mensajes personalizados utilizando múltiples servidores.       |
| 📂 Gestión de archivos              | Crea carpetas y copia archivos adicionales para cada lote SMTP.               |
| 🕒 Reportes y registros              | Guarda detalles de los envíos exitosos y errores en archivos JSON y logs.     |

## 🌟 Características Destacadas

- **Concurrente:** Utiliza hilos para procesar múltiples servidores SMTP a la vez. ⚡
- **Personalización:** Mensajes dinámicos generados con detalles específicos de usuarios. 🧩
- **Rotación SMTP:** Maneja múltiples servidores con rotación automática y manejo de lista negra. 🔄
