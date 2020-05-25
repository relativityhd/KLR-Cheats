betrag_I = float(input("Betrag I in €: "))
restwert_L = float(input("Restwert L in €: "))
nutzungsdauer_T = int(input("Nutzungsdauer T in €: "))

abschreibungsbetrag_a = (betrag_I - restwert_L) / nutzungsdauer_T

print("Periode|Betrag Beginn|Abschreibungsbetrag|Betrag Ende")
for year in range(nutzungsdauer_T):
  betrag_davor = betrag_I
  betrag_I -= abschreibungsbetrag_a
  print("{:^7}|{:^13}|{:^19}|{:^11}".format((year+1), round(betrag_davor, 2), round(abschreibungsbetrag_a, 2), round(betrag_I, 2)))
