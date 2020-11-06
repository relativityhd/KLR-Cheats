print("\n{:^14}|{:^14}\n{}".format('Vorhergesagt', 'Tatsaechlich', '-'*28))
TN = float(input("{:^14}|{:^14}: ".format('Falsch', 'Falsch'))) # True Negative
FN = float(input("{:^14}|{:^14}: ".format('Falsch', 'Richtig'))) # False Negative
FP = float(input("{:^14}|{:^14}: ".format('Richtig', 'Falsch'))) # False Positive
TP = float(input("{:^14}|{:^14}: ".format('Richtig', 'Richtig'))) # True Positive
N = float(TN + FP) # All Negatives
P = float(FN + TP) # All Positives
n = TN + FN +  FP + TP

print("\n n = {:^15}| Vorhergesgt: Falsch | Vorhergesagt: richtig | Summe".format(n))
row = "{}|{}|{}|{}".format("-"*20, "-"*21, "-"*23, "-"*10)
print(row)
print("{:^20}|{:^21}|{:^23}|{:^10}".format( "Tatsaechlich Falsch", TN, FP, N))
print("{:^20}|{:^21}|{:^23}|{:^10}".format( "Tatsaechlich richtig", FN, TP, P))
print("{:^20}|{:^21}|{:^23}|{:^10}".format( "Summe", TN + FN, FP + TP, ""))

ACC = round((TP+TN)/(P+N), 2)
Miscl = round((FP+FN)/(P+N), 2)
PPV = round(TP/(TP+FP), 2)
TPR = round(TP/P, 2)
FPR = round(FP/N, 2)
TNR = round(1-FPR, 2)
F1 = round(2 * ((PPV*TPR)/(PPV+TPR)), 2)

print("\nAccuracy (ACC) = {} ".format(ACC))
print("\nMissclassification = {} ".format(Miscl))
print("\nPrecision (PPV) = {}".format(PPV))
print("\nSensitivity (TPR) = {}".format(TPR))
print("\nFall-out (FPR) = {}".format(FPR))
print("\nSpecificity (TNR) = {}".format(TNR))
print("\nF1 = {}\n".format(F1))