DB_USER = "root"
DB_PASSWORD = "shreyas"
DB_HOST = "127.0.0.1"
DB_NAME = "ecommerce"
DB_SERVER_NAME="redberyl"

QUERY_INSERT_Customer  = "INSERT INTO Customer (cid, cname, c_email, c_number) VALUES (%s, %s, %s,%s)"
QUERY_UPDATE_Customer ="UPDATE customer SET c_number = %s,cname= %s,c_email=%s WHERE cid = %s"


DELETE_QUERY = "DELETE FROM customer WHERE cid = %s"
QUERY_SELECT_ALL_Customer = "Select * from Customer"



QUERY_INSERT_Status  = "INSERT INTO Status (status_id, status_name,odid) VALUES (%s, %s,%s)"
QUERY_UPDATE_Status ="UPDATE status SET status_name = %s WHERE status_id= %s"


DELETE_Status = "DELETE FROM status WHERE status_id = %s"
QUERY_SELECT_ALL_Status = "Select * from Status"



QUERY_INSERT_Address  = "INSERT INTO Address (aid,cid,city,country,state,street,zipcode) VALUES (%s, %s,%s,%s,%s,%s,%s)"
QUERY_UPDATE_Address ="UPDATE address SET city = %s  WHERE aid= %s"


DELETE_Address = "DELETE FROM address WHERE aid = %s"
QUERY_SELECT_ALL_Address = "Select * from Address"

QUERY_INSERT_Orders  = "INSERT INTO Orders (oid,cid,orderdate,payid) VALUES (%s, %s,%s,%s)"
QUERY_UPDATE_Orders ="UPDATE orders SET orderDate = %s  WHERE oid= %s"


DELETE_Orders = "DELETE FROM orders WHERE oid = %s"
QUERY_SELECT_ALL_Orders = "Select * from Orders"


QUERY_INSERT_Payment  = "Insert into payments(payid,pdate,amount,paymethod,oid) values(%s,%s,%s,%s,%s);"
QUERY_UPDATE_Payment ="UPDATE payments SET  amount= %s,pdate = %s,paymethod = %s  WHERE payid= %s"


DELETE_Payment = "DELETE FROM payments WHERE payid = %s"
QUERY_SELECT_ALL_Payment = "Select * from payments"





QUERY_INSERT_Product  = "INSERT INTO product (p_name,  p_available_stock, p_sell_stock, p_price_per_item, p_is_available, p_category_id,inv_id) Values( %s,%s,%s,%s,%s,%s,%s )";

QUERY_UPDATE_Product ="UPDATE product SET p_price_per_item = %s,p_available_stock= %s WHERE p_id = %s"


DELETE_Product= "DELETE FROM product WHERE p_id = %s"
QUERY_SELECT_ALL_Product = "Select * from product"


AUTO_INCR_PRODUCT="alter table product AUTO_INCREMENT = 1"



TABEL_NAME="product"




DUPLICATE_CHECK="SELECT COUNT(*) FROM customer WHERE c_number = %s"




QUERY_INSERT_OrderDetails  = "INSERT INTO OrderDetails (odid,oid,payid,pid,quantity) VALUES (%s, %s,%s,%s,%s)"
QUERY_UPDATE_OrderDetails ="UPDATE OrderDetails SET quantity = %s  WHERE odid= %s"


DELETE_OrderDetails = "DELETE FROM OrderDetails WHERE odid = %s"
QUERY_SELECT_ALL_OrderDetails = "Select * from OrderDetails"



# Cutomer wise product purchase


# Customer_wise_product_purchases="Select cust.cname,p.p_name ,s.status_name,ordd.odid from customer cust inner join orders o on o.cid=cust.cid \
#                                 inner join orderdetails ordd on ordd.oid=o.oid \
#                                 inner join product p on p.p_id=ordd.pid \
#                                 inner join status s on s.odid=ordd.odid where s.status_name='delivered'"






Customer_wise_product_purchases="SELECT cust.cname, p.p_name,  COUNT(*) as purchase_count \
                                 FROM customer cust \
                                 INNER JOIN orders o ON o.cid = cust.cid \
                                 INNER JOIN orderdetails ordd ON ordd.oid = o.oid \
                                 INNER JOIN product p ON p.p_id = ordd.pid \
                                 INNER JOIN status s ON s.odid = ordd.odid \
                                 WHERE s.status_name = 'delivered' \
                                 GROUP BY cust.cname, p.p_name;"


# DaywiseOrderplaced Query

# Daywise_total_orders_placed = "SELECT COUNT(o.oid) AS placed_orders_count, o.orderDate \
#                               FROM status st \
#                               INNER JOIN orderdetails odd ON st.odid = odd.odid \
#                               INNER JOIN orders o ON odd.oid = o.oid \
#                               WHERE st.status_name = 'placed' \
#                               GROUP BY o.orderDate ;  "


Daywise_total_orders_placed = "SELECT \
                              COUNT(o.oid) AS placed_orders_count, \
                              o.orderDate, \
                              SUM(odd.quantity) AS total_quantity \
                              FROM \
                              status st \
                              INNER JOIN \
                              orderdetails odd ON st.odid = odd.odid \
                              INNER JOIN \
                             orders o ON odd.oid = o.oid \
                             WHERE \
                             st.status_name = 'placed' \
                             GROUP BY \
                             o.orderDate;"




# Daywise total orders cancelled

# Daywise_total_orders_cancelled = "SELECT COUNT(o.oid) AS placed_orders_count, o.orderDate \
#                               FROM status st \
#                               INNER JOIN orderdetails odd ON st.odid = odd.odid \
#                               INNER JOIN orders o ON odd.oid = o.oid \
#                               WHERE st.status_name = 'Cancelled' \
#                               GROUP BY o.orderDate ;  "






Daywise_total_orders_cancelled = "SELECT \
                              COUNT(o.oid) AS placed_orders_count, \
                              o.orderDate, \
                              SUM(odd.quantity) AS total_quantity \
                              FROM \
                              status st \
                              INNER JOIN \
                              orderdetails odd ON st.odid = odd.odid \
                              INNER JOIN \
                             orders o ON odd.oid = o.oid \
                             WHERE \
                             st.status_name = 'Cancelled' \
                             GROUP BY \
                             o.orderDate;"

#TOP 5 selling product

TOP_FIVE_SELLING_PRODUCT = "SELECT DISTINCT \
                            p.p_id, \
                            p.p_name \
                            FROM \
                            product p \
                            JOIN \
                            orderdetails od ON p.p_id = od.pid \
                            JOIN \
                            status s ON od.odid = s.odid \
                            WHERE \
                            s.status_name = 'Delivered' \
                            ORDER BY \
                            p.p_id, p.p_name \
                            LIMIT 5;"











Customer_wise_orders=" SELECT cust.cname , st.status_name,pd.p_name,year(ord.orderDate) \
                        FROM customer cust \
                        INNER JOIN orders ord ON ord.cid = cust.cid  \
                        INNER JOIN orderdetails  ordd ON ordd.oid = ord.oid \
                        Inner join status st On ordd.odid=st.odid \
                        Inner join product pd on pd.p_id=ordd.pid \
                        INNER JOIN product pr ON ordd.pid = pr.p_id where year(ord.orderDate)=2022;"









QUERY_INSERT_Inventory  = "INSERT INTO Inventory (product_quantity,created_at,modified_at,deleted_at,inv_id,pid) VALUES (%s, %s,%s,%s,%s,%s)"
QUERY_UPDATE_Inventory ="UPDATE Inventory SET product_quantity = %s WHERE inv_id = %s"


DELETE_Inventory = "DELETE FROM Inventory WHERE inv_id = %s"
QUERY_SELECT_ALL_Inventory = "Select * from Inventory"
