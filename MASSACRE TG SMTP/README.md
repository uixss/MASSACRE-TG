# 📧 MASSACRE TG SMTP 

Envio de reportes en masa al email@soporte

    sms@telegram.org
    dmca@telegram.org
    abuse@telegram.org
    sticker@telegram.org
    stopCA@telegram.org
    recover@telegram.org
    support@telegram.org
    security@telegram.org

### 🚀 Funcionalidades Clave

- **🔍 Verificación SMTP**  
  Comprueba credenciales y conectividad de servidores SMTP.  

- **🗂️ Agrupación de servidores**  
  Clasifica servidores válidos en lotes para facilitar la configuración.  

- **✉️ Envío de correos dinámico**  
  Genera y envía mensajes personalizados utilizando múltiples servidores SMTP con encabezados y pies de página aleatorios.
  
- **📂 Gestión de archivos**  
  Crea carpetas y copia archivos adicionales para cada lote SMTP.  

- **📈 Escalabilidad**  
  Diseñado para manejar grandes volúmenes de servidores SMTP y destinatarios.  

- **🔄 Rotación inteligente de servidores**  
  Gestiona una lista rotativa de servidores SMTP para evitar bloqueos o saturaciones.  

- **🗃️ Gestión de reportes completa**  
  Almacena registros detallados de cada envío para análisis posterior.

📧 El mensaje se genera dinámicamente

```python
import random

headers = [
    "Dear Telegram Compliance Monitoring Team,",
    "Hello Telegram Policy Team,",
    "To the Telegram Trust Enforcement Team,",
]

footers = [
    "Warmly,",
    "With heartfelt thanks,",
    "Ever grateful,",
]

static_message = "We have detected irregular activity in the following account."
details = "Account ID: 123456"

header = random.choice(headers)
footer = random.choice(footers)
message = f"""{header}\n\n{static_message}\n\n{details}\n\n{footer}\nBye"""

```
<br>

<div style="display: flex; justify-content: space-between; align-items: center;">
    <img src="../img/letter.png" alt="MASSACRE_SMTP_1" width="400" height="500">
    <img src="../img/imbox.png" alt="MASSACRE_SMTP_2" width="425" height="500">
</div> <br><br> 
