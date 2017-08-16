#begin
-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql
CREATE TABLE dbo.Employee 
(
	EmployeeID int PRIMARY KEY CLUSTERED, 
	SalesPersonID int NULL REFERENCES SalesPerson(SalesPersonID)
);  
CREATE TABLE dbo.Employee 
(
	EmployeeID int PRIMARY KEY CLUSTERED, 
	ProductID int, 
	SpecialOfferID int, 
	CONSTRAINT FK_SpecialOfferProduct_SalesOrderDetail FOREIGN KEY (ProductID, SpecialOfferID) REFERENCES SpecialOfferProduct (ProductID, SpecialOfferID)
);
#end
#begin
-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql
-- -- F. Showing the complete table definition
-- TODO: make working
/*
CREATE TABLE dbo.PurchaseOrderDetail  
(  
    PurchaseOrderID int NOT NULL  
        REFERENCES Purchasing.PurchaseOrderHeader(PurchaseOrderID),  
    LineNumber smallint NOT NULL,  
    ProductID int NULL   
        REFERENCES Production.Product(ProductID),  
    UnitPrice money NULL,  
    OrderQty smallint NULL,  
    ReceivedQty float NULL,  
    RejectedQty float NULL,  
    DueDate datetime NULL,  
    rowguid uniqueidentifier ROWGUIDCOL  NOT NULL  
        CONSTRAINT DF_PurchaseOrderDetail_rowguid DEFAULT (newid()),  
    ModifiedDate datetime NOT NULL   
        CONSTRAINT DF_PurchaseOrderDetail_ModifiedDate DEFAULT (getdate()),  
    LineTotal  AS ((UnitPrice*OrderQty)),  
    StockedQty  AS ((ReceivedQty-RejectedQty)),  
    CONSTRAINT PK_PurchaseOrderDetail_PurchaseOrderID_LineNumber  
               PRIMARY KEY CLUSTERED (PurchaseOrderID, LineNumber)  
               WITH (IGNORE_DUP_KEY = OFF)  
);
*/
#end