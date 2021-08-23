def main():
    #escribe tu código abajo de esta línea
    n=int(input("Dame un número: "))
    n1=n//1000
    n2=n//100
    n3=n//10
    if (n1%2==0):
        d1=1
    else:
        d1=0
    if (n2%2==0):
        d2=1
    else:
        d2=0
    if (n3%2==0):
        d3=1
    else:
        d3=0
    if (n%2==0):
        d4=1
    else:
        d4=0
    df=d1+d2+d3+d4
    print("El número de dígitos pares es: " + str(df))
    pass

if __name__ == '__main__':
    main()
