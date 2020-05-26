betrag_I = float(input("Betrag I in €: "))
restwert_L = float(input("Restwert L in €: "))
nutzungsdauer_T = int(input("Nutzungsdauer T: "))
kapazitaet_k = int(input("Nutzungskapazität: "))

wertverlust_w = betrag_I - restwert_L

output = []
for year in range(nutzungsdauer_T):
  produktionsleistung_pl = int(input(f"Produktionsleistung in Periode {year+1}: "))
  anteilnutzung_an = produktionsleistung_pl / kapazitaet_k
  betrag_davor = betrag_I
  abschreibungsbetrag_a = wertverlust_w * anteilnutzung_an
  betrag_I -= abschreibungsbetrag_a

  output.append([year+1, round(betrag_davor, 2), round(abschreibungsbetrag_a, 2), round(betrag_I, 2)])

print("\n Periode | Betrag Beginn | Abschreibungsbetrag | Betrag Ende ")
print("{}|{}|{}|{}".format("-"*9, "-"*15, "-"*21, "-"*13))
for out in output:
  print("{:^9}|{:^15}|{:^21}|{:^13}".format(*out))

print("\n")
