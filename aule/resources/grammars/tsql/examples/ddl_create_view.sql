-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql

#begin
-- Using a simple CREATE VIEW
CREATE VIEW hiredate_view
AS
SELECT p.FirstName, p.LastName, e.BusinessEntityID, e.HireDate
FROM HumanResources.Employee e
JOIN Person.Person AS p ON e.BusinessEntityID = p.BusinessEntityID ;
GO

#end
#begin
-- Using WITH ENCRYPTION
CREATE VIEW Purchasing.PurchaseOrderReject
WITH ENCRYPTION
AS
SELECT PurchaseOrderID, ReceivedQty, RejectedQty,
    RejectedQty / ReceivedQty AS RejectRatio, DueDate
FROM Purchasing.PurchaseOrderDetail
WHERE RejectedQty / ReceivedQty > 0
AND DueDate > CONVERT(DATETIME,'20010630',101) ;
GO

#end
#begin
-- Using WITH CHECK OPTION
CREATE VIEW dbo.SeattleOnly
AS
SELECT p.LastName, p.FirstName, e.JobTitle, a.City, sp.StateProvinceCode
FROM HumanResources.Employee e
INNER JOIN Person.Person p
ON p.BusinessEntityID = e.BusinessEntityID
    INNER JOIN Person.BusinessEntityAddress bea
    ON bea.BusinessEntityID = e.BusinessEntityID
    INNER JOIN Person.Address a
    ON a.AddressID = bea.AddressID
    INNER JOIN Person.StateProvince sp
    ON sp.StateProvinceID = a.StateProvinceID
WHERE a.City = 'Seattle'
WITH CHECK OPTION ;
GO

#end
#begin
-- Using built-in functions within a view
CREATE VIEW Sales.SalesPersonPerform
AS
SELECT TOP (100) SalesPersonID, SUM(TotalDue) AS TotalSales
FROM Sales.SalesOrderHeader
WHERE OrderDate > CONVERT(DATETIME,'20001231',101)
GROUP BY SalesPersonID;
GO
#end
#begin
-- Using partitioned data
--Create the tables and insert the values.
CREATE TABLE dbo.SUPPLY1 (
supplyID INT PRIMARY KEY CHECK (supplyID BETWEEN 1 and 150),
supplier CHAR(50)
);
CREATE TABLE dbo.SUPPLY2 (
supplyID INT PRIMARY KEY CHECK (supplyID BETWEEN 151 and 300),
supplier CHAR(50)
);
CREATE TABLE dbo.SUPPLY3 (
supplyID INT PRIMARY KEY CHECK (supplyID BETWEEN 301 and 450),
supplier CHAR(50)
);
CREATE TABLE dbo.SUPPLY4 (
supplyID INT PRIMARY KEY CHECK (supplyID BETWEEN 451 and 600),
supplier CHAR(50)
);
GO
INSERT dbo.SUPPLY1 VALUES ('1', 'CaliforniaCorp'), ('5', 'BraziliaLtd')
, ('231', 'FarEast'), ('280', 'NZ')
, ('321', 'EuroGroup'), ('442', 'UKArchip')
, ('475', 'India'), ('521', 'Afrique');
GO
--Create the view that combines all supplier tables.
CREATE VIEW dbo.all_supplier_view
WITH SCHEMABINDING
AS
SELECT supplyID, supplier
  FROM dbo.SUPPLY1
UNION ALL
SELECT supplyID, supplier
  FROM dbo.SUPPLY2
UNION ALL
SELECT supplyID, supplier
  FROM dbo.SUPPLY3
UNION ALL
SELECT supplyID, supplier
  FROM dbo.SUPPLY4;

#end
#begin
-- Creating a simple view
CREATE VIEW DimEmployeeBirthDates AS
SELECT FirstName, LastName, BirthDate
FROM DimEmployee;

#end
#begin
-- Create a view by joining two tables
CREATE VIEW view1
AS
SELECT fis.CustomerKey, fis.ProductKey, fis.OrderDateKey,
  fis.SalesTerritoryKey, dst.SalesTerritoryRegion
FROM FactInternetSales AS fis
LEFT OUTER JOIN DimSalesTerritory AS dst
ON (fis.SalesTerritoryKey=dst.SalesTerritoryKey);
#end

