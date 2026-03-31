import pandas as pd
import os
import pywhatkit as pwk
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
"""
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
                return bajoStockPepsi
def mandarPedidoPepsi(df_pedidoPepsi):
    if df_pedidoPepsi is not None:
        lineas_pedido=[]
        for _, fila in df_pedidoPepsi.iterrows():
            lineas_pedido.append(f"- {fila['Nombre']}: {fila['Piezas']} pz")
        cuerpo_mensaje = "\n".join(lineas_pedido)
        mensaje_final = f"Hola, requiero el siguiente pedido 📦:\n\n{cuerpo_mensaje}"
        numero_proveedor = "+525563372685"
        print("\nEnviando pedido por WhatsApp...")
        try:
            # Enviamos instantáneamente
            pwk.sendwhatmsg_instantly(numero_proveedor, mensaje_final, wait_time=15, tab_close=True)
            print("¡Mensaje enviado con éxito!")
        except Exception as e:
            print(f"Error al enviar: {e}")
datos_para_pedido = reportePepsiCo()
if datos_para_pedido is not None:
    mandarPedidoPepsi(datos_para_pedido)
"""

"""
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
                return bajoStockCocaCola
def mandarPedidoCocaCola(df_pedidoCoca):
    if df_pedidoCoca is not None:
        lineas_pedido=[]
        for _, fila in df_pedidoCoca.iterrows():
            lineas_pedido.append(f"- {fila['Nombre']}: {fila['Piezas']} pz")
        cuerpo_mensaje = "\n".join(lineas_pedido)
        mensaje_final = f"Hola, requiero el siguiente pedido 📦:\n\n{cuerpo_mensaje}"
        numero_proveedor = "+525563372685"
        print("\nEnviando pedido por WhatsApp...")
        try:
            pwk.sendwhatmsg_instantly(numero_proveedor,mensaje_final,wait_time=15,tab_close=True)
            print("¡Mensaje enviado con éxito!")
        except Exception as e:
            print(f"Error al enviar: {e}")
datos_para_pedido=reporteCocaCola()
if datos_para_pedido is not None:
    mandarPedidoCocaCola(datos_para_pedido)
"""

def reportePeñafiel ():
    df=ubicacionArchivo()
    if df is not None:
        reportePeñafiel_df=df[df["Marca"].str.upper()=="PEÑAFIEL"]
        if reportePeñafiel_df.empty:
            print("No se a encontrado registro para PEÑAFIEL")
        else:
            filtroPeñafiel=(df["Marca"].str.upper()=="PEÑAFIEL") & (df["Stock"]<=df["Stock Minimo"])
            bajoStockPeñafiel=df[filtroPeñafiel]
            if bajoStockPeñafiel.empty:
                print("Tienes productos suficentes")
            else:
                print("-->PEDIDO PARA PEÑAFIEL\n")
                print(bajoStockPeñafiel[["Nombre", "Piezas"]].to_markdown(index=False))
                return bajoStockPeñafiel

def mandarPedidoPeñafiel(df_pedidoPeñafiel):
    if df_pedidoPeñafiel is not None:
        lineas_pedido=[]
        for _, fila in df_pedidoPeñafiel.iterrows():
            lineas_pedido.append(f"- {fila['Nombre']}: {fila['Piezas']} pz")
        cuerpo_mensaje = "\n".join(lineas_pedido)
        mensaje_final = f"Hola, requiero el siguiente pedido 📦:\n\n{cuerpo_mensaje}"
        numero_proveedor = "+525563372685"
        print("\nEnviando pedido por WhatsApp...")
        try:
            pwk.sendwhatmsg_instantly(numero_proveedor,mensaje_final,wait_time=15,tab_close=True)
            print("¡Mensaje enviado con éxito!")
        except Exception as e:
            print(f"Error al enviar: {e}")
datos_para_pedido=reportePeñafiel()
if datos_para_pedido is not None:
    mandarPedidoPeñafiel(datos_para_pedido)
