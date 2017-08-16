-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-trigger-transact-sql

#begin
-- Using a DML trigger with a reminder message
CREATE TRIGGER reminder1
ON Sales.Customer
AFTER INSERT, UPDATE
AS RAISERROR ('Notify Customer Relations', 16, 10);
GO

#end
#begin
-- Using a DML trigger with a reminder e-mail message
CREATE TRIGGER reminder2
ON Sales.Customer
AFTER INSERT, UPDATE, DELETE
AS
   EXEC msdb.dbo.sp_send_dbmail
        @profile_name = 'AdventureWorks2012 Administrator',
        @recipients = 'danw@Adventure-Works.com',
        @body = 'Don''t forget to print a report for the sales force.',
        @subject = 'Reminder';
GO

#end
#begin
-- Using a DML AFTER trigger to enforce a business rule between the PurchaseOrderHeader and Vendor tables
-- This trigger prevents a row from being inserted in the Purchasing.PurchaseOrderHeader
-- table when the credit rating of the specified vendor is set to 5 (below average).

CREATE TRIGGER Purchasing.LowCredit ON Purchasing.PurchaseOrderHeader
AFTER INSERT
AS
IF EXISTS (SELECT *
           FROM Purchasing.PurchaseOrderHeader AS p
           JOIN inserted AS i
           ON p.PurchaseOrderID = i.PurchaseOrderID
           JOIN Purchasing.Vendor AS v
           ON v.BusinessEntityID = p.VendorID
           WHERE v.CreditRating = 5
          )
BEGIN
RAISERROR ('A vendor''s credit rating is too low to accept new
purchase orders.', 16, 1);
ROLLBACK TRANSACTION;
RETURN
END;
GO

-- This statement attempts to insert a row into the PurchaseOrderHeader table
-- for a vendor that has a below average credit rating.
-- The AFTER INSERT trigger is fired and the INSERT transaction is rolled back.

INSERT INTO Purchasing.PurchaseOrderHeader (RevisionNumber, Status, EmployeeID,
VendorID, ShipMethodID, OrderDate, ShipDate, SubTotal, TaxAmt, Freight)
VALUES (
2
,3
,261
,1652
,4
,GETDATE()
,GETDATE()
,44594.55
,3567.564
,1114.8638 );
GO

#end
#begin
-- Using a database-scoped DDL trigger
CREATE TRIGGER safety
ON DATABASE
FOR DROP_SYNONYM
AS
   RAISERROR ('You must disable Trigger "safety" to drop synonyms!',10, 1)
   ROLLBACK
GO
DROP TRIGGER safety
ON DATABASE;
GO

#end
#begin
-- Using a server-scoped DDL trigger
CREATE TRIGGER ddl_trig_database
ON ALL SERVER
FOR CREATE_DATABASE
AS
    PRINT 'Database Created.'
    SELECT EVENTDATA().value('(/EVENT_INSTANCE/TSQLCommand/CommandText)[1]','nvarchar(max)')
GO
DROP TRIGGER ddl_trig_database
ON ALL SERVER;
GO

#end
--#begin
--  Using a logon trigger
--USE master;
--GO
--CREATE LOGIN login_test WITH PASSWORD = '3KHJ6dhx(0xVYsdf' MUST_CHANGE,
--    CHECK_EXPIRATION = ON;
--GO
--GRANT VIEW SERVER STATE TO login_test;
--GO
--CREATE TRIGGER connection_limit_trigger
--ON ALL SERVER WITH EXECUTE AS 'login_test'
--FOR LOGON
--AS
--BEGIN
--IF ORIGINAL_LOGIN()= 'login_test' AND
--    (SELECT COUNT(*) FROM sys.dm_exec_sessions
--            WHERE is_user_process = 1 AND
--                original_login_name = 'login_test') > 3
--    ROLLBACK;
--END;

--#end
#begin
-- Viewing the events that cause a trigger to fire
SELECT TE.*
FROM sys.trigger_events AS TE
JOIN sys.triggers AS T ON T.object_id = TE.object_id
WHERE T.parent_class = 0 AND T.name = 'safety';
GO
#end
