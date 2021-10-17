DROP TABLE IF EXISTS Order_Product;
DROP TABLE IF EXISTS "Order";
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Customer;

CREATE TABLE Product(
    ID serial PRIMARY KEY,
    ProductlineID INT,
    Name varchar (255),
    Scale INT,
    vendor varchar (255),
    PdtDescription varchar (255),
    QtylStock INT,
    BuyPrice numeric(19, 0),
    MSRP varchar (255)
);

CREATE TABLE Customer(
    ID serial PRIMARY KEY,
    salesRepEmployeeNum INT,
    "Name" varchar (255),
    LastName varchar (255),
    FirstName varchar (255),
    Phone varchar (255),
    Address1 varchar (255),
    Address2 varchar (255),
    City varchar (255),
    State varchar (255),
    PostalCode INT,
    Country varchar (255),
    CreditLimit numeric(19, 0)
);

CREATE TABLE "Order"(
    ID serial PRIMARY KEY,
    CustomerID INT REFERENCES Customer(ID),
    OrderDate timestamp,
    ShippedDate timestamp,
    Status INT,
    Comments varchar (255)
);

CREATE TABLE payment(
    CheckNum varchar (255) PRIMARY KEY,
    CustomerID INT REFERENCES Customer(ID),
    PaymentDate timestamp,
    Amount numeric(19, 0)
);

CREATE TABLE Order_product(
    ID SERIAL PRIMARY KEY,
    OrderID INT REFERENCES "Order"(ID),
    ProductCode INT REFERENCES Product(ID),
    Quantity INT,
    PriceEach numeric(19, 0)
);
