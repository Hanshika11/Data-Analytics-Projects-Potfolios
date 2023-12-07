#Product Sales Analysis using SQL
CREATE DATABASE Product_Sales;

CREATE TABLE Products(
ProductID INT PRIMARY KEY,
ProductName Varchar(50),
Price Decimal(10,2)
);

INSERT INTO Products (ProductID, ProductName,Price)
VALUES
(1,'Apple', 2.4),
(2,'Banna',3.5),
(3,'orange',9),
(4,'Mango',2.0);

CREATE TABLE Orders(
OrderID INT PRIMARY KEY,
ProductID INT,
Quantity INT,
Sales DECIMAL(10,2)
);

INSERT INTO Orders(OrderID, ProductID , Quantity, Sales)
Values
(1,1,10,25.0),
(2,1,5,12.5),
(3,2,8,12.0),
(4,3,12,36.0),
(5,4,6, 12.0); 

SELECT * FROM Products;
SELECT * FROM Orders;

#Now here’s how to solve the Product Sales Analysis problem using SQL:

SELECT p.productName, SUM(o.quantity * p.price) AS totalRevenue
FROM Products p
JOIN Orders o ON p.productID = o.productID
GROUP BY p.productName
ORDER BY totalRevenue DESC;