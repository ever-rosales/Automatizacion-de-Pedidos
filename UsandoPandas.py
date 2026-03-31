import pandas as pd
import os
def ubicacionArchivo ():
    #Abriendo el archivo Reporte
    usuario=os.path.join("~")
    rutaArchivo=os.path.join(usuario,"Desktop","PedidosApp","Reporte.xlsx")
    df=pd.read_excel(rutaArchivo)
    return df

def ReporteCocaCola ():
    #Abriendo el archivo Reporte
    df=ubicacionArchivo()
    #Aplicando las primeras condiciones
    NombreProductosMinimo=df.loc[df["Stock"]<=df["Stock Minimo"],["Nombre Completo", "Stock"]]
    if not NombreProductosMinimo.empty:
        print("REPORTE DE PEDIDO COCACOLA")
        print("-"*50)
        print(NombreProductosMinimo)
        print("-"*50)
    else:
        print("No hay productos por pedir")
ReporteCocaCola()
