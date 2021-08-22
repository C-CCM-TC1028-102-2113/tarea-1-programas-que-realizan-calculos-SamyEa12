def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    mensajes=int(input("Dame el número de mensajes: "))
    megas=float(input("Dame el número de megas: "))
    minutos=int(input("Dame el número de minutos: "))

    pmen=mensajes*0.80
    pmeg=megas*0.80
    pmin=minutos*0.80
    
    precio=pmen+pmeg+pmin
    
    print("El costo mensual es: " + str(precio)) 
    pass


if __name__ == '__main__':
    main()
