def main():
    #escribe tu código abajo de esta línea
    jnuevos=int(input("Dame la cantidad de juegos nuevos: "))
    jusados=int(input("Dame la cantidad de juegos usados: "))
    
    pjn=jnuevos*1000
    pju=jusados*350
    
    ptotal=pjn+pju
    
    print("El total de la compra es: " + str(ptotal))
    pass
   pass



if __name__ == '__main__':
    main()
