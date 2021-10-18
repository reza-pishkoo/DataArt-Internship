-- query1
-- the tables file

-- query2
ALTER TABLE customer COLUMN postalcode;

-- query3
UPDATE payment
SET amount = 2500
WHERE checknum = '1234';

-- query4
SELECT * FROM customer
WHERE city = 'tehran';

-- query5
SELECT lastname FROM customer
WHERE address1 LIKE '%azadi%' OR address2 LIKE '%azadi%';

-- query6
SELECT customer_order.firstname FROM
(SELECT order_product.orderid, "Order".id, "Order".customerid, customer.id, customer.firstname
FROM order_product
join "Order" ON order_product.orderid = "Order".id
join customer ON "Order".customerid = customer.id)AS customer_order
WHERE customer_order.orderid = 123;

-- query7
CREATE OR REPLACE FUNCTION get_orderid (first_name varchar(255)) 
    RETURNS TABLE (
        custome_orderid INT
) 
AS $$
BEGIN
    RETURN QUERY SELECT
        customer_order.orderid
        FROM
            (SELECT order_product.orderid, "Order".id, "Order".customerid, customer.id, customer.firstname
            FROM order_product
            join "Order" ON order_product.orderid = "Order".id
            join customer ON "Order".customerid = customer.id)AS customer_order
            WHERE customer_order.firstname = first_name;
END; $$ 
LANGUAGE 'plpgsql';

-- query8
SELECT firstname, lastname, name, total FROM
    (SELECT customer.firstname, customer.lastname, product.name, order_product.quantity * order_product.priceeach AS total FROM order_product
    INNER JOIN "Order" ON "Order".id = order_product.orderid
    INNER JOIN customer ON customer.Id = "Order".customerid
    INNER JOIN product ON order_product.productcode = product.ID) as total_order
    WHERE total_order.total > 1000
        AND NOT EXISTS(SELECT customerID FROM payment WHERE paymentdate < '2019-01-01'::date);

