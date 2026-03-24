/*Resolviendo problemas de registros duplicados*/
-- 1. Verificamos los duplicados primero (Solo para que los veas con tus propios ojos)
SELECT id_venta, COUNT(*) as cantidad
FROM dbo.ventas_raw
GROUP BY id_venta
HAVING COUNT(*) > 1;

-- 2. Borramos los duplicados dejando solo el registro más reciente
WITH CTE_Duplicados AS (
    SELECT 
        id_venta,
        ROW_NUMBER() OVER(
            PARTITION BY id_venta 
            ORDER BY fecha_ingesta DESC
        ) as FilaNum
    FROM dbo.ventas_raw
)
DELETE FROM CTE_Duplicados WHERE FilaNum > 1;