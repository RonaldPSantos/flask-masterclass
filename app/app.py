from flask import Flask, render_template
from flask_mail import Mail, Message

config = {
    "MAIL_SERVER": "smtp.ethereal.email",
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_DEBUG": True,
    "MAIL_USERNAME": "candice.wunsch@ethereal.email",
    "MAIL_PASSWORD": "V5V9MbB5zKXdv2pVCA",
    "MAIL_DEFAULT_SENDER": "SG Informatica <oi@spacedevs.com.br>"
}

app = Flask(__name__)
app.config.update(config)
mail = Mail(app)


@app.route("/sendmail")
def sendmail():
    msg = Message(
        subject="Bem vindo(a)",
        sender=app.config["MAIL_DEFAULT_SENDER"],
        recipients=["ronaldpsantos@outlook.com"],
        html=render_template("mail/welcome.html", name="Ronald")
    )

    mail.send(msg)
    return "E-mail enviado com sucesso!"


if __name__ == "__main__":
    app.run(debug=True)
