-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-procedure-transact-sql
#begin
-- Creating a simple Transact-SQL procedure
IF OBJECT_ID ( 'HumanResources.uspGetAllEmployees', 'P' ) IS NOT NULL
    DROP PROCEDURE HumanResources.uspGetAllEmployees;
GO
CREATE PROCEDURE HumanResources.uspGetAllEmployees
AS
    SET NOCOUNT ON;
    SELECT LastName, FirstName, JobTitle, Department
    FROM HumanResources.vEmployeeDepartment;
GO

SELECT * FROM HumanResources.vEmployeeDepartment;

#end
#begin
-- Returning more than one result set
CREATE PROCEDURE dbo.uspMultipleResults
AS
SELECT TOP(10) BusinessEntityID, Lastname, FirstName FROM Person.Person;
SELECT TOP(10) CustomerID, AccountNumber FROM Sales.Customer;
GO

#end
--#begin
-- Creating a CLR stored procedure
--CREATE ASSEMBLY HandlingLOBUsingCLR
--FROM '\\MachineName\HandlingLOBUsingCLR\bin\Debug\HandlingLOBUsingCLR.dll';
--GO
--CREATE PROCEDURE dbo.GetPhotoFromDB
--(
--    @ProductPhotoID int,
--    @CurrentDirectory nvarchar(1024),
--    @FileName nvarchar(1024)
--)
--AS EXTERNAL NAME HandlingLOBUsingCLR.LargeObjectBinary.GetPhotoFromDB;
--GO

--#end
#begin
-- Creating a procedure with input parameters
IF OBJECT_ID ( 'HumanResources.uspGetEmployees', 'P' ) IS NOT NULL
    DROP PROCEDURE HumanResources.uspGetEmployees;
GO
CREATE PROCEDURE HumanResources.uspGetEmployees
    @LastName nvarchar(50),
    @FirstName nvarchar(50)
AS

    SET NOCOUNT ON;
    SELECT FirstName, LastName, JobTitle, Department
    FROM HumanResources.vEmployeeDepartment
    WHERE FirstName = @FirstName AND LastName = @LastName;
GO

#end
#begin
-- Using a procedure with wildcard parameters
IF OBJECT_ID ( 'HumanResources.uspGetEmployees2', 'P' ) IS NOT NULL
    DROP PROCEDURE HumanResources.uspGetEmployees2;
GO
CREATE PROCEDURE HumanResources.uspGetEmployees2
    @LastName nvarchar(50) = N'D%',
    @FirstName nvarchar(50) = N'%'
AS
    SET NOCOUNT ON;
    SELECT FirstName, LastName, JobTitle, Department
    FROM HumanResources.vEmployeeDepartment
    WHERE FirstName LIKE @FirstName AND LastName LIKE @LastName;
EXECUTE HumanResources.uspGetEmployees2;
-- Or
EXECUTE HumanResources.uspGetEmployees2 N'Wi%';
-- Or
EXECUTE HumanResources.uspGetEmployees2 @FirstName = N'%';
-- Or
EXECUTE HumanResources.uspGetEmployees2 N'[CK]ars[OE]n';
-- Or
EXECUTE HumanResources.uspGetEmployees2 N'Hesse', N'Stefen';
-- Or
EXECUTE HumanResources.uspGetEmployees2 N'H%', N'S%';
#end
#begin
-- Using OUTPUT parameters
IF OBJECT_ID ( 'Production.uspGetList', 'P' ) IS NOT NULL
    DROP PROCEDURE Production.uspGetList;
GO
CREATE PROCEDURE Production.uspGetList @Product varchar(40)
    , @MaxPrice money
    , @ComparePrice money OUTPUT
    , @ListPrice money OUT
AS
    SET NOCOUNT ON;
    SELECT p.[Name] AS Product, p.ListPrice AS 'List Price'
    FROM Production.Product AS p
    JOIN Production.ProductSubcategory AS s
      ON p.ProductSubcategoryID = s.ProductSubcategoryID
    WHERE s.[Name] LIKE @Product AND p.ListPrice < @MaxPrice;
-- Populate the output variable @ListPprice.
SET @ListPrice = (SELECT MAX(p.ListPrice)
        FROM Production.Product AS p
        JOIN  Production.ProductSubcategory AS s
          ON p.ProductSubcategoryID = s.ProductSubcategoryID
        WHERE s.[Name] LIKE @Product AND p.ListPrice < @MaxPrice);
-- Populate the output variable @compareprice.
SET @ComparePrice = @MaxPrice;
GO

DECLARE @ComparePrice money, @Cost money ;
EXECUTE Production.uspGetList '%Bikes%', 700,
    @ComparePrice OUT,
    @Cost OUTPUT
IF @Cost <= @ComparePrice
BEGIN
    PRINT 'These products can be purchased for less than
    $'+RTRIM(CAST(@ComparePrice AS varchar(20)))+'.'
END
ELSE
    PRINT 'The prices for all products in this category exceed
    $'+ RTRIM(CAST(@ComparePrice AS varchar(20)))+'.';
#end
--#begin
-- Using a Table-Valued Parameter
/* Create a table type. */
--CREATE TYPE LocationTableType AS TABLE
--( LocationName VARCHAR(50)
--, CostRate INT );
--GO

/* Create a procedure to receive data for the table-valued parameter. */
--CREATE PROCEDURE usp_InsertProductionLocation
--    @TVP LocationTableType READONLY
--    AS
--    SET NOCOUNT ON
--    INSERT INTO [AdventureWorks2012].[Production].[Location]
--           ([Name]
--           ,[CostRate]
--          ,[Availability]
--           ,[ModifiedDate])
--        SELECT *, 0, GETDATE()
--        FROM  @TVP;
--GO

/* Declare a variable that references the type. */
--DECLARE @LocationTVP
--AS LocationTableType;

/* Add data to the table variable. */
--INSERT INTO @LocationTVP (LocationName, CostRate)
--    SELECT [Name], 0.00
--    FROM
--    [AdventureWorks2012].[Person].[StateProvince];

/* Pass the table variable data to a stored procedure. */
--EXEC usp_InsertProductionLocation @LocationTVP;
--GO

--#end
--#begin
-- Using an OUTPUT cursor paramete
--IF OBJECT_ID ( 'dbo.uspCurrencyCursor', 'P' ) IS NOT NULL
--    DROP PROCEDURE dbo.uspCurrencyCursor;
--GO
--CREATE PROCEDURE dbo.uspCurrencyCursor
--    @CurrencyCursor CURSOR VARYING OUTPUT
--AS
--    SET NOCOUNT ON;
--    SET @CurrencyCursor = CURSOR
--    FORWARD_ONLY STATIC FOR
--      SELECT CurrencyCode, Name
--      FROM Sales.Currency;
--    OPEN @CurrencyCursor;
--GO

--DECLARE @MyCursor CURSOR;
--EXEC dbo.uspCurrencyCursor @CurrencyCursor = @MyCursor OUTPUT;
--WHILE (@@FETCH_STATUS = 0)
--BEGIN;
--     FETCH NEXT FROM @MyCursor;
--END;
--CLOSE @MyCursor;
--DEALLOCATE @MyCursor;
--GO

--#end
#begin
-- Using UPDATE in a stored procedure
CREATE PROCEDURE HumanResources.Update_VacationHours
@NewHours smallint
AS
SET NOCOUNT ON;
UPDATE HumanResources.Employee
SET VacationHours =
    ( CASE
         WHEN SalariedFlag = 0 THEN VacationHours + @NewHours
         ELSE @NewHours
       END
    )
WHERE CurrentFlag = 1;
GO

EXEC HumanResources.Update_VacationHours 40;
#end
#begin
-- Using TRY…CATCH
CREATE PROCEDURE Production.uspDeleteWorkOrder ( @WorkOrderID int )
AS
SET NOCOUNT ON;
BEGIN TRY
   BEGIN TRANSACTION
   -- Delete rows from the child table, WorkOrderRouting, for the specified work order.
   DELETE FROM Production.WorkOrderRouting
   WHERE WorkOrderID = @WorkOrderID;

   -- Delete the rows from the parent table, WorkOrder, for the specified work order.
   DELETE FROM Production.WorkOrder
   WHERE WorkOrderID = @WorkOrderID;

   COMMIT

END TRY
BEGIN CATCH
  -- Determine if an error occurred.
  IF @@TRANCOUNT > 0
     ROLLBACK

  -- Return the error information.
  DECLARE @ErrorMessage nvarchar(4000),  @ErrorSeverity int;
  SELECT @ErrorMessage = ERROR_MESSAGE(),@ErrorSeverity = ERROR_SEVERITY();
  RAISERROR(@ErrorMessage, @ErrorSeverity, 1);
END CATCH;

GO
EXEC Production.uspDeleteWorkOrder 13;

/* Intentionally generate an error by reversing the order in which rows
   are deleted from the parent and child tables. This change does not
   cause an error when the procedure definition is altered, but produces
   an error when the procedure is executed.
*/
ALTER PROCEDURE Production.uspDeleteWorkOrder ( @WorkOrderID int )
AS

BEGIN TRY
   BEGIN TRANSACTION
      -- Delete the rows from the parent table, WorkOrder, for the specified work order.
   DELETE FROM Production.WorkOrder
   WHERE WorkOrderID = @WorkOrderID;

   -- Delete rows from the child table, WorkOrderRouting, for the specified work order.
   DELETE FROM Production.WorkOrderRouting
   WHERE WorkOrderID = @WorkOrderID;

   COMMIT TRANSACTION

END TRY
BEGIN CATCH
  -- Determine if an error occurred.
  IF @@TRANCOUNT > 0
     ROLLBACK TRANSACTION

  -- Return the error information.
  DECLARE @ErrorMessage nvarchar(4000),  @ErrorSeverity int;
  SELECT @ErrorMessage = ERROR_MESSAGE(),@ErrorSeverity = ERROR_SEVERITY();
  RAISERROR(@ErrorMessage, @ErrorSeverity, 1);
END CATCH;
GO
-- Execute the altered procedure.
EXEC Production.uspDeleteWorkOrder 15;

DROP PROCEDURE Production.uspDeleteWorkOrder;

#end
#begin
-- Using the WITH ENCRYPTION option
IF OBJECT_ID ( 'HumanResources.uspEncryptThis', 'P' ) IS NOT NULL
    DROP PROCEDURE HumanResources.uspEncryptThis;
GO
CREATE PROCEDURE HumanResources.uspEncryptThis
WITH ENCRYPTION
AS
    SET NOCOUNT ON;
    SELECT BusinessEntityID, JobTitle, NationalIDNumber,
        VacationHours, SickLeaveHours
    FROM HumanResources.Employee;
GO

#end
#begin
-- Using the WITH RECOMPILE option
IF OBJECT_ID ( 'dbo.uspProductByVendor', 'P' ) IS NOT NULL
    DROP PROCEDURE dbo.uspProductByVendor;
GO
CREATE PROCEDURE dbo.uspProductByVendor @Name varchar(30) = '%'
WITH RECOMPILE
AS
    SET NOCOUNT ON;
    SELECT v.Name AS 'Vendor name', p.Name AS 'Product name'
    FROM Purchasing.Vendor AS v
    JOIN Purchasing.ProductVendor AS pv
      ON v.BusinessEntityID = pv.BusinessEntityID
    JOIN Production.Product AS p
      ON pv.ProductID = p.ProductID
    WHERE v.Name LIKE @Name;

#end
#begin
-- Using the EXECUTE AS clause
IF OBJECT_ID ( 'Purchasing.uspVendorAllInfo', 'P' ) IS NOT NULL
    DROP PROCEDURE Purchasing.uspVendorAllInfo;
GO
CREATE PROCEDURE Purchasing.uspVendorAllInfo
WITH EXECUTE AS CALLER
AS
    SET NOCOUNT ON;
    SELECT v.Name AS Vendor, p.Name AS 'Product name',
      v.CreditRating AS 'Rating',
      v.ActiveFlag AS Availability
    FROM Purchasing.Vendor v
    INNER JOIN Purchasing.ProductVendor pv
      ON v.BusinessEntityID = pv.BusinessEntityID
    INNER JOIN Production.Product p
      ON pv.ProductID = p.ProductID
    ORDER BY v.Name ASC;
GO

#end
--#begin
-- Creating custom permission sets
--CREATE PROCEDURE dbo.TruncateMyTable
--WITH EXECUTE AS SELF
--AS TRUNCATE TABLE MyDB..MyTable;
--#end
#begin
-- Create a Stored Procedure that runs a SELECT statement
-- Uses AdventureWorksDW database

--Run CREATE PROCEDURE as the first statement in a batch.
CREATE PROCEDURE Get10TopResellers
AS
BEGIN
    SELECT TOP (10) r.ResellerName, r.AnnualSales
    FROM DimReseller AS r
    ORDER BY AnnualSales DESC, ResellerName ASC;
END
;

--Show 10 Top Resellers
EXEC Get10TopResellers;
#end


