# HTTP Client Console Application

## Descriere

Această aplicație de consolă scrisă în Python permite comunicarea cu un server HTTP ce simulează un magazin online.
Aplicația utilizează HTTP requests pentru a enumera, crea, modifica și șterge categorii și produse.

Este o aplicație didactică, realizată în scopul înțelegerii următoarelor concepte:

- Cum se efectuează HTTP requests în Python
- Cum se serializează și deserializează obiecte (JSON)
- Cum se construiește un client HTTP funcțional

---

## Funcționalități

Aplicația permite utilizatorului să:

- ✅ **Enumere lista de categorii** (`GET /categories`)
- ✅ **Vizualizeze detalii despre o categorie** (`GET /categories/{id}`)
- ✅ **Creeze o categorie nouă** (`POST /categories`)
- ✅ **Șteargă o categorie existentă** (`DELETE /categories/{id}`)
- ✅ **Modifice titlul unei categorii** (`PUT /categories/{id}`)
- ✅ **Adauge produse noi într-o categorie** (`POST /categories/{id}/products`)
- ✅ **Vizualizeze lista produselor dintr-o categorie** (`GET /categories/{id}/products`)

---

## Tehnologii Utilizate

- **Python 3.10+**
- **requests** (librărie pentru HTTP client)
- **json** (pentru serializare și deserializare date)

---

## Instalare

1. Creează un mediu virtual (opțional, dar recomandat):

   ```bash
   python -m venv venv
   source venv/bin/activate  # pentru Linux/Mac
   venv\Scripts\activate     # pentru Windows
   ```

2. Instalează dependințele:
   ```bash
   pip install -r requirements.txt
   ```

---

## Rulare

După instalarea dependențelor, poți rula aplicația cu:

```bash
python main.py
```

Aplicația va afișa un meniu interactiv în consolă, unde poți selecta acțiunile dorite:

```
1. Listează categorii
2. Afișează detalii categorie
3. Creează categorie nouă
4. Șterge categorie
5. Modifică titlul unei categorii
6. Adaugă produs într-o categorie
7. Listează produsele dintr-o categorie
8. Ieșire
```

---

## Structura Proiectului

```
http-client-console-app/
├── http-client.py
├── server.txt
└── README.md
```

---

## Exemple de Request-uri

- **Obținere categorii**

  ```python
  response = requests.get('http://localhost:8000/categories')
  ```

- **Creare categorie nouă**

  ```python
  data = {"title": "Electronice"}
  response = requests.post('http://localhost:8000/categories', json=data)
  ```

- **Actualizare categorie**

  ```python
  data = {"title": "Electrocasnice"}
  response = requests.put('http://localhost:8000/categories/1', json=data)
  ```

- **Ștergere categorie**

  ```python
  response = requests.delete('http://localhost:8000/categories/1')
  ```

- **Creare produs într-o categorie**
  ```python
  data = {"name": "Laptop", "price": 3000}
  response = requests.post('http://localhost:8000/categories/1/products', json=data)
  ```

---

## Cerințe Minime Server

Aplicația presupune existența unui server HTTP compatibil, care oferă următoarele endpoint-uri:

- `GET /categories`
- `GET /categories/{id}`
- `POST /categories`
- `PUT /categories/{id}`
- `DELETE /categories/{id}`
- `GET /categories/{id}/products`
- `POST /categories/{id}/products`
