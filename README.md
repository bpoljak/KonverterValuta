# Konverter Valuta

Aplikacija omogućuje jednostavnu konverziju iznosa iz jedne valute u drugu koristeći ažurirane tečajeve. Prilagođena je za korisnike koji žele brzo i intuitivno iskustvo konverzije valuta putem grafičkog sučelja izrađenog u Tkinteru.

## Značajke
- **Podrška za dvije verzije API-ja:**
  - **HNB API:** Dohvaća tečajeve iz Hrvatske narodne banke.
  - **Exchangerate API:** Koristi globalne podatke o tečajevima valuta.
- Unos iznosa za konverziju i prikaz krajnjeg iznosa.
- Automatsko dohvaćanje tečajeva valuta.
- Prikaz trenutnog tečaja za odabranu valutu.
- Jednostavno i intuitivno grafičko korisničko sučelje.

## Instalacija

### Preduvjeti
- **Python 3.7** ili novija verzija mora biti instalirana na vašem sustavu.
- **Pip** (Python Package Installer) za instalaciju ovisnosti.

### Koraci
1. Klonirajte repozitorij:
   git clone https://github.com/bpoljak/KonverterValuta.git
   cd KonverterValuta
   
2. Instalirajte potrebne ovisnosti:
   Pokrenite sljedeću naredbu kako biste instalirali sve potrebne ovisnosti navedene u datoteci `requirements.txt`:

   pip install -r requirements.txt
   
## Pokretanje

### Pokretanje Python skripte
Aplikaciju možete pokrenuti izravno pomoću Pythona:

python konverter_valuta.py

## API Informacije

### HNB API
- **URL:** [https://api.hnb.hr/tecajn-eur/v3](https://api.hnb.hr/tecajn-eur/v3)
- Koristi srednji tečaj za EUR kao baznu valutu.

### Exchangerate API
- **URL:** [https://api.exchangerate-api.com/v4/latest/EUR](https://api.exchangerate-api.com/v4/latest/EUR)
- Globalna podrška za različite valute.

## Struktura projekta

- `konverter_valuta.py`: Skripta aplikacije koja koristi Exchangerate API.
- `konverter_valuta_hnb.py`: Alternativna verzija koja koristi HNB API.
- `main.spec`: Konfiguracijska datoteka za PyInstaller za izradu izvršnih datoteka.
- `dist/`: Direktorij koji sadrži generirane binarne datoteke.

## Kako koristiti aplikaciju

1. Pokrenite aplikaciju.
2. Odaberite valutu koju želite konvertirati.
3. Unesite iznos za konverziju.
4. Odaberite ciljnu valutu.
5. Pogledajte izračunati iznos u polju rezultata.

## Napomena

Aplikacija je izrađena za kolegij **Objektno orijentirano programiranje** u ljetnom semestru 2022. godine.
