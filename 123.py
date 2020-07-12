
print("podaj 3 liczby")
a=int(input())
b=int(input())
c=int(input())

if (a>b):
    naj=a
else:
    naj=b
if(c>naj):
    naj=c
print("nawieksza liczba to", naj)


if(a>b):
    jeden=a
else:
    jeden=b
if(c>jeden):
    jeden=c

if(jeden != a and jeden != b):
    if(a>b):
        dwa=a
    else:
        dwa=b
if(jeden != a and jeden != c):
    if(a>c):
        dwa=a
    else:
        dwa=c
if(jeden != b and jeden != c):
    if(c>b):
        dwa=c
    else:
        dwa=b

if(jeden !=c and dwa !=c):
    trzy=c
if(jeden !=b and dwa !=b):
    trzy=b
if(jeden !=a and dwa !=a):
    trzy=a


print(jeden, dwa, trzy)
print("siema")
