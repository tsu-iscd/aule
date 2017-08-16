-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-statistics-transact-sql

#begin
-- Using CREATE STATISTICS with SAMPLE number PERCENT
CREATE STATISTICS ContactMail1
    ON Person.Person (BusinessEntityID, EmailPromotion)
    WITH SAMPLE 5 PERCENT;

#end
#begin
-- Using CREATE STATISTICS with FULLSCAN and NORECOMPUTE
CREATE STATISTICS NamePurchase
    ON AdventureWorks2012.Person.Person (BusinessEntityID, EmailPromotion)
    WITH FULLSCAN, NORECOMPUTE;

#end
--#begin
-- Using CREATE STATISTICS to create filtered statistics
--CREATE STATISTICS ContactPromotion1
--    ON Person.Person (BusinessEntityID, LastName, EmailPromotion)
--WHERE EmailPromotion = 2
--WITH SAMPLE 50 PERCENT;
--GO

--#end
#begin
-- Create statistics on an external table
--Create statistics on an external table and use default sampling.
CREATE STATISTICS CustomerStats1 ON DimCustomer (CustomerKey, EmailAddress);

--Create statistics on an external table and scan all the rows
CREATE STATISTICS CustomerStats1 ON DimCustomer (CustomerKey, EmailAddress) WITH FULLSCAN;

#end
#begin
-- Create statistics on two columns
CREATE STATISTICS CustomerStats1 ON DimCustomer (CustomerKey, EmailAddress);

#end
#begin
-- Create statistics by using a full scan
CREATE STATISTICS CustomerStatsFullScan
ON DimCustomer (CustomerKey, EmailAddress) WITH FULLSCAN;

#end
#begin
-- Create statistics by specifying the sample percentage
CREATE STATISTICS CustomerStatsSampleScan
ON DimCustomer (CustomerKey, EmailAddress) WITH SAMPLE 50 PERCENT;
#end
