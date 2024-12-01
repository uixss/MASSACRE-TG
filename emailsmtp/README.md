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

## 📋 Archivos Clave

| 📁 Archivo                | 📋 Descripción                                                     |
|---------------------------|-------------------------------------------------------------------|
| `data.json`               | Lista de servidores SMTP con credenciales para validar.          |
| `config.ini`              | Configuración de nombres, asuntos y tiempo entre envíos.         |
| `report.json`             | Mensajes estáticos para reportar problemas.                      |
| `belito.json`             | Datos válidos de usuarios o entidades a reportar.                |
| `registro_envios.json`    | Registro de todos los correos enviados con detalles.             |

## 🚀 Ejecución

1. 📂 Coloca los archivos requeridos (`data.json`, `config.ini`, etc.) en el directorio raíz.
2. 🏃 Ejecuta el script principal:
   ```bash
   python main.py
   ```
3. 🛠️ Monitorea los logs para revisar los servidores y reportes procesados.

## ⚙️ Requisitos

- Python 3.8 o superior
- Paquetes requeridos:
  ```bash
  pip install -r requirements.txt
  ```
- Configuración inicial en `data.json` y `config.ini`.

## 🌟 Características Destacadas

- **Concurrente:** Utiliza hilos para procesar múltiples servidores SMTP a la vez. ⚡
- **Personalización:** Mensajes dinámicos generados con detalles específicos de usuarios. 🧩
- **Rotación SMTP:** Maneja múltiples servidores con rotación automática y manejo de lista negra. 🔄

---

