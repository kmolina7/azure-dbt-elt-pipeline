# 🚀 Arquitectura ELT Serverless: Azure & dbt

## 🎯 Objetivo del Proyecto
Diseño e implementación de un pipeline de datos empresarial (End-to-End) simulando la ingesta de ventas de un sistema ERP legacy hacia un modelo analítico, priorizando la eficiencia en costos y la calidad de datos.

## 🏗️ Arquitectura y Tecnologías
1. **Extracción y Carga (EL):** Azure Data Factory (ADF) extrae datos crudos desde un Data Lake (Azure Blob Storage) y los carga en Azure SQL Database.
2. **Transformación (T):** `dbt` (Data Build Tool) se conecta a Azure SQL para modelar los datos utilizando **Cargas Incrementales** (ahorrando costos de cómputo).
3. **Calidad de Datos (DataOps):** Implementación de pruebas genéricas en dbt (`not_null`, `unique`, `accepted_values`) para auditar la integridad antes de la visualización.
4. **Visualización:** Power BI conectado vía Import a la tabla curada para toma de decisiones.

## 💡 Habilidades Técnicas Demostradas
* Orquestación de pipelines visuales en Azure Data Factory.
* Configuración de redes, firewalls y bases de datos Serverless en Azure.
* Modelado dimensional y materialización incremental con dbt (T-SQL/Jinja).
* Integración de Git para control de versiones.
