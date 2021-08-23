def main():
    #escribe tu código abajo de esta línea
    print("Introduce un número entero de 4 dígitos")
    n = int(input())
    if (n%2==0):
        print ("- El cuarto dígito es par")
    else:
        print ("- El cuarto dígito es impar")
    n1 = n//10
    print (n1)
    if (n1%2==0):
        print ("- El tercer dígito es par")
    else:
        print ("- El tercer dígito es impar")
    n2 = n1//10
    print(n2)
    if (n2%2==0):
        print ("- El segundo dígito es par")
    else:
        print ("- El segundo dígito es impar")
    n3 = n2//10
    print(n3)
    if (n3%2==0):
        print ("- El primero dígito es par")
    else:
        print ("- El primer dígito es impar")
    pass

if __name__ == '__main__':
    main()
