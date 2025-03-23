# Aplicație client DNS

## Prezentare generală

Aplicația client DNS este un instrument de linie de comandă care permite utilizatorilor să efectueze căutări DNS și căutări inverse DNS. Acceptă atât serverele DNS implicite de sistem, cât și serverele DNS personalizate specificate de utilizator. Aplicația este scrisă în Python și folosește biblioteca `dnspython` pentru interogări DNS avansate.

---

## Caracteristici

1. **Domeniu la rezoluție IP**:
 - Rezolvați un nume de domeniu la adresele IP corespunzătoare (atât IPv4, cât și IPv6).
 - Suportă mai multe adrese IP pentru domenii cu mai multe înregistrări A/AAAA.

2. **Rezoluție IP la domeniu**:
 - Efectuați căutări inverse DNS pentru a găsi numele de domeniu asociate cu o adresă IP.
 - Suportă mai multe domenii pentru IP-uri cu mai multe înregistrări PTR.

3. **Server DNS personalizat**:
 - Comutați la un server DNS personalizat pentru toate interogările ulterioare.
 - Validați serverul DNS personalizat înainte de utilizare.

4. **Gestionarea erorilor**:
 - Se ocupă de IP-uri de server DNS invalide, servere DNS inaccesibile și timeout-uri de interogare DNS.
 - Afișează mesaje de eroare adecvate pentru rezoluțiile eșuate.

5. **Interfață ușor de utilizat**:
 - Interfață simplă de linie de comandă cu instrucțiuni clare.
 - Suportă atât utilizarea interactivă, cât și bazată pe comandă.

---

## Instalare

### Cerințe preliminare

- Python 3.6 sau o versiune ulterioară
- biblioteca `dnspython`

### Pași

1. Clonați depozitul sau descărcați scriptul:
 ```bash
 git clone https://github.com/your-repo/dns-client.git
 cd dns-client
 ```

2. Instalați dependența necesară:
 ```bash
 pip install dnspython
 ```

3. Rulați aplicația:
 ```bash
 python dns_client.py
 ```

---

## Utilizare

### Comenzi

Aplicația acceptă următoarele comenzi:

1. **Rezolvați un domeniu sau IP**:
 ```
 rezolva <domeniu sau ip>
 ```
 - Rezolvă un nume de domeniu la adresele sale IP sau o adresă IP la numele (numele) de domeniu.
 - Exemplu:
 ```
 > rezolvați google.com
 IP-uri:
 142.250.187.206
 2607:f8b0:4004:815::200e
 ```

2. **Schimbați serverul DNS**:
 ```
 utilizați dns <ip>
 ```
 - Modifică serverul DNS utilizat pentru toate interogările ulterioare.
 - Exemplu:
 ```
 > utilizați dns 8.8.8.8
 Serverul DNS a fost schimbat la 8.8.8.8
 ```

3. **Ieșiți din aplicație**:
 - Apăsați `Ctrl+C` pentru a ieși din aplicație.

---

## Exemple

### Exemplul 1: Rezolvarea unui domeniu
```
> rezolvați google.com
IP-uri:
142.250.187.206
2607:f8b0:4004:815::200e
```

### Exemplul 2: Rezolvarea unui IP
```
> rezolvați 8.8.8.8
Domenii:
dns.google.
```

### Exemplul 3: Schimbarea serverului DNS
```
> utilizați dns 1.1.1.1
Serverul DNS a fost schimbat la 1.1.1.1
```

### Exemplul 4: Gestionarea erorilor
```
> rezolvați invalid.domain
Erori:
 - Domeniul nu a fost găsit.

> utilizați dns 192.168.0.999
Eroare: format de adresă IP nevalid
```

---

## Mesaje de eroare

Aplicația oferă mesaje de eroare clare pentru diferite scenarii:

1. **IP server DNS nevalid**:
 ```
 Eroare: format de adresă IP nevalid
 ```

2. **Server DNS inaccesibil**:
 ```
 Eroare: serverul DNS este inaccesibil sau nu răspunde
 ```

3. **Domeniul nu a fost găsit**:
 ```
 Erori:
 - Domeniul nu a fost găsit.
 ```

4. **Nu au fost găsite înregistrări PTR**:
 ```
 Erori:
 - Nu au fost găsite înregistrări PTR.
 ```

5. **Expirare interogare DNS**:
 ```
 Erori:
 - Interogarea DNS a expirat.
 ```

---

## Detalii tehnice

### Dependențe

- **`dnspython`**: Un set de instrumente DNS puternic pentru Python, folosit pentru interogări DNS avansate.
- **`socket`**: un modul Python încorporat folosit pentru rezoluția DNS a sistemului.

### Structura codului

- **Bucla principală**:
 - Citește intrarea utilizatorului și procesează comenzi.
 - Gestionează comenzile `resolve` și `use dns`.

- **Funcții de rezoluție**:
 - `resolve_domain_system`: rezolvă domenii folosind DNS-ul sistemului.
 - `resolve_ip_system`: Rezolvă IP-urile utilizând DNS-ul sistemului.
 - `resolve_domain_custom`: rezolvă domenii folosind un server DNS personalizat.
 - `resolve_ip_custom`: rezolvă IP-uri folosind un server DNS personalizat.

- **Funcții de validare**:
 - `is_valid_ip`: validează formatul adresei IP.
 - `validate_dns_server`: Verifică dacă un server DNS este accesibil.