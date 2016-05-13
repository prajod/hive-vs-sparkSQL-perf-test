
-- df category_list: word=/usr/text_files/category_list.txt

CREATE TABLE categories (
category_id INTEGER NOT NULL SERIAL PRIMARY KEY, --category_id int,
category_department_id INTEGER NOT NULL,-- category_department_id int,
category_name TEXT UNIQUE NOT NULL, -- df: use=category_list 
) ;

CREATE TABLE products ( --df: mult=2.0
product_id SERIAL PRIMARY KEY, -- product_id int,
product_category_id INTEGER NOT NULL REFERENCES categories, -- product_category_id int,
product_name TEXT UNIQUE NOT NULL, -- product_name string,
product_description TEXT UNIQUE NOT NULL, -- product_description string,
product_price INTEGER NOT NULL, -- product_price float,
product_image TEXT UNIQUE NOT NULL --product_image string
) ;

CREATE TABLE order_items ( --df: mult=100000
order_item_id SERIAL PRIMARY KEY, 
order_item_order_id INTEGER NOT NULL, -- df: int sub=uniform offset=1 size=10 
order_item_product_id INTEGER NOT NULL REFERENCES products, 
order_item_quantity INTEGER NOT NULL, -- df: int sub=uniform offset=1 size=5 
order_item_subtotal INTEGER NOT NULL, -- df: int sub=uniform offset=1 size=9
order_item_product_price INTEGER NOT NULL, -- df: int sub=uniform offset=1 size=9 
);



