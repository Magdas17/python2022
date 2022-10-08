miasto_a = input("miasto a:")
miasto_b = input("miasto b:")

dystans = int(input(f"odleglosc pomiedzy {miasto_a} - {miasto_b}: "))

cena = float(input("cena paliwa: "))
spalanie = float(input("spalanie na 100 km: "))

koszt = dystans * cena / spalanie
print(f"koszt podrozy {koszt}")
