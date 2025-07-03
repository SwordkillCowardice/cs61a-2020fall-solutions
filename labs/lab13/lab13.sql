.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;


CREATE TABLE good_item AS
  SELECT MIN(MSRP / rating) AS good FROM products GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT name, store FROM products, good_item, lowest_prices WHERE name = item and MSRP / rating = good;
  

CREATE TABLE total_bandwidth AS
  SELECT SUM(b.Mbs) FROM shopping_list AS a, stores AS b WHERE a.store = b.store;

