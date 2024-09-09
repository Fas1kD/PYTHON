### AHOJ SVĚTE

#print("Ahoj světe")


### KTERÉ ZE TŘÍ ČÍSEL JE NEJVĚTŠÍ
# """" """" = # - (komentáře)

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


### ZNÁMKOVÁNÍ NA ZÁKLADĚ PROCENT

"""
procenta = int(input("Napište procento od 0 po 100: "))

if procenta >= 100 or procenta < 0:     # >= větší nebo rovno, <= menší nebo rovno
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

"""
list_cisel = []

x = int(input("Kolik si přejete čísel ve vašem listu: "))
for y in range(x):
    cislo = int(input("Zadejte číslo: "))
    list_cisel.append(cislo)

print(list_cisel)

vysledek = sum(list_cisel) / x # sum(list_cisel) - sečte čísla v listu dohromady, /x - následně tato číslo vydělí počtem zapsaných čísel

print(vysledek) 
"""

### ZJISTIT JESTLI JE ROK PŘESTUPNÝ

"""
rok = int(input("Napište nějaký rok a zjistite zda se jedná o přestupný: "))

if rok%4 == 0:  # rok%4 == 0 - jestli je rok dělitelný 4 a nemá zbytek
    print(f"Rok {rok} je přestupný")
else:
    print(f"Rok {rok} není přestupný")
"""

### ZKONTROLUJ JESTLI JE ČÍSLO PRVO ČÍSLO

cislo = int(input("Zadejte číslo u kterého chcete zjistit zda se jedná o prvočíslo: "))
je_prvocislo = True

for i in range(2, cislo):  
    if cislo % i == 0:  
        je_prvocislo = False

if je_prvocislo:
    print(f"Číslo {cislo} je prvočíslo.")
else:
    print(f"Číslo {cislo} není prvočíslo")

# nemám tušení jak to funguje ale funguje to (tento příklad )

