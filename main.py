import pandas as pd
import os
import glob


def encontrar_archivo_mas_nuevo(carpeta, nombre):
    # Construir el patrón de búsqueda
    patron = os.path.join(carpeta, f'*{nombre}*.csv')

    # Obtener la lista de archivos que coinciden con el patrón
    archivos = glob.glob(patron)

    # Verificar si se encontraron archivos
    if not archivos:
        return None  # No se encontraron archivos

    # Encontrar el archivo más nuevo
    archivo_mas_nuevo = max(archivos, key=os.path.getctime)

    # Devolver la ruta completa del archivo más nuevo
    return os.path.abspath(archivo_mas_nuevo)


carpeta_data = os.path.join(os.getcwd(), "data")
archivo_producto_mas_nuevo = encontrar_archivo_mas_nuevo(carpeta_data, 'producto')
archivo_precio_mas_nuevo = encontrar_archivo_mas_nuevo(carpeta_data, 'precio')

df_producto = pd.read_csv(archivo_producto_mas_nuevo)
df_precio = pd.read_csv(archivo_precio_mas_nuevo)

df_consolidado = pd.merge(df_producto, df_precio, left_on='id', right_on='producto_id', how='inner')

archivo_final = os.path.join(carpeta_data, 'csv_final.xlsx')
df_consolidado.to_excel(archivo_final, index=False)
