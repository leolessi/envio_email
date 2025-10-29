"""
Envio de e-mail via SMTP (smtplib). Esse método não funciona com outlook, que possui um método um pouco diferente.
"""

# permite fazer o login/envio de e-mail pelo protocolo, sem precisar fazer login na máquina física
import smtplib

# é onde a mensagem do e-mail será construida
import email.message


lista_usuarios = [
    {
        "Usuario": "Leonardo",
        "From": "leonardo@email.com",
        "To": "destinatario@email.com",
        "Cc": "emailcopia@email.com",
        "Bcc": "emailcopiaoculta@email.com",
        "Subject": "Commodo sint laboris ut id. Consequat dolore ex reprehenderit mollit. Commodo cillum labore enim deserunt elit non sunt anim.",
    }
]


def enviar_email():
    msg = email.message.Message()
    msg["Subject"] = (
        "Assunto do e-mail. Duis cillum cillum non cillum ullamco aute cillum irure tempor dolore id adipisicing. Ex fugiat aute nostrud do dolore ipsum commodo. Ut labore qui adipisicing incididunt voluptate voluptate est. Sunt proident aliqua ut ad sint ullamco. Fugiat culpa commodo commodo in minim eu minim ex esse."
    )
    msg["From"] = "emaildoremetente@gmail.com"
    msg["To"] = "emaildodestinatario@gmail.com"
    msg["Cc"] = "emaildocopia@gmail.com; emaildoremetente+copia@gmail.com"
    msg["Bcc"] = "emaildocopiaoculta@gmail.com"

    corpo_email = """
    <p>Boa tarde, destinatário.</p>
    <p>Mollit ea incididunt excepteur exercitation incididunt cillum cillum reprehenderit labore commodo. Id do minim aliqua quis mollit incididunt quis consectetur quis nisi ut ex cillum aliqua. Veniam deserunt deserunt mollit esse culpa occaecat dolor velit. Officia cupidatat dolor ex consectetur aliquip deserunt reprehenderit aliquip mollit mollit pariatur. Ullamco est cillum veniam velit excepteur aliquip minim. Non sint qui aute in cupidatat aliquip.</p>
    <p>Att., Remetente</p>
    """

    corpo_email = corpo_email.encode("utf-8")

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

    # estabelece conexão com o servidor
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    # criptografa as informacoes dentro do servidor
    servidor.starttls()
    # ATENÇÃO: Não é recomendado, DE FORMA ALGUMA, deixar a senha exposta. Consulte README.md
    servidor.login(msg["From"], "senha_envio_emails")
    servidor.send_message(msg)
    servidor.quit()
    print(f"E-mail enviado com sucesso de {msg['From']} para {msg['To']}")


enviar_email()
