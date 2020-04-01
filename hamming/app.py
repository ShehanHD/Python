def test(p):
    ris = []

    x = y = 0
    for i in range(p, 8, 2):
        for j in range(p):
            if x+y < 8 and p is not 1:
                ris.insert(x+y, complete[i+y-1])
            if p is 1:
                ris.insert(x, complete[i-1])
            y += 1
        x = y
    ris.remove("_")

    return ris

def parita(x):
    ret = []
    for i in range(len(x)):
        temp = 0
        for j in range(len(x[i])):
            temp = temp != int(x[i][j])
        ret.append(temp)

    return ret

dati = []
controllo = []
complete = []

for i in range(4):
    dati.insert(i, input(f"inserisci il {i+1}° dato > "))

c = d = 0

for i in range(7):
    if i is not 0 and i is not 1 and i is not 3:
        temp = dati[d]
        complete.insert(i, temp)
        d = d + 1
    else:
        complete.insert(i, "_")
        c = c + 1

print(f"{complete} \n")
1
for i in range(3):
    controllo.insert(i, test(pow(2, i)))

#print(f"{controllo} \n")

j = 0
for i in parita(controllo):
    complete.__delitem__(pow(2, j)-1)
    x = (1 if i else 0)
    complete.insert(pow(2, j)-1, x)
    j += 1

print(complete)
