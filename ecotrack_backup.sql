/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.18-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: EcoTrack
-- ------------------------------------------------------
-- Server version	10.11.18-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Contributions`
--

DROP TABLE IF EXISTS `Contributions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contributions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(100) DEFAULT NULL,
  `units` int(11) DEFAULT NULL,
  `associated_house` varchar(50) DEFAULT NULL,
  `collection_date` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `associated_house` (`associated_house`),
  CONSTRAINT `Contributions_ibfk_1` FOREIGN KEY (`associated_house`) REFERENCES `Houses` (`house_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contributions`
--

LOCK TABLES `Contributions` WRITE;
/*!40000 ALTER TABLE `Contributions` DISABLE KEYS */;
INSERT INTO `Contributions` VALUES
(1,'jon',1,'Red','2026-07-28 15:29:59'),
(2,'kayla',1,'Red','2026-07-28 15:31:56');
/*!40000 ALTER TABLE `Contributions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Houses`
--

DROP TABLE IF EXISTS `Houses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Houses` (
  `house_name` varchar(50) NOT NULL,
  `total_points` int(11) DEFAULT 0,
  PRIMARY KEY (`house_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Houses`
--

LOCK TABLES `Houses` WRITE;
/*!40000 ALTER TABLE `Houses` DISABLE KEYS */;
INSERT INTO `Houses` VALUES
('Blue',0),
('Green',0),
('Red',2),
('Yellow',0);
/*!40000 ALTER TABLE `Houses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `student_id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `grade` varchar(10) DEFAULT NULL,
  `section` varchar(10) DEFAULT NULL,
  `house` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES
('1','jonathan','12','a','Red'),
('10','mike','3','a','Green'),
('11','rohan','3','a','Yellow'),
('12','kay','7','b','Blue'),
('13','jamie','5','c','Blue'),
('14','jon','4','a','Blue'),
('2','joston','10','a','Red'),
('3','jenoshka','4','c','Red'),
('4','jon','11','b','Blue'),
('5','kayla','3','c','Green'),
('6','maroon','4','a','Yellow'),
('7','leo','6','b','Green'),
('9','jake','2','a','Blue');
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WasteLog`
--

DROP TABLE IF EXISTS `WasteLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `WasteLog` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(50) DEFAULT NULL,
  `waste_type` varchar(50) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `points_earned` int(11) DEFAULT NULL,
  `collection_date` date DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `fk_student` (`student_id`),
  CONSTRAINT `fk_student` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WasteLog`
--

LOCK TABLES `WasteLog` WRITE;
/*!40000 ALTER TABLE `WasteLog` DISABLE KEYS */;
INSERT INTO `WasteLog` VALUES
(3,'1','Glass',20,30,'2026-07-28'),
(4,'2','Plastic',30,40,'2026-07-28'),
(5,'3','Organic',40,50,'2026-07-28'),
(6,'4','Plastic',20,25,'2026-07-28'),
(7,'5','Metal',60,100,'2026-07-28'),
(8,'6','Plastic',45,50,'2026-07-28');
/*!40000 ALTER TABLE `WasteLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-28 16:32:26
