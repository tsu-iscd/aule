--https://docs.microsoft.com/en-us/sql/t-sql/statements/create-index-transact-sql
#begin
-- Create a simple nonclustered rowstore index
CREATE INDEX IX_VendorID ON ProductVendor (VendorID);
CREATE INDEX IX_VendorID ON dbo.ProductVendor (VendorID DESC, Name ASC, Address DESC);
CREATE INDEX IX_VendorID ON Purchasing..ProductVendor (VendorID);

#end
#begin
-- Create a simple nonclustered rowstore composite index
CREATE NONCLUSTERED INDEX IX_SalesPerson_SalesQuota_SalesYTD ON Sales.SalesPerson (SalesQuota, SalesYTD);

#end
#begin
-- Create an index on a table in another database
CREATE CLUSTERED INDEX IX_ProductVendor_VendorID ON Purchasing..ProductVendor (VendorID);

#end
#begin
-- Add a column to an index
CREATE INDEX IX_FF ON dbo.FactFinance ( FinanceKey ASC, DateKey ASC );
--Rebuild and add the OrganizationKey
CREATE INDEX IX_FF ON dbo.FactFinance ( FinanceKey, DateKey, OrganizationKey DESC)
WITH ( DROP_EXISTING = ON );

#end
#begin
-- Create a unique nonclustered index
CREATE UNIQUE INDEX AK_UnitMeasure_Name
    ON Production.UnitMeasure(Name);
--Verify the existing value.
SELECT Name FROM Production.UnitMeasure WHERE Name = N'Ounces';
GO
INSERT INTO Production.UnitMeasure (UnitMeasureCode, Name, ModifiedDate)
    VALUES ('OC', 'Ounces', GetDate());

#end
#begin
--Use the IGNORE_DUP_KEY option
CREATE TABLE #Test (C1 nvarchar(10), C2 nvarchar(50), C3 datetime);
GO
CREATE UNIQUE INDEX AK_Index ON #Test (C2)
    WITH (IGNORE_DUP_KEY = ON);
GO
INSERT INTO #Test VALUES (N'OC', N'Ounces', GETDATE());
INSERT INTO #Test SELECT * FROM Production.UnitMeasure;
GO
SELECT COUNT(*)AS [Number of rows] FROM #Test;
GO
DROP TABLE #Test;
GO

CREATE TABLE #Test (C1 nvarchar(10), C2 nvarchar(50), C3 datetime);
GO
CREATE UNIQUE INDEX AK_Index ON #Test (C2)
    WITH (IGNORE_DUP_KEY = OFF);
GO
INSERT INTO #Test VALUES (N'OC', N'Ounces', GETDATE());
INSERT INTO #Test SELECT * FROM Production.UnitMeasure;
GO
SELECT COUNT(*)AS [Number of rows] FROM #Test;
GO
DROP TABLE #Test;
GO

#end
#begin
-- Using DROP_EXISTING to drop and re-create an index
CREATE NONCLUSTERED INDEX IX_WorkOrder_ProductID
    ON Production.WorkOrder(ProductID)
    WITH (FILLFACTOR = 80,
        PAD_INDEX = ON,
        DROP_EXISTING = ON);
GO

#end
#begin
-- Create an index on a view
-- Set the options to support indexed views.
--SET NUMERIC_ROUNDABORT OFF;
--SET ANSI_PADDING, ANSI_WARNINGS, CONCAT_NULL_YIELDS_NULL, ARITHABORT,
--    QUOTED_IDENTIFIER, ANSI_NULLS ON;
--GO
-- Create view with schemabinding.
--IF OBJECT_ID ('Sales.vOrders', 'view') IS NOT NULL
--DROP VIEW Sales.vOrders ;
--GO
--CREATE VIEW Sales.vOrders
--WITH SCHEMABINDING
--AS
--    SELECT SUM(UnitPrice*OrderQty*(1.00-UnitPriceDiscount)) AS Revenue,
--        OrderDate, ProductID, COUNT_BIG(*) AS COUNT
--    FROM Sales.SalesOrderDetail AS od, Sales.SalesOrderHeader AS o
--    WHERE od.SalesOrderID = o.SalesOrderID
--    GROUP BY OrderDate, ProductID;
--GO
--Create an index on the view.
--CREATE UNIQUE CLUSTERED INDEX IDX_V1
--    ON Sales.vOrders (OrderDate, ProductID);
--GO
--This query can use the indexed view even though the view is
--not specified in the FROM clause.
--SELECT SUM(UnitPrice*OrderQty*(1.00-UnitPriceDiscount)) AS Rev,
--    OrderDate, ProductID
--FROM Sales.SalesOrderDetail AS od
--    JOIN Sales.SalesOrderHeader AS o ON od.SalesOrderID=o.SalesOrderID
--        AND ProductID BETWEEN 700 and 800
--        AND OrderDate >= CONVERT(datetime,'05/01/2002',101)
--GROUP BY OrderDate, ProductID
--ORDER BY Rev DESC;
--GO
--This query can use the above indexed view.
--SELECT  OrderDate, SUM(UnitPrice*OrderQty*(1.00-UnitPriceDiscount)) AS Rev
--FROM Sales.SalesOrderDetail AS od
--    JOIN Sales.SalesOrderHeader AS o ON od.SalesOrderID=o.SalesOrderID
--        AND DATEPART(mm,OrderDate)= 3
--        AND DATEPART(yy,OrderDate) = 2002
--GROUP BY OrderDate
--ORDER BY OrderDate ASC;
--GO

#end
#begin
-- Create an index with included (non-key) columns
CREATE NONCLUSTERED INDEX IX_Address_PostalCode
    ON Person.Address (PostalCode)
    INCLUDE (AddressLine1, AddressLine2, City, StateProvinceID);
GO
SELECT AddressLine1, AddressLine2, City, StateProvinceID, PostalCode
FROM Person.Address
WHERE PostalCode BETWEEN N'98000' and N'99999';
GO

#end
#begin
-- Create a partitioned index
--CREATE NONCLUSTERED INDEX IX_TransactionHistory_ReferenceOrderID
--    ON Production.TransactionHistory (ReferenceOrderID)
--    ON TransactionsPS1 (TransactionDate);
--GO
#end
#begin
--Creating a filtered index
CREATE NONCLUSTERED INDEX "FIBillOfMaterialsWithEndDate"
    ON Production.BillOfMaterials (ComponentID, StartDate)
    WHERE EndDate IS NOT NULL;
#end
#begin
--Create a compressed index
--CREATE NONCLUSTERED INDEX IX_INDEX_1
--    ON T1 (C2)
--WITH ( DATA_COMPRESSION = ROW );
--GO

CREATE CLUSTERED INDEX IX_PartTab2Col1
ON PartitionTable1 (Col1)
WITH ( DATA_COMPRESSION = ROW );
GO

--CREATE CLUSTERED INDEX IX_PartTab2Col1
--ON PartitionTable1 (Col1)
--WITH (DATA_COMPRESSION = PAGE ON PARTITIONS(1),
--    DATA_COMPRESSION = ROW ON PARTITIONS (2 TO 4 ) ) ;
--GO
#end
#begin

CREATE INDEX IX_VendorID
    ON ProductVendor (VendorID);
CREATE INDEX IX_VendorID
    ON dbo.ProductVendor (VendorID DESC, Name ASC, Address DESC);
CREATE INDEX IX_VendorID
    ON Purchasing..ProductVendor (VendorID);

#end
#begin
-- Create a non-clustered index on a table in the current database
CREATE INDEX IX_ProductVendor_VendorID
    ON ProductVendor (VendorID);

#end
#begin
-- Create a clustered index on a table in another database
CREATE CLUSTERED INDEX IX_ProductVendor_VendorID
    ON Purchasing..ProductVendor (VendorID);

#end
#begin
-- Add a column to an index
CREATE INDEX IX_FF ON dbo.FactFinance (
    FinanceKey ASC, DateKey ASC );

--Rebuild and add the OrganizationKey
CREATE INDEX IX_FF ON dbo.FactFinance (
    FinanceKey, DateKey, OrganizationKey DESC)
WITH ( DROP_EXISTING = ON );

#end
