# Aplicație de Chat UDP

Acest proiect constă într-o implementare simplă a unui server și a unui client de chat bazate pe UDP. Serverul găzduiește o cameră de chat unde mai mulți clienți se pot conecta și comunica în timp real. Clienții trimit mesaje către server, care apoi le transmite tuturor celorlalți clienți conectați.

## Fișiere

1. **`server.py`** - Scriptul serverului care ascultă mesajele primite de la clienți și le transmite tuturor clienților conectați.
2. **`client1.py`** - Script de client care se conectează la server și permite utilizatorului să trimită și să primească mesaje.
3. **`client2.py`** - Un alt script de client, identic cu `client1.py`, utilizat pentru testarea mai multor clienți.

## Cum funcționează

### Server
- Serverul rulează pe `127.0.0.1` (localhost) și ascultă pe portul `5000`.
- Utilizează protocolul UDP (User Datagram Protocol) pentru comunicare.
- Serverul menține un set de clienți conectați și retransmite mesajele primite tuturor clienților, cu excepția expeditorului.
- Dacă un client trimite mesajul `qqq`, serverul elimină acel client din lista de clienți conectați.

### Client
- Fiecare client rulează pe `127.0.0.1`, dar se leagă la un port aleatoriu între `6000` și `10000`.
- Clientul solicită utilizatorului să introducă un nume. Dacă nu este furnizat un nume, se atribuie unul implicit, cum ar fi `Guest1234`.
- Clientul trimite mesaje către server, care sunt apoi retransmise tuturor celorlalți clienți.
- Clientul poate părăsi chatul tastând `qqq`.

## Cerințe preliminare

- Python 3.x

## Rularea aplicației

1. **Pornirea serverului**:
   - Rulează scriptul serverului folosind comanda:
     ```bash
     python server.py
     ```
   - Serverul va porni și va afișa un mesaj care indică faptul că este activ.

2. **Pornirea clienților**:
   - Deschide două sau mai multe ferestre de terminal.
   - În fiecare terminal, rulează unul dintre scripturile client:
     ```bash
     python client1.py
     ```
     sau
     ```bash
     python client2.py
     ```
   - Fiecare client îți va solicita să introduci un nume și apoi îți va permite să trimiți mesaje.

3. **Conversarea**:
   - Mesajele trimise de un client vor fi recepționate de toți ceilalți clienți conectați la server.
   - Pentru a ieși din chat, tastează `qqq`.

## Prezentare generală a codului

### Codul serverului (`server.py`)
- **Funcția `RecvData`** - Primește continuu date de la clienți și le adaugă într-o coadă.
- **Funcția `RunServer`** - Gestionează bucla principală a serverului, manipulând conexiunile clienților și retransmiterea mesajelor.

### Codul clientului (`client1.py` și `client2.py`)
- **Funcția `ReceiveData`** - Primește continuu date de la server și le afișează în consolă.
- **Funcția `RunClient`** - Gestionează bucla principală a clientului, manipulând introducerea utilizatorului și trimiterea mesajelor către server.
