# Initialisierung der Liste
tup = []

# Hinzufügen von Tupeln zur Liste
tup.append((1, 2))
tup.append((3, 4))
tup.append((5, 6))
tup.append((7, 8))
tup.append((9, 10))

# Zugriff auf das 3. Tupel (Index 2, da Indizes bei 0 beginnen)
drittes_tupel = tup[2]

# Zugriff auf die Elemente des 3. Tupels
erstes_element = tup[2][0]
zweites_element = tup[2][1]

# Ausgabe der Elemente
print(f"Das 3. Tupel ist: {drittes_tupel}")
print(f"Erstes Element des 3. Tupels: {erstes_element}")
print(f"Zweites Element des 3. Tupels: {zweites_element}")