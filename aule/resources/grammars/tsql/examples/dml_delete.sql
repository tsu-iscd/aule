#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using DELETE with no WHERE clause

DELETE FROM Sales.SalesPersonQuotaHistory;
GO

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using the WHERE clause to delete a set of rows

DELETE FROM Production.ProductCostHistory
WHERE StandardCost > 1000.00;
GO

DELETE Production.ProductCostHistory
WHERE StandardCost BETWEEN 12.00 AND 14.00
      AND EndDate IS NULL;
PRINT 'Number of rows deleted is ' + CAST(@@ROWCOUNT as char(3));

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using a cursor to determine the row to delete

DECLARE complex_cursor CURSOR FOR
    SELECT a.BusinessEntityID
    FROM HumanResources.EmployeePayHistory AS a
    WHERE RateChangeDate <>
         (SELECT MAX(RateChangeDate)
          FROM HumanResources.EmployeePayHistory AS b
          WHERE a.BusinessEntityID = b.BusinessEntityID) ;
OPEN complex_cursor;
FETCH FROM complex_cursor;
DELETE FROM HumanResources.EmployeePayHistory
WHERE CURRENT OF complex_cursor;
CLOSE complex_cursor;
DEALLOCATE complex_cursor;
GO

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using joins and subqueries to data in one table to delete rows in another table

DELETE FROM Sales.SalesPersonQuotaHistory
WHERE BusinessEntityID IN
    (SELECT BusinessEntityID
     FROM Sales.SalesPerson
     WHERE SalesYTD > 2500000.00);
GO

DELETE FROM Sales.SalesPersonQuotaHistory
FROM Sales.SalesPersonQuotaHistory AS spqh
INNER JOIN Sales.SalesPerson AS sp
ON spqh.BusinessEntityID = sp.BusinessEntityID
WHERE sp.SalesYTD > 2500000.00;
GO

DELETE spqh
  FROM
               Sales.SalesPersonQuotaHistory AS spqh
    INNER JOIN Sales.SalesPerson             AS sp  ON spqh.BusinessEntityID = sp.BusinessEntityID
  WHERE
    sp.SalesYTD > 2500000.00;

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using TOP to limit the number of rows deleted

DELETE TOP (20)
FROM Purchasing.PurchaseOrderDetail
WHERE DueDate < '20020701';
GO

DELETE FROM Purchasing.PurchaseOrderDetail
WHERE PurchaseOrderDetailID IN
   (SELECT TOP 10 PurchaseOrderDetailID
    FROM Purchasing.PurchaseOrderDetail
    ORDER BY DueDate ASC);
GO

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Deleting data from a remote table by using a linked server

USE master;
GO
-- Create a link to the remote data source.
-- Specify a valid server name for @datasrc as 'server_name' or 'server_name\instance_name'.

EXEC sp_addlinkedserver @server = N'MyLinkServer',
    @srvproduct = N' ',
    @provider = N'SQLNCLI',
    @datasrc = N'server_name',
    @catalog = N'AdventureWorks2012';
GO

DELETE MyLinkServer.AdventureWorks2012.HumanResources.Department WHERE DepartmentID > 16;
GO

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Deleting data from a remote table by using the OPENQUERY function

DELETE OPENQUERY (MyLinkServer, 'SELECT Name, GroupName FROM AdventureWorks2012.HumanResources.Department
WHERE DepartmentID = 18');
GO

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Deleting data from a remote table by using the OPENDATASOURCE function

DELETE FROM OPENDATASOURCE('SQLNCLI',
    'Data Source= <server_name>; Integrated Security=SSPI')
    .AdventureWorks2012.HumanResources.Department
WHERE DepartmentID = 17;

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using DELETE with the OUTPUT clause

DELETE Sales.ShoppingCartItem
OUTPUT DELETED.*
WHERE ShoppingCartID = 20621;

--Verify the rows in the table matching the WHERE clause have been deleted.
SELECT COUNT(*) AS [Rows in Table] FROM Sales.ShoppingCartItem WHERE ShoppingCartID = 20621;
GO

#end
#begin
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Using OUTPUT with <from_table_name> in a DELETE statement

DECLARE @MyTableVar table (
    ProductID int NOT NULL,
    ProductName nvarchar(50)NOT NULL,
    ProductModelID int NOT NULL,
    PhotoID int NOT NULL);

DELETE Production.ProductProductPhoto
OUTPUT DELETED.ProductID,
       p.Name,
       p.ProductModelID,
       DELETED.ProductPhotoID
    INTO @MyTableVar
FROM Production.ProductProductPhoto AS ph
JOIN Production.Product as p
    ON ph.ProductID = p.ProductID
    WHERE p.ProductModelID BETWEEN 120 and 130;

--Display the results of the table variable.
SELECT ProductID, ProductName, ProductModelID, PhotoID
FROM @MyTableVar
ORDER BY ProductModelID;
GO

#end