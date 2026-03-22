import pandas as pd
from sqlalchemy import create_engine
import urllib
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env oculto
load_dotenv()

def cargar_csv_a_sql():
    print("🚀 Iniciando carga hacia Azure SQL Database (Modo Seguro)...")
    
    # 1. Leer el archivo local
    nombre_archivo = "tasas_cambio_hoy.csv"
    try:
        df = pd.read_csv(nombre_archivo)
        print(f"✅ Archivo '{nombre_archivo}' leído correctamente. Filas: {len(df)}")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {nombre_archivo}. Ejecuta el script de extracción primero.")
        return

    # 2. Credenciales dinámicas (Leídas de forma segura desde el archivo .env)
    server = os.getenv('AZURE_SERVER')
    database = os.getenv('AZURE_DB')
    username = os.getenv('AZURE_USER')
    password = os.getenv('AZURE_PASSWORD')
    driver = '{ODBC Driver 17 for SQL Server}'

    try:
        # 3. Armar la cadena de conexión estricta para Azure
        print("⏳ Conectando a la base de datos...")
        cadena_conexion = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
        params = urllib.parse.quote_plus(cadena_conexion)
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

        # 4. Magia de Pandas: Enviar el DataFrame completo a SQL
        # Si la tabla no existe, la crea. Si existe, agrega los datos al final (append)
        nombre_tabla = 'tasas_raw'
        
        df.to_sql(
            name=nombre_tabla, 
            con=engine, 
            schema='dbo', 
            if_exists='append', # 'append' inserta sin borrar lo anterior
            index=False
        )
        
        print(f"🎉 ¡Éxito Total! Los datos se insertaron en la tabla 'dbo.{nombre_tabla}'.")
        
    except Exception as e:
        print(f"❌ Error al conectar o insertar en SQL: {e}")

if __name__ == "__main__":
    cargar_csv_a_sql()