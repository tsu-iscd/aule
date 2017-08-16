--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#begin
-- https://docs.microsoft.com/en-us/sql/t-sql/language-elements/else-if-else-transact-sql
-- IF...ELSE
-- Using a simple Boolean expression
IF 1 = 1 PRINT 'Boolean_expression is true.'
ELSE PRINT 'Boolean_expression is false.' ;

IF 1 = 2 PRINT 'Boolean_expression is true.'
ELSE PRINT 'Boolean_expression is false.' ;
GO

#end
#begin
-- Using a query as part of a Boolean expression
USE AdventureWorks2012;
GO
IF
(SELECT COUNT(*) FROM Production.Product WHERE Name LIKE 'Touring-3000%' ) > 5
PRINT 'There are more than 5 Touring-3000 bicycles.'
ELSE PRINT 'There are 5 or less Touring-3000 bicycles.' ;
GO

#end
#begin
-- Using a statement block
USE AdventureWorks2012;
GO
DECLARE @AvgWeight decimal(8,2), @BikeCount int
IF
(SELECT COUNT(*) FROM Production.Product WHERE Name LIKE 'Touring-3000%' ) > 5
BEGIN
   SET @BikeCount =
        (SELECT COUNT(*)
         FROM Production.Product
         WHERE Name LIKE 'Touring-3000%');
   SET @AvgWeight =
        (SELECT AVG(Weight)
         FROM Production.Product
         WHERE Name LIKE 'Touring-3000%');
   PRINT 'There are ' + CAST(@BikeCount AS varchar(3)) + ' Touring-3000 bikes.'
   PRINT 'The average weight of the top 5 Touring-3000 bikes is ' + CAST(@AvgWeight AS varchar(8)) + '.';
END
ELSE
BEGIN
SET @AvgWeight =
        (SELECT AVG(Weight)
         FROM Production.Product
         WHERE Name LIKE 'Touring-3000%' );
   PRINT 'Average weight of the Touring-3000 bikes is ' + CAST(@AvgWeight AS varchar(8)) + '.' ;
END ;
GO

#end
#begin
-- Using nested IF...ELSE statements
DECLARE @Number int;
SET @Number = 50;
IF @Number > 100
   PRINT 'The number is large.';
ELSE
   BEGIN
      IF @Number < 10
      PRINT 'The number is small.';
   ELSE
      PRINT 'The number is medium.';
   END ;
GO

#end
#begin
-- Using a query as part of a Boolean expression
-- Uses AdventureWorks

DECLARE @maxWeight float, @productKey integer
SET @maxWeight = 100.00
SET @productKey = 424
IF @maxWeight <= (SELECT Weight from DimProduct WHERE ProductKey=@productKey)
    (SELECT @productKey, EnglishDescription, Weight, 'This product is too heavy to ship and is only available for pickup.' FROM DimProduct WHERE ProductKey=@productKey)
ELSE
    (SELECT @productKey, EnglishDescription, Weight, 'This product is available for shipping or pickup.' FROM DimProduct WHERE ProductKey=@productKey)
#end
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#begin
-- https://docs.microsoft.com/en-us/sql/t-sql/language-elements/return-transact-sql
-- RETURN
--  Returning from a procedure
CREATE PROCEDURE findjobs @nm sysname = NULL
AS
IF @nm IS NULL
    BEGIN
        PRINT 'You must give a user name'
        RETURN
    END
ELSE
    BEGIN
        SELECT o.name, o.id, o.uid
        FROM sysobjects o INNER JOIN master..syslogins l
            ON o.uid = l.sid
        WHERE l.name = @nm
    END;

#end
#begin
-- Returning status codes

USE AdventureWorks2012;
GO
CREATE PROCEDURE checkstate @param varchar(11)
AS
IF (SELECT StateProvince FROM Person.vAdditionalContactInfo WHERE ContactID = @param) = 'WA'
    RETURN 1
ELSE
    RETURN 2;
GO

#end
#begin
DECLARE @return_status int;
EXEC @return_status = checkstate '2';
SELECT 'Return Status' = @return_status;
GO

#end
#begin
DECLARE @return_status int;
EXEC @return_status = checkstate '6';
SELECT 'Return Status' = @return_status;
GO

#end
#begin
DECLARE @return_status int
EXEC @return_status = checkstate '12345678901';
SELECT 'Return Status' = @return_status;
GO
#end
--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- WHILE
-- https://docs.microsoft.com/en-us/sql/t-sql/language-elements/while-transact-sql
#begin
-- Using BREAK and CONTINUE with nested IF...ELSE and WHILE
USE AdventureWorks2012;
GO
WHILE (SELECT AVG(ListPrice) FROM Production.Product) < $300
BEGIN
   UPDATE Production.Product
      SET ListPrice = ListPrice * 2
   SELECT MAX(ListPrice) FROM Production.Product
   IF (SELECT MAX(ListPrice) FROM Production.Product) > $500
      BREAK
   ELSE
      CONTINUE
END
PRINT 'Too much for the market to bear';

#end
#begin
-- Using WHILE in a cursor
DECLARE Employee_Cursor CURSOR FOR
SELECT EmployeeID, Title
FROM AdventureWorks2012.HumanResources.Employee
WHERE JobTitle = 'Marketing Specialist';
OPEN Employee_Cursor;
FETCH NEXT FROM Employee_Cursor;
WHILE @@FETCH_STATUS = 0
   BEGIN
      FETCH NEXT FROM Employee_Cursor;
   END;
CLOSE Employee_Cursor;
DEALLOCATE Employee_Cursor;
GO

#end
#begin
-- Simple While Loop
-- Uses AdventureWorks

WHILE ( SELECT AVG(ListPrice) FROM dbo.DimProduct) < $300
BEGIN
    UPDATE dbo.DimProduct
        SET ListPrice = ListPrice * 2;
    SELECT MAX ( ListPrice) FROM dbo.DimProduct
    IF ( SELECT MAX (ListPrice) FROM dbo.DimProduct) > $500
        BREAK;
END
#end
