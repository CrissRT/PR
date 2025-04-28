import requests
import json

BASE_URL = 'http://localhost:5000'  # înlocuiește cu URL-ul serverului tău

def list_categories():
    response = requests.get(f'{BASE_URL}/categories')
    if response.ok:
        categories = response.json()
        print("Categorii disponibile:")
        for cat in categories:
            print(f"- {cat['id']}: {cat['title']}")
    else:
        print("Eroare la preluarea categoriilor!")

def category_details():
    cat_id = input("Introduceți ID-ul categoriei: ")
    response = requests.get(f'{BASE_URL}/categories/{cat_id}')
    if response.ok:
        category = response.json()
        print(json.dumps(category, indent=4))
    else:
        print("Categoria nu a fost găsită.")

def create_category():
    title = input("Introduceți titlul noii categorii: ")
    data = {
        "title": title
    }
    response = requests.post(f'{BASE_URL}/categories', json=data)
    if response.ok:
        print("Categorie creată cu succes.")
    else:
        print("Eroare la crearea categoriei.")

def delete_category():
    cat_id = input("Introduceți ID-ul categoriei de șters: ")
    response = requests.delete(f'{BASE_URL}/categories/{cat_id}')
    if response.ok:
        print("Categorie ștearsă cu succes.")
    else:
        print("Eroare la ștergerea categoriei.")

def update_category_title():
    cat_id = input("Introduceți ID-ul categoriei de modificat: ")
    new_title = input("Introduceți noul titlu: ")
    data = {
        "title": new_title
    }
    response = requests.put(f'{BASE_URL}/categories/{cat_id}', json=data)
    if response.ok:
        print("Titlul categoriei a fost modificat.")
    else:
        print("Eroare la modificarea categoriei.")

def create_product():
    cat_id = input("Introduceți ID-ul categoriei unde adăugăm produsul: ")
    name = input("Introduceți numele produsului: ")
    price = input("Introduceți prețul produsului: ")
    data = {
        "name": name,
        "price": float(price)
    }
    response = requests.post(f'{BASE_URL}/categories/{cat_id}/products', json=data)
    if response.ok:
        print("Produs creat cu succes.")
    else:
        print("Eroare la crearea produsului.")

def list_products_in_category():
    cat_id = input("Introduceți ID-ul categoriei: ")
    response = requests.get(f'{BASE_URL}/categories/{cat_id}/products')
    if response.ok:
        products = response.json()
        print(f"Produsele din categoria {cat_id}:")
        for prod in products:
            print(f"- {prod['id']}: {prod['name']} - {prod['price']} lei")
    else:
        print("Eroare la preluarea produselor.")

def main():
    while True:
        print("\n--- Magazin Online ---")
        print("1. Listează categorii")
        print("2. Afișează detalii categorie")
        print("3. Creează categorie")
        print("4. Șterge categorie")
        print("5. Modifică titlu categorie")
        print("6. Creează produs într-o categorie")
        print("7. Listează produse dintr-o categorie")
        print("8. Ieșire")

        choice = input("Alegeți o opțiune: ")

        if choice == '1':
            list_categories()
        elif choice == '2':
            category_details()
        elif choice == '3':
            create_category()
        elif choice == '4':
            delete_category()
        elif choice == '5':
            update_category_title()
        elif choice == '6':
            create_product()
        elif choice == '7':
            list_products_in_category()
        elif choice == '8':
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă, încercați din nou.")

if __name__ == "__main__":
    main()
