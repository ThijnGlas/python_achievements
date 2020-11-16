km_per_maand = ""
verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

def bereken_maandkosten(km_per_maand):
    return (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand


while not isinstance(km_per_maand, float):
    try:
        km_per_maand = input("Hoeveel KM rijdt jij per maand?: ")
        km_per_maand = float(km_per_maand)
        print("€ ",round(bereken_maandkosten(km_per_maand), 2   ))
    except ValueError:
        print(km_per_maand + " is geen geldig getal!")
