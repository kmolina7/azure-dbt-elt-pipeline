{{
    config(
        materialized='incremental',
        unique_key='id_venta'
    )
}}

-- 1. Leemos los datos crudos
WITH ventas_crudas AS (
    SELECT 
        id_venta,
        fecha_venta,
        producto,
        cantidad,
        precio_unitario,
        sucursal,
        fecha_ingesta,
        -- Añadimos valor de negocio: Calculamos el total
        (cantidad * precio_unitario) AS total_venta
    FROM {{ source('erp_logistica', 'ventas_raw') }}
)

SELECT * FROM ventas_crudas

-- 2. LA MAGIA INCREMENTAL
-- Si la tabla fact_ventas ya existe, este bloque de código se activa
{% if is_incremental() %}

  -- Solo trae los registros que entraron DESPUÉS del último registro que procesé
  WHERE fecha_ingesta > (SELECT MAX(fecha_ingesta) FROM {{ this }})

{% endif %}