pierwsza_cyfra = int(input("pierwsza "))

druga_cyfra = int(input("druga "))

if pierwsza_cyfra + druga_cyfra == 15:
    print("dodawanie")
elif pierwsza_cyfra + druga_cyfra == 5:
    print("odejmowanie")
elif pierwsza_cyfra + druga_cyfra == 50:
    print("mnozenie")
elif pierwsza_cyfra + druga_cyfra == 1.5:
    print("dzielenie")
else:
    print("potegowanie")