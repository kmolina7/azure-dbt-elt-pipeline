# 🚀 Arquitectura ELT Serverless: Azure & dbt

## 🎯 Objetivo del Proyecto
Diseño e implementación de un pipeline de datos empresarial (End-to-End) simulando la ingesta de ventas de un sistema ERP legacy hacia un modelo analítico, priorizando la eficiencia en costos y la calidad de datos.

## 🏗️ Arquitectura y Tecnologías
1. **Extracción de APIs (NUEVO):** Scripts en **Python** (`requests`, `pandas`) que extraen tasas de cambio en vivo desde una API financiera (Frankfurter), procesan el JSON y lo suben a Azure Blob Storage y Azure SQL Database (usando `sqlalchemy` y `pyodbc`).
2. **Extracción y Carga (EL):** Azure Data Factory (ADF) orquesta la ingesta de datos transaccionales desde el Data Lake hacia Azure SQL.
3. **Transformación (T):** `dbt` modela los datos usando Cargas Incrementales. Se implementó un modelo analítico (`mart_ventas_globales`) que realiza un `CROSS JOIN` entre las ventas y las tasas de cambio extraídas por Python para reportería multimoneda.
4. **Calidad de Datos (DataOps):** Pruebas genéricas en dbt (`not_null`, `unique`, `accepted_values`) para auditar la integridad.
5. **Visualización:** Power BI conectado vía Import para toma de decisiones.

## 💡 Habilidades Técnicas Demostradas
* Orquestación de pipelines visuales en Azure Data Factory.
* Configuración de redes, firewalls y bases de datos Serverless en Azure.
* Modelado dimensional y materialización incremental con dbt (T-SQL/Jinja).
* Integración de Git para control de versiones.
