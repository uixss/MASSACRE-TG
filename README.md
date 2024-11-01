# 🎫 Coding Services SEND DM 🎫

# 📊 MASSACRE-TG

Telegram Reporter es una herramienta avanzada para realizar reportes automatizados en Telegram, utilizando múltiples sesiones y proxies para mejorar la eficiencia y evitar bloqueos. Esta herramienta es ideal para manejar grandes volúmenes de reportes mientras se minimizan los riesgos de restricciones y bloqueos por parte de Telegram.

## 🚀 Características

- ✅ **Reportes automáticos**: Envía reportes a usuarios, grupos o canales de Telegram de manera automática, permitiendo la selección de diferentes razones de reporte, como spam, infracción de derechos de autor, contenido falso, y más.
- 🌐 **Gestión de proxies**: Utiliza proxies HTTP, HTTPS y SOCKS para evitar restricciones de IP y asegurar el anonimato durante el proceso de reporte. Los proxies son verificados automáticamente para garantizar que solo se usen proxies válidos.
- 🔄 **Rotación de sesiones**: Permite la rotación de múltiples sesiones de Telegram para minimizar el riesgo de bloqueos de cuenta, distribuyendo los reportes entre varias cuentas.
- 📋 **Reportes detallados**: Obtiene información detallada de los canales, grupos o usuarios objetivo, incluyendo el número de miembros, administradores y otros detalles relevantes.
- ⏱️ **Control de frecuencia**: Ajusta el delay entre cada reporte para evitar errores por exceder los límites de uso (Flood Wait).
- 👥 **Diferenciación de entidades**: Identifica si el objetivo es un canal, grupo o usuario y adapta la lógica de reporte en consecuencia. Si el objetivo es un canal o grupo, se obtiene y reporta a los administradores, además de los mensajes.

## 🔧 Funcionamiento Interno

Telegram Reporter implementa un sistema basado en las siguientes lógicas:

| Funcionalidad               | Descripción                                                                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Carga de Sesiones**       | Las sesiones de Telegram se cargan desde un archivo `vars.txt`, lo cual permite el uso de múltiples cuentas para distribuir los reportes.         |
| **Gestión de Proxies**      | La herramienta obtiene proxies de servicios como `proxyscrape.com`, los cuales son verificados antes de ser utilizados para garantizar calidad.   |
| **Automatización de Reportes** | Utiliza `Telethon` para conectarse a Telegram y enviar reportes a usuarios, grupos o canales con distintas razones de reporte disponibles.       |
| **Rotación de Sesiones y Proxies** | Cada sesión y proxy se usa de forma rotativa para evitar bloqueos y proporcionar anonimato adicional.                                      |
| **Obtención de Administradores**  | Para grupos y canales, obtiene y reporta a los administradores, maximizando el impacto del reporte.                                            |
| **Diferenciación de Entidades**   | Adapta la lógica de reporte según si el objetivo es un canal, grupo o usuario. Obtiene detalles adicionales si es un grupo o canal.          |
| **Manejo de Errores y Retrasos**  | Controla los errores de Flood Wait aplicando retrasos adecuados para evitar que Telegram limite temporalmente la cuenta.                     |

## 📝 Notas

- ⚠️ **Sesiones y proxies**: Asegúrate de configurar correctamente las sesiones y los proxies para evitar errores durante los reportes.
- ⏳ **Flood Wait**: El uso excesivo de reportes puede resultar en un error de `Flood Wait`, bloqueando temporalmente la capacidad de la cuenta. Ajusta el delay para minimizar el riesgo.
- 🔍 **Verificación de Proxies**: No todos los proxies obtenidos son válidos. La herramienta los verifica automáticamente antes de usarlos para garantizar su funcionalidad.



## ⚙️ Requisitos

- 🐍 **Python**: 3.8+
- 📚 **Librerías necesarias**: 
  - `telethon`: Para la interacción con la API de Telegram.
  - `requests`: Para la gestión y verificación de proxies.
  - `asyncio`: Para la ejecución asíncrona de tareas.

## 📦 Instalación

1. 🔧 **Clona este repositorio**:

   ```sh
   git clone https://github.com/tu_usuario/telegram-reporter.git
   cd telegram-reporter
   ```

2. 📥 **Instala las dependencias**:

   ```sh
   pip install -r requirements.txt
   ```

## 🛠️ Contribuciones

💡 ¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la herramienta o encuentras errores, por favor, abre un *issue* o envía un *pull request*. Juntos podemos hacer que Telegram Reporter sea más eficiente y robusto.

## 📄 Licencia

📝 Este proyecto está bajo la licencia MIT.
