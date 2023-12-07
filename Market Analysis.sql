#Market Analysis: Problem Statement

CREATE DATABASE MARKET_ANALYSIS;
USE MARKET_ANALYSIS;
CREATE TABLE Sales(
CustomerID INT,
ProductID Char(1),
PurchaseDate DATE,
Quantity INT,
Revenue DECIMAL(10,2)
);
INSERT INTO Sales( CustomerID,Product PurchaseDate, Quantity, Revenue)
VALUES
(1,'A','2023-01-01', 5, 100),
(2,'B','2023-01-02', 3, 50),
(3,'A','2023-01-03',2 , 30),
(4,'C','2023-01-03',1,20),
(1,'B','2023-01-04',4, 80);

SELECT SUM(Revenue) As TotalRevenue FROM Sales;

#Calculating total sales by product:

SELECT ProductID, SUM(Quantity) AS TotalQuantity, SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY ProductID;

#Finding top customers by revenue:

SELECT CustomerID, SUM(Revenue) AS TotalRevenue
FROM  Sales
GROUP BY CustomerID
ORDER BY TOtalRevenue DESC
LIMIT 5;
