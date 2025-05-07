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

> **Important:**  
> Fișierul nu trebuie să se numească `email.py` pentru a evita conflicte cu librăria standard Python `email`.

## 🔑 Autentificare Gmail

Pentru a folosi aplicația cu Gmail:

1. Activează **Less Secure Apps** *(sau creează o parolă de aplicație dacă ai 2FA activ)*.
2. Setează emailul și parola în cod sau folosește input la runtime.

Alternativ, folosește autentificare OAuth2 pentru mai multă securitate (neimplementat în această versiune simplă).

---

## ⚙️ Funcționalități

### 1. Listare Emailuri - POP3
- Conectează-te la serverul POP3 Gmail (`pop.gmail.com`)
- Afișează lista emailurilor disponibile

### 2. Listare Emailuri - IMAP
- Conectează-te la serverul IMAP Gmail (`imap.gmail.com`)
- Listează foldere și emailuri
- Permite selectarea unui email

### 3. Descărcare Email + Atașamente
- Descarcă corpul emailului
- Salvează automat atașamentele local

### 4. Trimitere Email Text
- Trimite email simplu doar cu corp text

### 5. Trimitere Email cu Atașament
- Trimite email text + unul sau mai multe fișiere atașate

### 6. Subiect și Reply-To
- Permite setarea subiectului emailului
- Permite adăugarea headerului `Reply-To`

---

## 🌐 Servere utilizate

| Protocol | Server | Port |
|:---------|:-------|:-----|
| SMTP     | smtp.gmail.com | 465 (SSL) |
| POP3     | pop.gmail.com | 995 (SSL) |
| IMAP     | imap.gmail.com | 993 (SSL) |

---

## 🧠 Noțiuni cheie

- **SMTP (Simple Mail Transfer Protocol)** – pentru trimiterea emailurilor
- **POP3 (Post Office Protocol 3)** – pentru descărcarea emailurilor de pe server
- **IMAP (Internet Message Access Protocol)** – pentru accesarea emailurilor direct pe server
- **MIME (Multipurpose Internet Mail Extensions)** – pentru formatul emailurilor cu atașamente
- **SSL (Secure Sockets Layer)** – pentru conexiuni securizate

---

## ⚠️ Note

- Pentru trimitere/recepție prin Gmail, poate fi necesar să folosești o **Parolă de Aplicație** dacă ai 2FA activ.
