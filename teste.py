#Hello_Github

b = 1
s = 0
a = [int(input("digite o primeiro número da lista"))]
while (b !=0):
 b = int(input("digite mais um número da lista digite 0 para sair"))
 a.append(b)
 s= s+1

del(a[s])

a.sort()
t=len(a) - 2

s = 0
while (s < t):
    if (a[s] == a[s+1]):
        del(a[s])
        t=t-1
        s=s-1
    s=s+1
 
print(a)
