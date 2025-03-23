# Aplicație de Chat folosind TCP Sockets

## Descriere
Acest proiect implementează o aplicație simplă de chat utilizând **sockets TCP** în Python. Este compusă dintr-un **server** și mai mulți **clienți** care se pot conecta la acesta și pot comunica în timp real.

## Funcționalități
- Suportă mai mulți clienți conectați simultan la server
- Clienții pot trimite mesaje către server, care apoi le retransmite tuturor utilizatorilor conectați
- Clienții se pot deconecta în siguranță
- Serverul gestionează erorile de conexiune

## Cerințe
- Python 3.x

## Instalare
Nu sunt necesare dependențe suplimentare. Se folosesc modulele `socket` și `threading` incluse în Python.

## Cum să rulezi aplicația

### 1. Pornește Serverul
Execută următoarea comandă în terminal:
```bash
python server.py
```
Serverul va începe să asculte conexiuni pe `127.0.0.1:12345`.

### 2. Pornește Clientul
Într-un alt terminal, execută:
```bash
python client1.py
```
Acesta se va conecta la server.

Într-un alt terminal, execută:
```bash
python client2.py
```

### 3. Trimite Mesaje
- Scrie un mesaj și apasă **Enter** pentru a-l trimite în chat.
- Mesajele vor fi retransmise tuturor clienților conectați, inclusiv expeditorului.
- Pentru a ieși, tastează `exit` și apasă **Enter**.

## Observații
- Asigură-te că serverul este pornit înainte de a lansa orice client.
- Poți rula mai multe instanțe de client în ferestre diferite ale terminalului pentru a simula utilizatori multipli.
- Dacă serverul se închide, trebuie repornit pentru a permite noi conexiuni.
