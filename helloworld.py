# AHOJ SVĚTE

#print("Ahoj světe")


# KTERÉ ZE TŘÍ ČÍSEL JE NEJVĚTŠÍ

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

