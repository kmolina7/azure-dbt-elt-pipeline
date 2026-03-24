use [sqldb-logistica]

--CREATE TABLE ventas_raw (
--    id_venta INT,
--    fecha_venta DATE,
--    producto VARCHAR(100),
--    cantidad INT,
--    precio_unitario DECIMAL(10,2),
--    sucursal VARCHAR(50),
    
--    -- Marca de auditoría: Práctica obligatoria de un Data Engineer
--    fecha_ingesta DATETIME DEFAULT GETDATE() 
--);
--GO

/*consultando tablas de datos crudos*/
SELECT TOP 100 v.* 
FROM ventas_raw AS v;

/*consultando tablas limpias y transformadas*/
SELECT TOP 100 f.* 
FROM fact_ventas AS f;

/*Consultando las tasas de referencia*/
SELECT TOP 1 t.*
FROM tasas_raw AS t
ORDER BY t.fecha_referencia DESC

/*consultando el Data Mart*/
SELECT TOP 20 m.*
FROM dbo.mart_ventas_globales AS m
ORDER BY m.id_venta ASC