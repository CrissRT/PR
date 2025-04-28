import imaplib
import poplib
import smtplib
import email
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailClient:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.imap_server = "imap.gmail.com"
        self.pop3_server = "pop.gmail.com"

    def list_emails_pop3(self):
        print("Conectare la serverul POP3...")
        server = poplib.POP3_SSL(self.pop3_server)
        server.user(self.email_address)
        server.pass_(self.password)

        num_messages = len(server.list()[1])
        print(f"Număr total de mesaje (POP3): {num_messages}")

        for i in range(num_messages):
            raw_email = b"\n".join(server.retr(i + 1)[1])
            parsed_email = email.message_from_bytes(raw_email)
            print(f"From: {parsed_email['From']}")
            print(f"Subject: {parsed_email['Subject']}\n")
        
        server.quit()

    def list_emails_imap(self):
        print("Conectare la serverul IMAP...")
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_address, self.password)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()

        print(f"Număr total de mesaje (IMAP): {len(mail_ids)}")

        for num in mail_ids[-10:]:  # Ultimele 10 emailuri
            result, data = mail.fetch(num, "(RFC822)")
            raw_email = data[0][1]
            parsed_email = email.message_from_bytes(raw_email)
            print(f"From: {parsed_email['From']}")
            print(f"Subject: {parsed_email['Subject']}\n")
        
        mail.logout()

    def download_email_with_attachments(self, email_index=0, folder='downloads'):
        print("Conectare la serverul IMAP pentru descărcare...")
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_address, self.password)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()
        
        if not os.path.exists(folder):
            os.makedirs(folder)

        email_id = mail_ids[email_index]
        result, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        parsed_email = email.message_from_bytes(raw_email)

        print(f"Descarcăm email de la: {parsed_email['From']}, Subiect: {parsed_email['Subject']}")

        for part in parsed_email.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            if filename:
                filepath = os.path.join(folder, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                print(f"Atașament salvat: {filepath}")

        mail.logout()

    def send_email(self, to_address, subject, body_text, reply_to=None, attachment_path=None):
        print("Trimitere email...")

        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_address
        msg['Subject'] = subject
        if reply_to:
            msg.add_header('Reply-To', reply_to)

        msg.attach(MIMEText(body_text, 'plain'))

        if attachment_path:
            filename = os.path.basename(attachment_path)
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(part)

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email_address, self.password)
        server.send_message(msg)
        server.quit()

        print("Email trimis cu succes!")


if __name__ == "__main__":
    email_address = input("Gmail Address: ")
    password = input("App Password: ")  # nu parola normală!!

    client = EmailClient(email_address, password)

    # Listăm emailuri cu POP3
    try:
        client.list_emails_pop3()
    except Exception as e:
        print(f"Eroare la listarea emailurilor cu POP3: {e}")

    # Listăm emailuri cu IMAP
    try:
        client.list_emails_imap()
    except Exception as e:
        print(f"Eroare la listarea emailurilor cu IMAP: {e}")

    # Descarcăm un email cu atașamente
    try:
        client.download_email_with_attachments(email_index=0, folder='downloads')
    except Exception as e:
        print(f"Eroare la descărcarea emailului: {e}")

    # Trimitem un email simplu
    try:
        client.send_email(
        to_address="diteg16674@ingitel.com",
        subject="Salutare!",
        body_text="Acesta este un email trimis din Python.",
        )
    except Exception as e:
        print(f"Eroare la trimiterea emailului: {e}")

    # Trimitem email cu atașament
    try:
        client.send_email(
        to_address="diteg16674@ingitel.com",
        subject="Email cu atașament",
        body_text="Atașez un fișier.",
        attachment_path="sql.txt"
    )
    except Exception as e:
        print(f"Eroare la trimiterea emailului cu atașament: {e}")
