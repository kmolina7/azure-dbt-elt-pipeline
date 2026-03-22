{{
    config(
        materialized='table'
    )
}}

-- 1. Traemos las ventas ya limpias de nuestro modelo anterior
WITH ventas_limpias AS (
    SELECT 
        id_venta,
        fecha_venta,
        producto,
        sucursal,
        total_venta AS total_usd
    FROM {{ ref('fact_ventas') }}
),

-- 2. Traemos LA ÚLTIMA tasa de cambio que Python haya descargado
tasa_actual AS (
    SELECT TOP 1
        tasa_EUR,
        tasa_GBP,
        tasa_JPY
    FROM {{ source('erp_logistica', 'tasas_raw') }}
    ORDER BY fecha_procesamiento DESC
)

-- 3. Cruzamos y calculamos las conversiones (dejando 2 decimales por estética)
SELECT 
    v.id_venta,
    v.fecha_venta,
    v.producto,
    v.sucursal,
    v.total_usd,
    CAST((v.total_usd * t.tasa_EUR) AS DECIMAL(10,2)) AS total_eur,
    CAST((v.total_usd * t.tasa_GBP) AS DECIMAL(10,2)) AS total_gbp,
    CAST((v.total_usd * t.tasa_JPY) AS DECIMAL(10,2)) AS total_jpy
FROM ventas_limpias v
CROSS JOIN tasa_actual t