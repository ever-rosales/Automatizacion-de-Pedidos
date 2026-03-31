import pandas as pd
import os
def ubicacionArchivo ():
    #Abriendo el archivo Reporte
    usuario=os.path.expanduser("~")
    rutaArchivo=os.path.join(usuario,"Desktop","PedidosApp","Reporte.xlsx")
    if os.path.exists(rutaArchivo):
        df=pd.read_excel(rutaArchivo)
        return df
    else:
        print("No hay ningun archivo ")
        return None

def reportePepsiCo ():
    df=ubicacionArchivo()
    if df is not None:
        #Listando todos los productos con marca "PepsiCo"
        pepsi_df=df[df["Marca"].str.upper()=="PEPSICO"]
        if pepsi_df.empty:
            print("No se a encontrado registro para PepsiCo")
        else:
            #Aplicando la condiciones principal (bajo stock)
            filtroPepsi=(df["Marca"].str.upper()=="PEPSICO") & (df["Stock"]<=df["Stock Minimo"])
            bajoStockPepsi=df[filtroPepsi]
            if bajoStockPepsi.empty:
                print("Tienes productos suficientes")
            else:
                #Debe conocer los elementos bajo stock para poder imprimir los que hagan falta
                print("-->PEDIDO PARA PEPSI\n")
                print(bajoStockPepsi[["Nombre", "Piezas"]].to_markdown(index=False))
reportePepsiCo()

def reporteCocaCola ():
    df=ubicacionArchivo()
    if df is not None:
        cocaCola_df=df[df["Marca"].str.upper()=="COCACOLA"]
        if cocaCola_df.empty:
            print("No se a encontrado registro para CocaCola")
        else:
            filtroCocaCola=(df["Marca"].str.upper()=="COCACOLA") & (df["Stock"]<=df["Stock Minimo"])
            bajoStockCocaCola=df[filtroCocaCola]
            if bajoStockCocaCola.empty:
                print("Tienes productos suficentes")
            else:
                print("-->PEDIDO PARA COCACOLA\n")
                print(bajoStockCocaCola[["Nombre", "Piezas"]].to_markdown(index=False))
reporteCocaCola()
