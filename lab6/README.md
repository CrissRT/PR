# README.md

````markdown
# Aplicație Client NTP în Python

## Descriere

Această aplicație permite utilizatorului să introducă o zonă geografică în format `"GMT+X"` sau `"GMT-X"` (unde `X` este între 0 și 11) și afișează ora exactă pentru acea zonă, obținută de la un server NTP (Network Time Protocol).

Aplicația folosește protocolul NTP pentru a sincroniza ora exactă și ajustează ora UTC în funcție de fusul orar introdus de utilizator.

---

## Funcționalități

- Solicită zona geografică de la utilizator (`GMT+X` sau `GMT-X`).
- Se conectează la un server NTP (`pool.ntp.org`) pentru a obține ora exactă UTC.
- Ajustează ora UTC în funcție de fusul orar introdus.
- Afișează ora locală corectă pentru fusul orar specificat.
- Tratament de erori pentru input invalid și probleme de conectare.

---

## Instalare

### 1. Instalare dependințe

Asigură-te că ai Python 3 instalat.

Instalează biblioteca necesară:

```bash
pip install ntplib
```
````

---

## Cum se rulează aplicația

1. Deschide terminalul.
2. Navighează către folderul proiectului.
3. Rulează aplicația:

```bash
python ntp_client.py
```

4. Introdu zona geografică când aplicația solicită, de exemplu:

```
GMT+2
```

sau

```
GMT-5
```

Aplicația va afișa ora exactă pentru fusul orar introdus.

---

## Exemple de utilizare

```bash
=== Aplicație Client NTP ===
Introdu zona geografică (format 'GMT+X' sau 'GMT-X', unde X între 0 și 11): GMT+3

Ora exactă pentru GMT+3 este: 2025-04-28 19:45:10
```

---

## Structură fișiere

```
index.py   # Codul sursă principal
README.md       # Documentația proiectului
```

---

## Cerințe

- Python 3.7 sau mai nou
- Internet activ (pentru conectarea la serverul NTP)
- Biblioteca Python `ntplib`

---

## Probleme frecvente

| Problemă                            | Cauză                                                   | Soluție                                                  |
| :---------------------------------- | :------------------------------------------------------ | :------------------------------------------------------- |
| Eroare de conectare la serverul NTP | Lipsă conexiune internet sau server NTP inaccesibil     | Verifică conexiunea internet sau încearcă alt server NTP |
| Format greșit al fusului orar       | Zona introdusă nu respectă formatul `GMT+X` sau `GMT-X` | Introdu corect zona geografică, ex: `GMT+2`, `GMT-5`     |
