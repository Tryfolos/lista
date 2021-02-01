#Importing stuff.
import random
import sys


#Bestämmer vilken tidpunkt det var som du gick till affären.
time_hours = random.randint(0, 23)
if time_hours < 10:
    time_hours = f"0{time_hours}"

time_minutes = random.randint(0, 60)
if time_minutes < 10:
    time_minutes = f"0{time_minutes}"

time = f"{time_hours}:{time_minutes}"

#En lista med affärer.
affärer = ["Ica", "Coop", "OKQ8", "Willys", "Ikea", "NetOnNet", "Elgiganten", "Apoteket", "Kiosken", "Källargubben", "Jysk", "McDonalds", "Frasses", "Kappahl", "Adolf Hitler", "Stalin", "Donalt Trump", "Stefan Löfven", "Greta Thunberg", "Kommunhuset"]

#En lista med saker som man kan köpa.
saker = ["Bulle", "Monster", "Knark", "Ost", "Digistive", "Toastol", "Handbojor", "Piska", "Mjölk", "Gurka", "Skinka", "Dammtrasa", "Chips", "Hockeyklubba", "Kondomer", "Basebollträ", "Sås", "Gurkmeja", "Kaffe", "Dator", "Rakapparat", "Motorsåg", "Elefanttestiklar", "Hästkuk", "Vodka", "Rutten banan", "Ingenting", "En slav", "Alvedon"]

#Vad gjorde personen.
handlingar = ["köpte", "Sålde", "skänkte"]

#Nu väljer programmet ord ur listorna och gör en mening. Sedan printas meningen.
affär = random.choice(affärer)
saken = random.choice(saker)
saken2 = random.choice(saker)
handling = random.choice(handlingar)

print(f"Jag gick till {affär} igår klockan {time} och {handling} {saken} och {saken2}")


