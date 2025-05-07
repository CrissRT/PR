import ntplib
from datetime import datetime, timedelta
import time

def get_ntp_time(ntp_server="pool.ntp.org"):
    """
    Returnează ora exactă UTC de la un server NTP.
    """
    client = ntplib.NTPClient()
    try:
        response = client.request(ntp_server, version=3)
        # response.tx_time este timpul transmis de server
        utc_time = datetime.utcfromtimestamp(response.tx_time)
        return utc_time
    except Exception as e:
        print(f"Eroare la conectarea la serverul NTP: {e}")
        return None

def get_timezone_offset(timezone_input):
    """
    Parsează stringul de forma 'GMT+X' sau 'GMT-X' și returnează offsetul ca int.
    """
    if not timezone_input.startswith('GMT'):
        raise ValueError("Format invalid. Trebuie să înceapă cu 'GMT'.")
    
    sign = timezone_input[3]
    if sign not in ('+', '-'):
        raise ValueError("Semn invalid. Trebuie să fie '+' sau '-' după 'GMT'.")
    
    try:
        offset = int(timezone_input[4:])
    except ValueError:
        raise ValueError("Ora trebuie să fie un număr întreg după semn.")
    
    if offset < 0 or offset > 11:
        raise ValueError("Offset-ul trebuie să fie între 0 și 11.")
    
    if sign == '-':
        offset = -offset
    
    return offset

def main():
    print("=== Aplicație Client NTP ===")
    timezone_input = input("Introdu zona geografică (format 'GMT+X' sau 'GMT-X', unde X între 0 și 11): ").strip()

    try:
        offset = get_timezone_offset(timezone_input)
    except ValueError as ve:
        print(f"Eroare: {ve}")
        return

    utc_time = get_ntp_time()
    if utc_time is None:
        print("Nu s-a putut obține timpul de la serverul NTP.")
        return

    # Ajustăm timpul UTC cu offsetul utilizatorului
    local_time = utc_time + timedelta(hours=offset)

    print(f"\nOra exactă pentru {timezone_input} este: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
