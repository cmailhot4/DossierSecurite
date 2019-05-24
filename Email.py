import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envoyer_email(emailSource, mpSource, emailCible):
    emailDepart = emailSource
    emailDestination = emailCible
    password = mpSource

    texte = MIMEMultipart()
    texte["Subject"] = "Modification mot de passe Omnivox"
    texte["From"] = emailDepart
    texte["To"] = emailDestination

    message = """\
    Bonjour,

    Il semble que quelqu'un se soit connecté à votre compte Omnivox en provenance de: Arabie Saoudite, jeudi 09/05/19.
    Cliquer sur le lien ci-dessous pour réinitialiser votre mot de passe et ainsi protéger votre compte.
    https://cmailhot4.github.io/DossierSecurite/Hameconnage/  
    
    Cordialement,
    L'équipe de soutient Omnivox."""
    messageAEnvoyer = MIMEText(message, "plain")
    texte.attach(messageAEnvoyer)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(emailSource, password)
        server.sendmail(emailSource, emailDestination, texte.as_string())
