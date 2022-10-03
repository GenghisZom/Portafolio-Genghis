import time

B=("\t\t\tMaquina expendedora")
for i in B:
    print(i, end="")
    time.sleep(0.05)

## 0 0 0
##  1  1  1       Filas   
## 2  2  2

##0 1 2 3
##0 1 2 3   Columnas
##0 1 2 3
    
Me=[["Papas","Mani","Salchichas","Gomitas"],
       ["Chocolatina","Agua","Coca-Cola","Pepsi"],
       ["Turron","Chicle","Avena","Cereales"]]

print("\nPrecios de cada producto:")
S=[['Papas:$1700'],['Mani:$1.000'],['Salchichas:$2.000'],['Gomitas:$1.000'],
   ['Chocolatina:$1.400'],['Agua:$1.200'],['Coca-cola:$2.100'],['Pepsi:$2.000'],
   ['Turron:1.000'],['Chicle:$$200'],['Avena:$1.500'],['Cereales:$2.200']]
print("\n",S[0],"\n",S[1],"\n",S[2],"\n",S[3],"\n",S[4],"\n",S[5],"\n",S[6],"\n",S[7],"\n",S[8],"\n",S[9],"\n",S[10],"\n",S[11])
time.sleep(1)      

MePrecios=[[(1700),(1000),(2000),(1000)],
                   [(1400),(1200),(2100),(2000)],
                   [(1000),(200),(1500),(2200)]]

print("\n",Me[0],"\n",Me[1],"\n",Me[2])

print("\nintroduzca su cantidad de dinero")
D=int(input("Dinero: "))
    
def Maquina(D):
    if D>=(MePrecios[0][0]) or D>=(MePrecios[0][1]) or D>=(MePrecios[0][2]) or D>=(MePrecios[0][3]) or D>=(MePrecios[1][0]) or D>=(MePrecios[1][1]) or D>=(MePrecios[1][2]) or D>=(MePrecios[1][3]) or D>=(MePrecios[2][0]) or D>=(MePrecios[2][1]) or D>=(MePrecios[2][2]) or D>=(MePrecios[2][3]):
        print("¿Que producto desea escoger? ")
        F=int(input("¿Cual fila?(Del 0 al 2): "))
        C=int(input("¿Cual columna?(Del 0 al 3): "))
        if D>=(MePrecios[F][C]):
            print("El producto que escogio es",Me[F][C],"y tiene un costo de",MePrecios[F][C],"pesos")
            Dr=D-(MePrecios[F][C])
            print("Su dinero restante es de",Dr,"pesos")
            R=input("¿Desea comprar otro producto?: ").upper()
            if R==("SI") or R==("SÍ"):
                Da=input("¿Desea introducir mas dinero?: ").upper()
                if Da==("SI") or Da==("SÍ"):
                    print("\nintroduzca su cantidad de dinero")
                    Dt=int(input("Dinero: "))
                if Da==("NO"):
                    D=Dr
                    Maquina(D)
            else:
                print("entregando su dinero restante")
                time.sleep(1)
                print("espere")
                time.sleep(1)
                print("Su dinero sobrante es de",Dr,"pesos")
                print("Muchas gracias por su compra, vuelva pronto")
                exit()
            D=Dr+Dt
            print("Su nuevo saldo es de",D,"pesos")
            Maquina(D)
        else:
            print("No tiene saldo suficiente para este producto")
            R=input("¿Desea introducir mas dinero?: ").upper()
            if R==("SI") or R==("SÍ"):
                print("\nintroduzca su cantidad de dinero")
                Dt=int(input("Dinero: "))
                D=Dt+D
                Maquina(D)
            else:
                print("Su dinero sobrante es de",D,"pesos")
                print("Muchas gracias por su compra, vuelva pronto")
                exit()
    else:
        print("No tiene la suficiente cantidad de dinero para comprar algun producto de la maquina expendedora")
        print("Introduzca otra cantidad de dinero")
        Dt=int(input("Dinero: "))
        D=Dt+D
        Maquina(D)

Maquina(D)
























































#Alejandro#Sarai#Daniel#Angel
#═══•◉•═════
#▂▄▄▓▄▄▂
#◢◤ █▀▀████▄▄▄▄◢◤
#█▄ █ █▄ ███▀▀▀▀▀▀▀╬
#◥█████◤
#═╩══╩═
#╬═╬
#╬═╬
#╬═╬
#╬═╬ chau, desinstalen python.
#╬═╬ ●/
#╬═╬/▌
#╬═╬/ \
