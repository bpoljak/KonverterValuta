from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

API_URL = "https://api.hnb.hr/tecajn-eur/v3"

def dohvati_sve_valute():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        podaci = response.json()
        return [{"valuta": el["valuta"], "tecaj": el["srednji_tecaj"]} for el in podaci]
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Greška", f"Neuspješno dohvaćanje valuta: {e}")
        return []

def dohvati_tecaj(valuta):
    valute = dohvati_sve_valute()
    tecaj = next((el for el in valute if el["valuta"] == valuta), None)
    if tecaj:
        return float(tecaj["tecaj"].replace(",", "."))
    else:
        messagebox.showerror("Greška", f"Tečaj za valutu {valuta} nije pronađen.")
        return 0

def konvertiraj():
    krajnji_iznos_entry.delete(0, END)
    ime_valute = unos_vlaute_za_konverziju.get()
    try:
        iznos = float(iznos_entry.get())
        tecaj = dohvati_tecaj(ime_valute)
        if tecaj:
            konv = round(iznos * tecaj, 2)
            krajnji_iznos_entry.insert(0, f"{konv:,.2f}")
        else:
            messagebox.showerror("Greška", "Podaci o tečaju nisu dostupni.")
    except ValueError:
        messagebox.showerror("Greška", "Unesite ispravan broj za iznos.")

def clear():
    iznos_entry.delete(0, END)
    krajnji_iznos_entry.delete(0, END)

def zakljucaj():
    if not vasa_valuta_entry.get() or not unos_vlaute_za_konverziju.get():
        messagebox.showwarning("Pažnja", "Ispunite sva polja!")
        return

    vasa_valuta_entry.config(state="disabled")
    unos_vlaute_za_konverziju.config(state="disabled")
    tecaj = dohvati_tecaj(unos_vlaute_za_konverziju.get())

    if tecaj:
        unos_tecaja.config(state="normal")
        unos_tecaja.delete(0, END)
        unos_tecaja.insert(0, f"1 {vasa_valuta_entry.get()} = {tecaj} {unos_vlaute_za_konverziju.get()}")
        unos_tecaja.config(state="disabled")
        moj_tab.tab(1, state="normal")
    else:
        messagebox.showerror("Greška", "Podaci o tečaju nisu dostupni.")

def otkljucaj():
    vasa_valuta_entry.config(state="normal")
    unos_vlaute_za_konverziju.config(state="normal")
    unos_tecaja.config(state="normal")
    unos_tecaja.delete(0, END)
    unos_tecaja.config(state="disabled")
    moj_tab.tab(1, state="disabled")

root = Tk()
root.title("Konverter valuta")
root.geometry("500x500")

moj_tab = ttk.Notebook(root)
moj_tab.pack(pady=5)

okvir_valuta = Frame(moj_tab, width=480, height=480)
okvir_konverzije = Frame(moj_tab, width=480, height=480)

okvir_valuta.pack(fill="both", expand=1)
okvir_konverzije.pack(fill="both", expand=1)

moj_tab.add(okvir_valuta, text="Valute")
moj_tab.add(okvir_konverzije, text="Konverzija")
moj_tab.tab(1, state="disabled")

valute = dohvati_sve_valute()
ime_valuti = [el["valuta"] for el in valute]

vasa_valuta_label = LabelFrame(okvir_valuta, text="Unesite valutu koju želite konvertirati:")
vasa_valuta_label.pack(pady=20)

vasa_valuta_entry = ttk.Combobox(vasa_valuta_label, values=ime_valuti, font=("Helvetica", 16))
vasa_valuta_entry.pack(padx=10, pady=10)

konverzija = LabelFrame(okvir_valuta, text="Konverzija valute")
konverzija.pack(pady=20)

Label(konverzija, text="Konvertiraj u:").pack(pady=10)

unos_vlaute_za_konverziju = ttk.Combobox(konverzija, values=ime_valuti, font=("Helvetica", 16))
unos_vlaute_za_konverziju.pack(padx=10, pady=10)

Label(konverzija, text="Trenutni tečaj:").pack(pady=10)

unos_tecaja = Entry(konverzija, font=("Helvetica", 16), state="disabled")
unos_tecaja.pack(padx=10, pady=10)

okvir_gumba = Frame(okvir_valuta)
okvir_gumba.pack(pady=20)

Button(okvir_gumba, text="Zaključaj", command=zakljucaj).grid(row=0, column=0, padx=10)
Button(okvir_gumba, text="Otključaj", command=otkljucaj).grid(row=0, column=1, padx=10)

iznos_konvertiranja_label = LabelFrame(okvir_konverzije, text="Iznos za konverziju:")
iznos_konvertiranja_label.pack(pady=20)

iznos_entry = Entry(iznos_konvertiranja_label, font=("Helvetica", 16))
iznos_entry.pack(padx=10, pady=10)

Button(iznos_konvertiranja_label, text="Konvertiraj", command=konvertiraj).pack(pady=10)

krajnji_iznos_label = LabelFrame(okvir_konverzije, text="Krajnji iznos:")
krajnji_iznos_label.pack(pady=20)

krajnji_iznos_entry = Entry(krajnji_iznos_label, font=("Helvetica", 16), bd=0, bg="systembuttonface")
krajnji_iznos_entry.pack(padx=10, pady=10)

Button(okvir_konverzije, text="Očisti", command=clear).pack(pady=20)

root.mainloop()
