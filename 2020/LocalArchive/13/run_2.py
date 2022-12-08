ipt = open("input_final.txt")
data = ipt.read().split("\n")
ipt.close()
busses = data[1].split(",")
bi = []
ni = []
for i in range(len(busses)):
    if busses[i]!="x":
        bi.append((int(busses[i])-i%int(busses[i]))%int(busses[i]))
        ni.append(int(busses[i]))
N = 1
for n in ni:
    N*=n
Ni = [N//n for n in ni]
xi = []
product = []
for i in range(len(Ni)):
    num = Ni[i]%ni[i]
    found = False
    x = 1
    while not found:
        if (x*num)%ni[i]==1:
            found = True
            break
        x+=1
    xi.append(x)
for i in range(len(bi)):
    product.append(bi[i]*Ni[i]*xi[i])
ans = sum(product)%N
print(ans)
