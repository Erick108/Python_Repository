import smtplib
from dotenv import load_dotenv
import os
#Practica para enviar correo electronico desde Python

load_dotenv()

host = os.getenv("HOST_MAIL")
puerto =  os.getenv("PUERTO_MAIL")
user = os.getenv("MAIL_USER")
contra = os.getenv("MAIL_PASSWORD")

if host is None or puerto is None or user is None or contra is None:
    raise ValueError ("❌ Alguna variable no está definida o es mal escrita en el .env")

destinatario = "erickrivera.v109@gmail.com"
#destinatario = ["04karenportillo@gmail.com", "yimu2104@gmail.com", "rubiomoises27@icloud.com"]
asunto = "Prueba"
cuerpo = "Wazzzzzzaaa (Mensaje enviado desde Python)"
mensaje = f"Subject: {asunto}\n\n{cuerpo}"

server = smtplib.SMTP(host, puerto)
server.starttls()
server.login(user, contra)
server.sendmail(user, destinatario, mensaje)
server.quit()
print("Correo enviado de forma exitosa")