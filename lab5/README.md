# Client de Email în Python

Această aplicație este un client simplu de email în Python care poate:

- Lista emailuri din căsuța poștală folosind protocoalele **POP3** și **IMAP**
- Descărca emailuri cu atașamente
- Trimite emailuri text și emailuri cu atașamente
- Seta subiectul și adresa de răspuns (`Reply-To`) la trimitere

## 🛠 Cerințe

- Python 3.10 sau mai nou
- Librării standard Python:
  - `smtplib`
  - `poplib`
  - `imaplib`
  - `email`
  - `os`
  - `ssl`

## 🔧 Instalare

1. Clonează sau descarcă acest proiect.
2. Asigură-te că ai Python instalat.
3. Rulează aplicația:

```bash
python email_client.py
```
