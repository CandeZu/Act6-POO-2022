from Manejador import ManejadorViajero
from Viajero import Viajero
import os

if __name__=='__main__':
    lista = ManejadorViajero()
    lista.GenerarLista()
    lista.ListarViajeros()
    NroViaj= int(input("Ingrese nro de viajero del cual desea consultar\n"))
    Viajero= lista.buscar(NroViaj)
    
    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Determinar el/los viajero/s con mayor cantidad de millas acumuladas.")
        print("[2] Para acumular millas")
        print("[3] Para canjear millas")
        print("[0] Para SALIR del menu")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))

        elif(op == 2):

        elif(op == 3):

        elif(op == 0):
            continuar = not continuar