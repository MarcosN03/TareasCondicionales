a = int(input("Introduce tu edad:"))
b = int(input("Introduce tus ingresos:"))

def calculo (a,b):
    if (a>16 and b>= 1000):
        print("Debe tributar")
    else:
        print("No tributa")
calculo (a,b)