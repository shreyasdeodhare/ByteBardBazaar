-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `aid` int NOT NULL,
  `cid` int DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `zipcode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  KEY `cid` (`cid`),
  CONSTRAINT `address_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `customer` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,1,'New York','USA','NY','123 Main St','10001'),(2,2,'Los Angeles','USA','CA','456 Oak St','90001'),(3,3,'Chicago','USA','IL','789 Pine St','60601'),(4,4,'Houston','USA','TX','101 Elm St','77001'),(5,5,'Phoenix','USA','AZ','202 Maple St','85001'),(6,6,'Philadelphia','USA','PA','303 Cedar St','19101'),(7,7,'San Antonio','USA','TX','404 Birch St','78201'),(8,8,'San Diego','USA','CA','505 Spruce St','92101'),(9,9,'Dallas','USA','TX','606 Pine St','75201'),(10,10,'San Jose','USA','CA','707 Oak St','95101');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `category_name` varchar(100) DEFAULT NULL,
  `categoryid` int NOT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('Electronics',1),('Clothing',2),('Books',3),('Home and Garden',4),('Toys and Games',5),('Health and Beauty',6),('Sports and Outdoors',7),('Automotive',8),('Jewelry',9),('Movies and Music',10),('Computers',11),('Appliances',12),('Furniture',13),('Food and Grocery',14),('Pet Supplies',15);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cid` int NOT NULL,
  `cname` varchar(250) NOT NULL,
  `c_email` varchar(100) DEFAULT NULL,
  `c_number` bigint DEFAULT NULL,
  PRIMARY KEY (`cid`),
  UNIQUE KEY `c_number` (`c_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'John Doe','john.doe@email.com',1234567890),(2,'Alice Smith','alice.smith@email.com',9876543210),(3,'Bob Johnson','bob.johnson@email.com',5551112222),(4,'Eva Davis','eva.davis@email.com',3334445555),(5,'Michael Wilson','michael.wilson@email.com',6667778888),(6,'Sophia Brown','sophia.brown@email.com',1112223333),(7,'Daniel Taylor','daniel.taylor@email.com',9990001111),(8,'Olivia Martin','olivia.martin@email.com',4445556666),(9,'James Anderson','james.anderson@email.com',2223334444),(10,'Emily Garcia','emily.garcia@email.com',7778889999),(11,'William White','william.white@email.com',8889990000),(12,'Ava Jones','ava.jones@email.com',1212121212),(13,'Benjamin Moore','benjamin.moore@email.com',3434343434),(14,'Mia Davis','mia.davis@email.com',5656565656),(15,'Ethan Martinez','ethan.martinez@email.com',7878787878),(16,'Emma Brown','emma.brown@email.com',9898989898),(17,'Alexander Wilson','alexander.wilson@email.com',2222222222),(18,'Abigail Taylor','abigail.taylor@email.com',4444444444),(19,'Daniel Thomas','daniel.thomas@email.com',6666666666),(20,'Sophia Robinson','sophia.robinson@email.com',8888888888);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderdetails`
--

DROP TABLE IF EXISTS `orderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderdetails` (
  `odid` int NOT NULL AUTO_INCREMENT,
  `oid` int DEFAULT NULL,
  `payid` int DEFAULT NULL,
  `pid` int DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`odid`),
  KEY `oid` (`oid`),
  KEY `payid` (`payid`),
  KEY `pid` (`pid`),
  CONSTRAINT `orderdetails_ibfk_1` FOREIGN KEY (`oid`) REFERENCES `orders` (`oid`),
  CONSTRAINT `orderdetails_ibfk_10` FOREIGN KEY (`pid`) REFERENCES `product` (`p_id`) ON DELETE CASCADE,
  CONSTRAINT `orderdetails_ibfk_2` FOREIGN KEY (`pid`) REFERENCES `product` (`p_id`),
  CONSTRAINT `orderdetails_ibfk_3` FOREIGN KEY (`payid`) REFERENCES `payments` (`payid`),
  CONSTRAINT `orderdetails_ibfk_4` FOREIGN KEY (`oid`) REFERENCES `orders` (`oid`) ON DELETE CASCADE,
  CONSTRAINT `orderdetails_ibfk_5` FOREIGN KEY (`payid`) REFERENCES `payments` (`payid`) ON UPDATE CASCADE,
  CONSTRAINT `orderdetails_ibfk_6` FOREIGN KEY (`payid`) REFERENCES `payments` (`payid`) ON DELETE CASCADE,
  CONSTRAINT `orderdetails_ibfk_7` FOREIGN KEY (`pid`) REFERENCES `product` (`p_id`) ON UPDATE CASCADE,
  CONSTRAINT `orderdetails_ibfk_8` FOREIGN KEY (`pid`) REFERENCES `product` (`p_id`) ON DELETE CASCADE,
  CONSTRAINT `orderdetails_ibfk_9` FOREIGN KEY (`pid`) REFERENCES `product` (`p_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderdetails`
--

LOCK TABLES `orderdetails` WRITE;
/*!40000 ALTER TABLE `orderdetails` DISABLE KEYS */;
INSERT INTO `orderdetails` VALUES (1,2,1,1,'2'),(2,4,2,4,'5'),(3,5,3,5,'1'),(4,6,1,6,'3'),(5,2,2,7,'2'),(6,4,3,8,'4'),(7,5,1,9,'1'),(8,6,2,10,'2'),(9,2,3,11,'3'),(10,4,3,12,'1'),(11,7,4,13,'2'),(12,8,5,14,'3'),(13,9,6,15,'1'),(14,10,7,16,'2'),(15,11,8,17,'4'),(16,12,9,18,'1'),(17,13,10,19,'2'),(18,14,11,20,'3'),(19,15,12,21,'1'),(20,16,13,22,'2');
/*!40000 ALTER TABLE `orderdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `oid` int NOT NULL,
  `cid` int DEFAULT NULL,
  `orderDate` date DEFAULT NULL,
  `payid` int DEFAULT NULL,
  PRIMARY KEY (`oid`),
  KEY `cid` (`cid`),
  KEY `payid` (`payid`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `customer` (`cid`) ON UPDATE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `customer` (`cid`) ON DELETE CASCADE,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`payid`) REFERENCES `payments` (`payid`) ON UPDATE CASCADE,
  CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`payid`) REFERENCES `payments` (`payid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,'2024-01-01',1),(2,2,'2024-01-02',2),(3,3,'2024-01-03',3),(4,4,'2024-01-04',4),(5,5,'2024-01-05',5),(6,6,'2024-01-06',6),(7,7,'2024-01-07',7),(8,8,'2024-01-08',8),(9,9,'2024-01-09',9),(10,10,'2024-01-10',10),(11,11,'2024-01-11',11),(12,12,'2024-01-12',12),(13,13,'2024-01-13',13),(14,14,'2024-01-14',14),(15,15,'2024-01-15',15),(16,16,'2024-01-16',16),(17,17,'2024-01-17',17),(18,18,'2024-01-18',18),(19,19,'2024-01-19',19),(20,20,'2024-01-20',20);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payid` int NOT NULL,
  `pdate` date DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `paymethod` varchar(250) DEFAULT NULL,
  `oid` int DEFAULT NULL,
  PRIMARY KEY (`payid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,'2024-01-01',50,'Credit Card - Visa',1),(2,'2024-01-02',30.5,'PayPal',2),(3,'2024-01-03',25,'Debit Card - MasterCard',3),(4,'2024-01-04',40.75,'Cash on Delivery',4),(5,'2024-01-05',60.2,'Bank Transfer',5),(6,'2024-01-06',75.5,'Credit Card - American Express',6),(7,'2024-01-07',20,'PayPal',7),(8,'2024-01-08',45.3,'Debit Card - Visa Electron',8),(9,'2024-01-09',35,'Cash on Delivery',9),(10,'2024-01-10',55.8,'Bank Transfer',10),(11,'2024-01-11',70.25,'Credit Card - MasterCard',11),(12,'2024-01-12',22.5,'PayPal',12),(13,'2024-01-13',33.75,'Debit Card - Maestro',13),(14,'2024-01-14',47.9,'Cash on Delivery',14),(15,'2024-01-15',65.4,'Bank Transfer',15),(16,'2024-01-16',18.2,'Credit Card - Visa',16),(17,'2024-01-17',29.3,'PayPal',17),(18,'2024-01-18',39.8,'Debit Card - MasterCard',18),(19,'2024-01-19',50,'Cash on Delivery',19),(20,'2024-01-20',55.6,'Bank Transfer',20),(21,'2024-01-21',67.9,'Credit Card - American Express',21),(22,'2024-01-22',23.4,'PayPal',22),(23,'2024-01-23',31.75,'Debit Card - Visa Electron',23),(24,'2024-01-24',43.2,'Cash on Delivery',24),(25,'2024-01-25',58.5,'Bank Transfer',25),(26,'2024-01-26',19.8,'Credit Card - MasterCard',26),(27,'2024-01-27',27.3,'PayPal',27),(28,'2024-01-28',37.5,'Debit Card - Maestro',28),(29,'2024-01-29',49.6,'Cash on Delivery',29),(30,'2024-01-30',60,'Bank Transfer',30);
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `p_id` int NOT NULL AUTO_INCREMENT,
  `p_name` varchar(100) DEFAULT NULL,
  `p_available_stock` int DEFAULT NULL,
  `p_sell_stock` int DEFAULT NULL,
  `p_price_per_item` int DEFAULT NULL,
  `p_category_id` int DEFAULT NULL,
  `p_is_available` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `fk_product_category` (`p_category_id`),
  CONSTRAINT `fk_product_category` FOREIGN KEY (`p_category_id`) REFERENCES `category` (`categoryid`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Blue Shirt',50,10,20,1,1),(2,'Black Jeans',30,5,15,1,1),(3,'White Sneakers',40,8,18,1,1),(4,'Red Dress',45,9,25,1,1),(5,'Gray Sweater',55,11,30,1,1),(6,'Laptop',60,12,1000,2,1),(7,'Smartphone',35,6,800,2,1),(8,'Tablet',25,5,600,2,1),(9,'Headphones',40,8,150,2,1),(10,'Camera',30,7,1200,2,1),(11,'Coffee Maker',20,4,50,3,1),(12,'Blender',15,3,40,3,1),(13,'Toaster',25,5,30,3,1),(14,'Microwave',10,2,120,3,1),(15,'Electric Kettle',18,4,35,3,1),(16,'Blue Shirt',50,10,20,1,1),(17,'Black Jeans',30,5,15,1,1),(18,'White Sneakers',40,8,18,1,1),(19,'Red Dress',45,9,25,1,1),(20,'Gray Sweater',55,11,30,1,1),(21,'Blue Shirt',50,10,20,1,1),(22,'Black Jeans',30,5,15,1,1),(23,'White Sneakers',40,8,18,1,1),(24,'Red Dress',45,9,25,1,1),(25,'Gray Sweater',55,11,30,1,1),(26,'Laptop',60,12,1000,2,1),(27,'Smartphone',35,6,800,2,1),(28,'Tablet',25,5,600,2,1),(29,'Headphones',40,8,150,2,1),(30,'Camera',30,7,1200,2,1),(31,'Laptop',60,12,1000,2,1),(32,'Smartphone',35,6,800,2,1),(33,'Tablet',25,5,600,2,1),(34,'Headphones',40,8,150,2,1),(35,'Camera',30,7,1200,2,1),(36,'Coffee Maker',20,4,50,3,1),(37,'Blender',15,3,40,3,1),(38,'Toaster',25,5,30,3,1),(39,'Microwave',10,2,120,3,1),(40,'Electric Kettle',18,4,35,3,1),(41,'Coffee Maker',20,4,50,3,1),(42,'Blender',15,3,40,3,1),(43,'Toaster',25,5,30,3,1),(44,'Microwave',10,2,120,3,1),(45,'Electric Kettle',18,4,35,3,1);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `status_id` int NOT NULL AUTO_INCREMENT,
  `status_name` varchar(500) DEFAULT NULL,
  `odid` int DEFAULT NULL,
  PRIMARY KEY (`status_id`),
  KEY `odid` (`odid`),
  CONSTRAINT `status_ibfk_1` FOREIGN KEY (`odid`) REFERENCES `orderdetails` (`odid`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (39,'Order Accepted',1),(40,'Order Packed',2),(41,'Out for Delivery',6),(42,'Delivered',7),(43,'Cancelled',8),(44,'Returned',9),(45,'On Hold',10),(46,'Order Accepted',11),(47,'Order Packed',12),(48,'Out for Delivery',13),(49,'Delivered',14),(50,'Cancelled',15),(51,'Returned',16),(52,'On Hold',17),(53,'Order Accepted',18),(54,'Order Packed',19),(55,'Out for Delivery',20),(56,'Delivered',14),(57,'Cancelled',12);
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-08 10:02:53
