personas = {"juan": 15, "maria": 22, "pedro": 18, "luis": 12, "ana": 30}

for nombre, edad in personas.items():
    if edad >= 18:
        print(f"{nombre} es mayor de edad")