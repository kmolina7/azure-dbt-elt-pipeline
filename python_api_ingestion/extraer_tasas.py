import requests
import pandas as pd
from datetime import datetime
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv() # Abrimos la caja fuerte

def extraer_datos_financieros():
    print("🚀 Iniciando extracción de datos...")
    url_api = "https://api.frankfurter.app/latest?from=USD&to=EUR,GBP,JPY"
    
    try:
        respuesta = requests.get(url_api)
        respuesta.raise_for_status() 
        datos_json = respuesta.json()
        print(f"✅ Datos obtenidos exitosamente para la fecha: {datos_json['date']}")
        
        tasas = datos_json['rates']
        fila_datos = {
            'fecha_referencia': datos_json['date'],
            'moneda_base': 'USD',
            'tasa_EUR': tasas['EUR'],
            'tasa_GBP': tasas['GBP'],
            'tasa_JPY': tasas['JPY'],
            'fecha_procesamiento': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        df = pd.DataFrame([fila_datos])
        nombre_archivo = "tasas_cambio_hoy.csv"
        df.to_csv(nombre_archivo, index=False)
        print(f"💾 Archivo '{nombre_archivo}' guardado localmente.")
        
        # Devolvemos el nombre del archivo para que la siguiente función lo use
        return nombre_archivo
        
    except Exception as e:
        print(f"❌ Ocurrió un error durante la extracción: {e}")
        return None

def cargar_a_azure(nombre_archivo_local):
    print(f"\n☁️ Iniciando carga a Azure Blob Storage (Modo Seguro)...")
    
    # ⚠️ Leemos la llave desde el archivo .env
    cadena_conexion = os.getenv('AZURE_STORAGE_CONN_STRING')
    nombre_contenedor = "datos-crudos"
    
    try:
        # 1. Nos conectamos a tu cuenta de almacenamiento en Azure
        blob_service_client = BlobServiceClient.from_connection_string(cadena_conexion)
        
        # 2. Apuntamos al contenedor y le decimos cómo se llamará el archivo en la nube
        blob_client = blob_service_client.get_blob_client(container=nombre_contenedor, blob=nombre_archivo_local)
        
        # 3. Subimos el archivo (con overwrite=True por si corremos el script varias veces)
        print(f"⏳ Subiendo {nombre_archivo_local}...")
        with open(nombre_archivo_local, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
        print(f"🎉 ¡Éxito Total! El archivo está ahora en tu contenedor '{nombre_contenedor}' en la nube.")
        
    except Exception as e:
        print(f"❌ Error al subir a Azure: {e}")

# Flujo principal de ejecución
if __name__ == "__main__":
    # 1. Extraer (E) y Transformar (T)
    archivo_generado = extraer_datos_financieros()
    
    # 2. Si todo salió bien, Cargar a Azure (L)
    if archivo_generado:
        cargar_a_azure(archivo_generado)