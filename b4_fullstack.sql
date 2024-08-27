-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: b4_fullstack
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `bookingid` int NOT NULL AUTO_INCREMENT,
  `campID` int DEFAULT NULL,
  `userEmail` varchar(255) DEFAULT NULL,
  `paymentID` varchar(255) DEFAULT NULL,
  `person` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `bookingDate` date DEFAULT NULL,
  PRIMARY KEY (`bookingid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (1,4,'raj@gmail.com','pay_Oh6tatX6Oxadhh',2,4000,'2024-08-05'),(2,4,'raj@gmail.com','pay_Oh7Cdkc6LBTHJE',3,6000,'2024-08-05'),(3,4,'raj@gmail.com','pay_OhV8J4SVPEuMHk',3,6000,'2024-08-06'),(4,7,'raj@gmail.com','pay_OhVP3CntCg4oGj',3,1500,'2024-08-06'),(5,8,'abd@gmail.com','pay_Oj4ScyYK2rhkuv',4,1200,'2024-08-10'),(6,4,'abd@gmail.com','pay_Oj4TnOXVswzo5r',3,6000,'2024-08-10'),(7,7,'abd@gmail.com','pay_Oj4ffetV6SJsSY',4,2000,'2024-08-10'),(8,10,'yash@gmail.com','pay_Oj5IiNq7lpOQaZ',3,1200,'2024-08-10'),(9,10,'yash@gmail.com','pay_Oj5KySDR9IXqPT',4,1600,'2024-08-10');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `camp`
--

DROP TABLE IF EXISTS `camp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `camp` (
  `campID` int NOT NULL AUTO_INCREMENT,
  `orgEmail` varchar(255) DEFAULT NULL,
  `campName` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `descp` longtext,
  `charges` int DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`campID`),
  KEY `campdelete_idx` (`orgEmail`),
  CONSTRAINT `campdelete` FOREIGN KEY (`orgEmail`) REFERENCES `organiser` (`email`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camp`
--

LOCK TABLES `camp` WRITE;
/*!40000 ALTER TABLE `camp` DISABLE KEYS */;
INSERT INTO `camp` VALUES (1,'rahul@gmail.com','Adventure Camp',NULL,'Ranchi','Tagore hill','2024-07-10','2024-07-13','1.collect participant information\r\n2.obtain medical health',2500,'1223122313'),(4,'youthcamp@gmail.com','Youth Camp',NULL,'Ranchi','Patratu','2024-07-13','2024-07-17','1.collect participant information 2.obtain medical health',2000,'2334233445'),(6,'asd@gmail.com','adfgf',NULL,'Rishikesh','Tagore hill','2024-07-17','2024-07-26','asdsadsad',200,'dftcr'),(7,'chetas@gmail.com','dj camp',NULL,'Rishikesh','rishikesh','2024-08-08','2024-08-15','fdtgdfdjfhtd',500,'chetas'),(8,'abd@gmail.com','rj camp',NULL,'Jodhpur','faridabad','2024-08-13','2024-08-22','rtdxtrfc',300,'arun'),(9,'abd@gmail.com','jaipur explore',NULL,'Jodhpur','sujata','2024-08-14','2024-08-22','errtt',400,'tarun'),(10,'yash@gmail.com','jaipur explore',NULL,'Jodhpur','sujata','2024-08-13','2024-08-22','fggyhy',400,'tarun'),(11,'yash@gmail.com','abcd','Jharkhand',' Ranchi ','Patratu','2024-08-20','2024-08-25','maza aa gaya',200,'gopu'),(12,'akshay@gmail.com','fun camp','Chhattisgarh',' Korba ','transport nagar','2024-08-23','2024-08-27','tdxtehx',400,'akshay'),(13,'neymar@gmail.com','sujata camp','Jharkhand',' Ranchi ','sujata','2024-08-28','2024-08-31','dstrtd',200,'neymar');
/*!40000 ALTER TABLE `camp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `camp_photo`
--

DROP TABLE IF EXISTS `camp_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `camp_photo` (
  `campPhotoid` int NOT NULL AUTO_INCREMENT,
  `campID` int DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`campPhotoid`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camp_photo`
--

LOCK TABLES `camp_photo` WRITE;
/*!40000 ALTER TABLE `camp_photo` DISABLE KEYS */;
INSERT INTO `camp_photo` VALUES (1,4,'1721370045.jpg'),(2,4,'1721788662.jpeg'),(3,4,'1721788746.png'),(4,4,'1721788983.jpg'),(5,7,'1722923487.jpg'),(6,7,'1722923492.'),(7,8,'1723265303.jpg'),(8,8,'1723265312.'),(9,9,'1723267322.jpg'),(15,11,'1723790828.jpeg'),(16,10,'1724219900.jpg'),(17,12,'1724220204.jpg'),(18,12,'1724220212.jpeg'),(19,12,'1724731263.jpg'),(20,13,'1724736528.jpeg'),(21,13,'1724736535.jpg');
/*!40000 ALTER TABLE `camp_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organiser`
--

DROP TABLE IF EXISTS `organiser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organiser` (
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `address` text,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organiser`
--

LOCK TABLES `organiser` WRITE;
/*!40000 ALTER TABLE `organiser` DISABLE KEYS */;
INSERT INTO `organiser` VALUES ('abd','abd@gmail.com','2324232423','sujata','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('akshay','akshay@gmail.com','4545454545','main road,sujata','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('asddf','asd@gmail.com','2323343445','main road, firyalal, ranchi (jharkhand)','cbfad02f9ed2a8d1e08d8f74f5303e9eb93637d47f82ab6f1c15871cf8dd0481'),('dj chetas','chetas@gmail.com','4556576756','manipur','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('monu','monu@gmail.com','5645455667','sujata','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('neymar','neymar@gmail.com','2222222222','main road,sujata','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('rahul&sons','rahul@gmail.com','1212121213','main road,sujata,near sbi bank','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('yash','yash@gmail.com','4545454545','main road,sujata','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('Youth Camp','youthcamp@gmail.com','6234534234','main road, firyalal, ranchi (jharkhand)','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c');
/*!40000 ALTER TABLE `organiser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `reviewID` int NOT NULL AUTO_INCREMENT,
  `userEmail` varchar(265) DEFAULT NULL,
  `campID` int DEFAULT NULL,
  `comment` mediumtext,
  `star` int DEFAULT NULL,
  PRIMARY KEY (`reviewID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('abd','abd@gmail.com','2324232423','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('akshay','akshay@gmail.com','4545454545','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('dj','dj@gmail.com','4546453435','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('jack','jack@gmail.com','3445344546','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),('imran khan','khan@gmail.com','9468734596','0988'),('king','king@gmail.com','3333333333','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('laksh','laksh@gmail.com','04565676787','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),('manan','manan@gmail.com','4546565767','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('neymar','neymar@gmail.com','2222222222','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('parinav','parinav@gmail.com','6202246261','1234'),('raj','raj@gmail.com','2334453434','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c'),('rajeev singh','rajeev1@gmail.com','6457839467','3456'),('vikash sinha','sinha@gmail.com','6767564534','5678'),('yash','yash@gmail.com','4545454545','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-27 11:15:58
