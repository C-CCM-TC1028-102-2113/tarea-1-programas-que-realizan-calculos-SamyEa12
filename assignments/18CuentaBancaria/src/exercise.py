def main():
    #escribe tu código abajo de esta línea
    saldom=float(input("Dame el saldo del mes anterior: "))
    ingresos=float(input("Dame los ingresos: "))
    egresos=float(input("Dame los egresos: "))
    cheques=int(input("Dame el número de cheques: "))
    pcheques=cheques*13
    saldon=saldom+ingresos-egresos-pcheques
    tasa=saldon*0.075
    saldof=saldon-tasa
    print("El saldo final de la cuenta es: " + str(saldof))

    pass

if __name__ == '__main__':
    main()
