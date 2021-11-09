betrag_I = float(input("Betrag I in €: "))
restwert_L = float(input("Restwert L in €: "))
nutzungsdauer_T = int(input("Nutzungsdauer T: "))

abschreibungsbetrag_a = (betrag_I - restwert_L) / nutzungsdauer_T

print("\n Periode | Betrag Beginn | Abschreibungsbetrag | Betrag Ende ")
print("{}|{}|{}|{}".format("-"*9, "-"*15, "-"*21, "-"*13))
for year in range(nutzungsdauer_T):
  betrag_davor = betrag_I
  betrag_I -= abschreibungsbetrag_a
  print("{:^9}|{:^15}|{:^21}|{:^13}".format((year+1), round(betrag_davor, 2), round(abschreibungsbetrag_a, 2), round(betrag_I, 2)))

print("\n")
