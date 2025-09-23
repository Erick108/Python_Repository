import smtplib
from dotenv import load_dotenv
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Practica para enviar correo electronico desde Python

load_dotenv()

host = os.getenv("HOST_MAIL")
puerto =  os.getenv("PUERTO_MAIL")
user = os.getenv("MAIL_USER")
contra = os.getenv("MAIL_PASSWORD")

if host is None or puerto is None or user is None or contra is None:
    raise ValueError ("❌ Alguna variable no está definida o es mal escrita en el .env")

destinatario = "yimu2104@gmail.com"
#destinatario = ["04karenportillo@gmail.com", "yimu2104@gmail.com", "rubiomoises27@icloud.com"] #"erickrivera.v109@gmail.com"
asunto = "Prueba de archivo adjunto"
cuerpo = "Enviando archivo adjunto solicitado"

mensaje = MIMEMultipart()
mensaje["From"] = user
mensaje["To"] = destinatario
mensaje["Subject"] = asunto
mensaje.attach(MIMEText(cuerpo, 'plain'))

ruta_archivo = "Wasa.jpg"
nombre_archivo = os.path.basename(ruta_archivo)

with open(nombre_archivo, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition"
                ,f"attatchment;filename={nombre_archivo}")
mensaje.attach(part)

with smtplib.SMTP(host, puerto) as server:
    server.starttls()
    server.login(user, contra)
    server.sendmail(user, destinatario, mensaje.as_string())
