-- https://docs.microsoft.com/en-us/sql/t-sql/statements/create-database-sql-server-transact-sql

#begin
-- Creating a database without specifying files
USE master;
GO
CREATE DATABASE mytest;
GO
-- Verify the database files and sizes
SELECT name, size, size*1.0/128 AS [Size in MBs]
FROM sys.master_files
WHERE name = N'mytest';
GO

#end
#begin
-- Creating a database that specifies the data and transaction log files

USE master;
GO
CREATE DATABASE Sales
ON
( NAME = Sales_dat,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\saledat.mdf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5 )
LOG ON
( NAME = Sales_log,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\salelog.ldf',
    SIZE = 5MB,
    MAXSIZE = 25MB,
    FILEGROWTH = 5MB ) ;
GO

#end
#begin
-- Creating a database by specifying multiple data and transaction log files
USE master;
GO
CREATE DATABASE Archive
ON
PRIMARY
    (NAME = Arch1,
    FILENAME = 'D:\SalesData\archdat1.mdf',
    SIZE = 100MB,
    MAXSIZE = 200,
    FILEGROWTH = 20),
    ( NAME = Arch2,
    FILENAME = 'D:\SalesData\archdat2.ndf',
    SIZE = 100MB,
    MAXSIZE = 200,
    FILEGROWTH = 20),
    ( NAME = Arch3,
    FILENAME = 'D:\SalesData\archdat3.ndf',
    SIZE = 100MB,
    MAXSIZE = 200,
    FILEGROWTH = 20)
LOG ON
   (NAME = Archlog1,
    FILENAME = 'D:\SalesData\archlog1.ldf',
    SIZE = 100MB,
    MAXSIZE = 200,
    FILEGROWTH = 20),
   (NAME = Archlog2,
    FILENAME = 'D:\SalesData\archlog2.ldf',
    SIZE = 100MB,
    MAXSIZE = 200,
    FILEGROWTH = 20) ;
GO
#end
#begin
-- Creating a database that has filegroups
USE master;
GO
CREATE DATABASE Sales
ON PRIMARY
( NAME = SPri1_dat,
    FILENAME = 'D:\SalesData\SPri1dat.mdf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 15% ),
( NAME = SPri2_dat,
    FILENAME = 'D:\SalesData\SPri2dt.ndf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 15% ),
FILEGROUP SalesGroup1
( NAME = SGrp1Fi1_dat,
    FILENAME = 'D:\SalesData\SG1Fi1dt.ndf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5 ),
( NAME = SGrp1Fi2_dat,
    FILENAME = 'D:\SalesData\SG1Fi2dt.ndf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5 ),
FILEGROUP SalesGroup2
( NAME = SGrp2Fi1_dat,
    FILENAME = 'D:\SalesData\SG2Fi1dt.ndf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5 ),
( NAME = SGrp2Fi2_dat,
    FILENAME = 'D:\SalesData\SG2Fi2dt.ndf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5 )
LOG ON
( NAME = Sales_log,
    FILENAME = 'E:\SalesLog\salelog.ldf',
    SIZE = 5MB,
    MAXSIZE = 25MB,
    FILEGROWTH = 5MB ) ;
GO
#end
--#begin
-- Attaching a database
--USE master;
--GO
--sp_detach_db Archive;
--GO
--CREATE DATABASE Archive
 --     ON (FILENAME = 'D:\SalesData\archdat1.mdf')
--      FOR ATTACH;
--GO

--#end
--#begin
-- Creating a database snapshot
--USE master;
--GO
--CREATE DATABASE sales_snapshot0600 ON
 --   ( NAME = SPri1_dat, FILENAME = 'D:\SalesData\SPri1dat_0600.ss'),
 --   ( NAME = SPri2_dat, FILENAME = 'D:\SalesData\SPri2dt_0600.ss'),
  --  ( NAME = SGrp1Fi1_dat, FILENAME = 'D:\SalesData\SG1Fi1dt_0600.ss'),
 --   ( NAME = SGrp1Fi2_dat, FILENAME = 'D:\SalesData\SG1Fi2dt_0600.ss'),
 --   ( NAME = SGrp2Fi1_dat, FILENAME = 'D:\SalesData\SG2Fi1dt_0600.ss'),
 --   ( NAME = SGrp2Fi2_dat, FILENAME = 'D:\SalesData\SG2Fi2dt_0600.ss')
--AS SNAPSHOT OF Sales ;
--GO

--#end
--#begin
-- Creating a database and specifying a collation name and options
--USE master;
--GO
--IF DB_ID (N'MyOptionsTest') IS NOT NULL
--DROP DATABASE MyOptionsTest;
--GO
--CREATE DATABASE MyOptionsTest
--COLLATE French_CI_AI
--WITH TRUSTWORTHY ON, DB_CHAINING ON;
--GO
--Verifying collation and option settings.
--SELECT name, collation_name, is_trustworthy_on, is_db_chaining_on
--FROM sys.databases
--WHERE name = N'MyOptionsTest';
--GO

--#end
--#begin
-- Attaching a full-text catalog that has been moved
--USE master;
--GO
--Detach the AdventureWorks2012 database
--sp_detach_db AdventureWorks2012;
--GO
-- Physically move the full text catalog to the new location.
--Attach the AdventureWorks2012 database and specify the new location of the full-text catalog.
--CREATE DATABASE AdventureWorks2012 ON
--    (FILENAME = 'c:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\Data\AdventureWorks2012_data.mdf'),
--    (FILENAME = 'c:\Program Files\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\Data\AdventureWorks2012_log.ldf'),
--    (FILENAME = 'c:\myFTCatalogs\AdvWksFtCat')
--FOR ATTACH;
--GO

--#end
#begin
-- Creating a database that specifies a row filegroup and two FILESTREAM filegroups
USE master;
GO
-- Get the SQL Server data path.
DECLARE @data_path nvarchar(256);
SET @data_path = (SELECT SUBSTRING(physical_name, 1, CHARINDEX(N'master.mdf', LOWER(physical_name)) - 1)
                  FROM master.sys.master_files
                  WHERE database_id = 1 AND file_id = 1);

 -- Execute the CREATE DATABASE statement.
EXECUTE ('CREATE DATABASE FileStreamDB
ON PRIMARY
    (
    NAME = FileStreamDB_data
    ,FILENAME = ''' + @data_path + 'FileStreamDB_data.mdf''
    ,SIZE = 10MB
    ,MAXSIZE = 50MB
    ,FILEGROWTH = 15%
    ),
FILEGROUP FileStreamPhotos CONTAINS FILESTREAM DEFAULT
    (
    NAME = FSPhotos
    ,FILENAME = ''C:\MyFSfolder\Photos''
-- SIZE and FILEGROWTH should not be specified here.
-- If they are specified an error will be raised.
, MAXSIZE = 5000 MB
    ),
    (
      NAME = FSPhotos2
      , FILENAME = ''D:\MyFSfolder\Photos''
      , MAXSIZE = 10000 MB
     ),
FILEGROUP FileStreamResumes CONTAINS FILESTREAM
    (
    NAME = FileStreamResumes
    ,FILENAME = ''C:\MyFSfolder\Resumes''
    )
LOG ON
    (
    NAME = FileStream_log
    ,FILENAME = ''' + @data_path + 'FileStreamDB_log.ldf''
    ,SIZE = 5MB
    ,MAXSIZE = 25MB
    ,FILEGROWTH = 5MB
    )'
);
GO
#end
--#begin
-- Creating a database that has a FILESTREAM filegroup with multiple files
--USE master;
--GO

--CREATE DATABASE [BlobStore1]
--CONTAINMENT = NONE
--ON PRIMARY
--(
--   NAME = N'BlobStore1',
--    FILENAME = N'C:\BlobStore\BlobStore1.mdf',
--    SIZE = 100MB,
--    MAXSIZE = UNLIMITED,
--    FILEGROWTH = 1MB
--),
--FILEGROUP [FS] CONTAINS FILESTREAM DEFAULT
--(
--    NAME = N'FS1',
--    FILENAME = N'C:\BlobStore\FS1',
--    MAXSIZE = UNLIMITED
--),
--(
--    NAME = N'FS2',
--    FILENAME = N'C:\BlobStore\FS2',
--    MAXSIZE = 100MB
--)
--LOG ON
--(
--    NAME = N'BlobStore1_log',
--    FILENAME = N'C:\BlobStore\BlobStore1_log.ldf',
--    SIZE = 100MB,
--    MAXSIZE = 1GB,
--    FILEGROWTH = 1MB
--);
--GO

--ALTER DATABASE [BlobStore1]
--ADD FILE
--(
--    NAME = N'FS3',
--    FILENAME = N'C:\BlobStore\FS3',
--    MAXSIZE = 100MB
--)
--TO FILEGROUP [FS];
--GO

--#end

#begin
-- from https://github.com/PositiveTechnologies/grammars-v4/blob/b94306b840b84fabb4acd54fc019b5797d7caf43/tsql/examples/ddl_create_alter_database.sql
USE [master]
GO

/****** Object:  Database [TestDb]    Script Date: 21/06/2016 07:38:14 ******/
CREATE DATABASE [TestDb]
 CONTAINMENT = NONE
 ON  PRIMARY
( NAME = N'TestDb', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.SQLEXPRESS\MSSQL\DATA\TestDb.mdf' , SIZE = 4288KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON
( NAME = N'TestDb_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.SQLEXPRESS\MSSQL\DATA\TestDb_log.ldf' , SIZE = 1072KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO

ALTER DATABASE [TestDb] SET COMPATIBILITY_LEVEL = 120
GO

ALTER DATABASE [TestDb] SET ANSI_NULL_DEFAULT OFF
GO

ALTER DATABASE [TestDb] SET ANSI_NULLS OFF
GO

ALTER DATABASE [TestDb] SET ANSI_PADDING OFF
GO

ALTER DATABASE [TestDb] SET ANSI_WARNINGS OFF
GO

ALTER DATABASE [TestDb] SET ARITHABORT OFF
GO

ALTER DATABASE [TestDb] SET AUTO_CLOSE OFF
GO

ALTER DATABASE [TestDb] SET AUTO_SHRINK OFF
GO

ALTER DATABASE [TestDb] SET AUTO_UPDATE_STATISTICS ON
GO

ALTER DATABASE [TestDb] SET CURSOR_CLOSE_ON_COMMIT OFF
GO

ALTER DATABASE [TestDb] SET CURSOR_DEFAULT  GLOBAL
GO

ALTER DATABASE [TestDb] SET CONCAT_NULL_YIELDS_NULL OFF
GO

ALTER DATABASE [TestDb] SET NUMERIC_ROUNDABORT OFF
GO

ALTER DATABASE [TestDb] SET QUOTED_IDENTIFIER OFF
GO

ALTER DATABASE [TestDb] SET RECURSIVE_TRIGGERS OFF
GO

ALTER DATABASE [TestDb] SET  ENABLE_BROKER
GO

ALTER DATABASE [TestDb] SET AUTO_UPDATE_STATISTICS_ASYNC OFF
GO

ALTER DATABASE [TestDb] SET DATE_CORRELATION_OPTIMIZATION OFF
GO

ALTER DATABASE [TestDb] SET TRUSTWORTHY OFF
GO

ALTER DATABASE [TestDb] SET ALLOW_SNAPSHOT_ISOLATION OFF
GO

ALTER DATABASE [TestDb] SET PARAMETERIZATION SIMPLE
GO

ALTER DATABASE [TestDb] SET READ_COMMITTED_SNAPSHOT OFF
GO

ALTER DATABASE [TestDb] SET HONOR_BROKER_PRIORITY OFF
GO

ALTER DATABASE [TestDb] SET RECOVERY SIMPLE
GO

ALTER DATABASE [TestDb] SET  MULTI_USER
GO

ALTER DATABASE [TestDb] SET PAGE_VERIFY CHECKSUM
GO

ALTER DATABASE [TestDb] SET DB_CHAINING OFF
GO

ALTER DATABASE [TestDb] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF )
GO

ALTER DATABASE [TestDb] SET TARGET_RECOVERY_TIME = 0 SECONDS
GO

ALTER DATABASE [TestDb] SET DELAYED_DURABILITY = DISABLED
GO

ALTER DATABASE [TestDb] SET  READ_WRITE
GO

USE master;
GO
CREATE DATABASE FileStreamDB
ON PRIMARY
    (
    NAME = FileStreamDB_data
    ,FILENAME = ''
    ,SIZE = 10MB
    ,MAXSIZE = 50MB
    ,FILEGROWTH = 15%
    ),
FILEGROUP FileStreamPhotos CONTAINS FILESTREAM DEFAULT
    (
    NAME = FSPhotos
    ,FILENAME = 'C:\MyFSfolderPhotos'
, MAXSIZE = 5000 MB
    ),
    (
      NAME = FSPhotos2
      , FILENAME = 'D:\MyFSfolderPhotos'
      , MAXSIZE = 10000 MB
     ),
FILEGROUP FileStreamResumes CONTAINS FILESTREAM
    (
    NAME = FileStreamResumes
    ,FILENAME = 'C:\MyFSfolderResumes'
    )
LOG ON
    (
    NAME = FileStream_log
    ,FILENAME = 'FileStreamDB_log.ldf'
    ,SIZE = 5MB
    ,MAXSIZE = 25MB
    ,FILEGROWTH = 5MB
    )
GO
#end
