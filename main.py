"""
Envio de e-mail via SMTP (smtplib). Esse método não funciona com outlook, que possui um método um pouco diferente.
"""

# permite fazer o login/envio de e-mail pelo protocolo, sem precisar fazer login na máquina física
import smtplib

# é onde a mensagem do e-mail será construida
import email.message

# senha ficticia
senha = 123456

lista_usuarios = [
    {
        "Usuario": "Leonardo",
        "Destinatario": "Destinatario teste",
        "From": "leonardo@gmail.com",
        "To": "destinatario@gmail.com",
        "Cc": "emailcopia@gmail.com",
        "Bcc": "emailcopiaoculta@gmail.com",
        "Subject": "Commodo sint laboris ut id. Consequat dolore ex reprehenderit mollit. Commodo cillum labore enim deserunt elit non sunt anim.",
    },
    {
        "Usuario": "Usuario Teste",
        "Destinatario": "Destinatario teste",
        "From": "teste@gmail.com",
        "To": "destinatario@gmail.com",
        "Cc": "emailcopia@gmail.com",
        "Bcc": "emailcopiaoculta@gmail.com",
        "Subject": "Commodo sint laboris ut id. Consequat dolore ex reprehenderit mollit. Commodo cillum labore enim deserunt elit non sunt anim.",
    },
]


def enviar_email(lista, senha):
    for usuario in lista:
        msg = email.message.Message()
        msg["Subject"] = usuario["Subject"]
        msg["From"] = usuario["From"]
        msg["To"] = usuario["To"]
        msg["Cc"] = usuario["Cc"]
        msg["Bcc"] = usuario["Bcc"]
        usuario_remetente = usuario["Usuario"]
        usuario_destinatario = usuario["Destinatario"]

        corpo_email = criar_corpo_email(
            usuario_destinatario, msg["Subject"], usuario_remetente
        )

        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo_email)
        conexao_servidor(msg["From"], senha, msg)
        print(f"E-mail enviado com sucesso de {msg['From']} para {msg['To']}")


def criar_corpo_email(destinatario, assunto, remetente):
    corpo_email = f"""
        <p>Boa tarde, {destinatario}.</p>
        <p>{assunto}</p>
        <p>Att., {remetente}</p>
        """
    corpo_email = corpo_email.encode("utf-8")

    return corpo_email


def conexao_servidor(email_remetente, senha_remetente, mensagem):
    # estabelece conexão com o servidor
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    # criptografa as informacoes dentro do servidor
    servidor.starttls()
    # ATENÇÃO: Não é recomendado, DE FORMA ALGUMA, deixar a senha exposta. Consulte README.md
    servidor.login(email_remetente, senha_remetente)
    servidor.send_message(mensagem)
    servidor.quit()


enviar_email(lista_usuarios)
