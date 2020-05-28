num_fertigungsstufen = int(input("Fertigungsstufen: "))

einsatzmenge = []
kosten_einsatzmenge = []
ausbringungsmenge = []
stufenkosten = []
aufgelaufene_stufenkosten = []
aufgelaufene_kosten = []

for i in range(num_fertigungsstufen):
    einsatzmenge.append(float(input(f"Einsatzmenge in Stufe {i+1}:")))
    
for i in range(num_fertigungsstufen):
    ausbringungsmenge.append(float(input(f"Ausbringungsmenge in Stufe {i+1}:")))
    
rohstoffkosten = float(input("Rohstoffkosten: "))

for i in range(num_fertigungsstufen):
    stufenkosten.append(float(input(f"Stufenkosten der Stufe {i+1}:")))
    
vuv = float(input("Vertriebs und Verwaltungskosten (pro Stück!): "))

for i in range(num_fertigungsstufen):
    if (i==0):
        kosten_einsatzmenge.append(einsatzmenge[0] *  rohstoffkosten)
        aufgelaufene_stufenkosten.append(kosten_einsatzmenge[0] + stufenkosten[0])
        aufgelaufene_kosten.append(aufgelaufene_stufenkosten[0] / ausbringungsmenge[0])
        continue
        
    kosten_einsatzmenge.append(einsatzmenge[i] *  aufgelaufene_kosten[i-1])
    aufgelaufene_stufenkosten.append(kosten_einsatzmenge[i] + stufenkosten[i])
    aufgelaufene_kosten.append(aufgelaufene_stufenkosten[i] / ausbringungsmenge[i])
    
print("\n Kosten Einsatzmenge | Stufenkosten | Aufgelaufene Stufenkosten | Ausbringungsmenge | Aufgelaufene Kosten ")
print("{}|{}|{}|{}|{}".format("-"*21, "-"*14, "-"*27, "-"*19, "-"*22))

for i in range(num_fertigungsstufen):
    print("{:^21}|{:^14}|{:^27}|{:^19}|{:^22}".format(round(kosten_einsatzmenge[i], 2), round(stufenkosten[i], 2), round(aufgelaufene_kosten[i], 2), round(ausbringungsmenge[i], 2), round(aufgelaufene_kosten[i], 2)))
          
print("\n Herstellkosten: "+ str(round(aufgelaufene_kosten[num_fertigungsstufen-1] ,2)))

print("\n Selbstkosten: "+ str(round(aufgelaufene_kosten[num_fertigungsstufen-1] + vuv, 2)))

print("\n")
