CREATE TABLE ventas_raw (
    id_venta INT,
    fecha_venta DATE,
    producto VARCHAR(100),
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    sucursal VARCHAR(50),
    
    -- Marca de auditoría: Práctica obligatoria de un Data Engineer
    fecha_ingesta DATETIME DEFAULT GETDATE() 
);
GO

SELECT * FROM ventas_raw;

SELECT * FROM fact_ventas;