# AHOJ SVĚTE

#print("Ahoj světe")


# KTERÉ ZE TŘÍ ČÍSEL JE NEJVĚTŠÍ
# """" """" = # (komentáře)

""""
print("Napiš 3 čísla o já za tebe zjistím které je největší")

x = int(input("Číslo1:"))
y = int(input("Číslo2:"))
z = int(input("Číslo3:"))

if x > y and x > z:
    nejvetsi_cislo = x
elif y > x and y >z:
    nejvetsi_cislo = y
else:    
    nejvetsi_cislo = z

print(f"Největší číslo je: {nejvetsi_cislo}")

"""


# ZNÁMKOVÁNÍ NA ZÁKLADĚ PROCENT
# >= větší nebo rovno, <= menší nebo rovno

"""
procenta = int(input("Napište procento od 0 po 100: "))

if procenta >= 100 or procenta < 0:
    print("Číslo musí být mezi 0 a 100")
elif procenta >= 90:
    print("Známka A")
elif procenta >= 75:
    print("Známka B")
elif procenta >= 50:
    print("Známka C")
elif procenta >= 25:
    print("Známka D")
else:
    print("F")
"""

### PRŮMĚR Z LISTU ČÍSEL

list_cisel = []

x = int(input("Kolik si přejete čísel ve vašem listu: "))
for y in range(x):
    cislo = int(input("Zadejte číslo: "))
    list_cisel.append(cislo)

print(list_cisel)

vysledek = sum(list_cisel) / x # sum(list_cisel) - sečte čísla v listu dohromady, /x - následně tato číslo vydělí počtem zapsaných čísel

print(vysledek) 


