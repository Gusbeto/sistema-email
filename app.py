from flask import Flask, request, send_file
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# ⚠️ Configure isso com seu e-mail e senha de app
EMAIL_ORIGEM = "beto2020ra@gmail.com"
SENHA = "Beto2020ra!Beto2020ra!"
EMAIL_DESTINO = "beto2020ra@gmail.com"

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    data = request.get_json()
    texto = data.get("texto", "")

    if texto.strip():
        enviar_email("Texto Digitado", texto)

    return "Texto recebido com sucesso!"

def enviar_email(assunto, corpo):
    msg = MIMEText(corpo)
    msg["Subject"] = assunto
    msg["From"] = EMAIL_ORIGEM
    msg["To"] = EMAIL_DESTINO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ORIGEM, SENHA)
        server.send_message(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
