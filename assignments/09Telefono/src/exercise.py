def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    mensajes=float(input("Dame el número de mensajes: "))
    megas=float(input("Dame el número de megas: "))
    minutos=float(input("Dame el número de minutos: "))
    
    pmen=mensajes*0.8
    pmeg=megas*0.8
    pmin=minutos*0.8
    
    precio=pmen+pmeg+pmin
    
    print("El costo mensual es: " + str(precio)) 
    pass

if __name__ == '__main__':
    main()
