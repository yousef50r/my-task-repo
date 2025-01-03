CREATE DATABASE Product;
USE Product;
CREATE TABLE products (
    product_id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (product_id),
    product_name VARCHAR(255) NOT NULL,
    is_recyclable BOOLEAN NOT NULL,
    is_low_fat BOOLEAN NOT NULL
);

INSERT INTO products (product_name, is_recyclable, is_low_fat) 
VALUES ('Product A', TRUE, TRUE), ('Product B', TRUE, FALSE), ('Product C', FALSE, TRUE), ('Product D', TRUE, TRUE);

SELECT product_id, product_name
FROM products
WHERE is_recyclable = TRUE AND is_low_fat = TRUE;
