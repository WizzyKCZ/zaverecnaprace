-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `firma`
--

DROP TABLE IF EXISTS `firma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `firma` (
  `idfirma` int(11) NOT NULL,
  `jmeno` varchar(45) NOT NULL,
  `sidlo` varchar(45) NOT NULL,
  `pocet_zamestnancu` int(11) DEFAULT NULL,
  PRIMARY KEY (`idfirma`),
  UNIQUE KEY `idfirma_UNIQUE` (`idfirma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `firma`
--

LOCK TABLES `firma` WRITE;
/*!40000 ALTER TABLE `firma` DISABLE KEYS */;
INSERT INTO `firma` VALUES (1,'CD PROJECT RED','Poland',400),(2,'Ubisoft','France',1000),(3,'Electronic Arts','United States',1200),(4,'Activision','United States',800),(5,'Bethesda Softworks','United States',1500);
/*!40000 ALTER TABLE `firma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hra`
--

DROP TABLE IF EXISTS `hra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hra` (
  `idhra` int(11) NOT NULL,
  `nazev` varchar(45) NOT NULL,
  `jazyky` enum('Anglictina','Nemcina','Polstina','Cestina') NOT NULL,
  `zanr` varchar(45) NOT NULL,
  `rating` enum('E','7','12','15','18') NOT NULL,
  `popis` text NOT NULL,
  `idvydavatel` int(11) NOT NULL,
  `idvyvojar` int(11) NOT NULL,
  PRIMARY KEY (`idhra`),
  UNIQUE KEY `idhra_UNIQUE` (`idhra`),
  KEY `fk_hra_firma1_idx` (`idvydavatel`),
  KEY `fk_hra_firma2_idx` (`idvyvojar`),
  CONSTRAINT `fk_hra_firma1` FOREIGN KEY (`idvydavatel`) REFERENCES `firma` (`idfirma`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_hra_firma2` FOREIGN KEY (`idvyvojar`) REFERENCES `firma` (`idfirma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hra`
--

LOCK TABLES `hra` WRITE;
/*!40000 ALTER TABLE `hra` DISABLE KEYS */;
INSERT INTO `hra` VALUES (1,'Zaklinac 3','Cestina','RPG','18','Zaklínač 3: Divoký hon (anglicky The Witcher 3: Wild Hunt, polsky Wiedźmin 3: Dziki Gon) je RPG videohra s otevřeným světem, uzavření videoherní trilogie ze ságy o Zaklínači.',1,1),(2,'Fallout 76','Anglictina','RPG','18','Spolupracuj s ostatními a přežijte - nebo taky ne. Pod hrozbou naprosté nukleární destrukce zažiješ největší a nejdynamičtější svět, který se v universu Fallout kdy objevil.',5,5),(3,'Assassin\'s Creed Odyssey','Anglictina','RPG','15','Assassin\'s Creed Odyssey je historická akční adventura vydaná Ubisoftem, jedná se o jedenáctou hlavní hru série Assassin\'s Creed. Tento díl vyšel 5. října 2018 pro platformy Microsoft Windows, Playstation 4 a Xbox One. Děj se odehrává v období antiky v Řecku Při peloponéských válkách.',2,2),(4,'FIFA 20','Cestina','Sport','E','FIFA 20 je fotbalová videohra, 27. díl každoročně vydávané série FIFA, vyvinutá studiem Electronic Arts. Vydána byla 27. září 2019 pro platformy Microsoft Windows, Xbox One, PlayStation 4 a Nintendo Switch.[1] Demo bylo vydáno 10. září 2019 pro Microsoft Windows, Xbox One a PlayStation 4.[2] 19. září 2019 byla vydána plná hra pro uživatele EA Access a 24. září 2019 byly vydány Champions a Ultimate edice.',3,3),(5,'Call of Duty: Modern Warfare','Anglictina','FPS','18','Call of Duty: Modern Warfare je akční FPS střílečka a šestnáctý díl série Call of Duty. Hra byla vývojáři oznámena 30. května 2019 a poté vyšla 25. října 2019.',4,4);
/*!40000 ALTER TABLE `hra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platforma`
--

DROP TABLE IF EXISTS `platforma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `platforma` (
  `idplatforma` int(11) NOT NULL,
  `nazev` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idplatforma`),
  UNIQUE KEY `idplatforma_UNIQUE` (`idplatforma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platforma`
--

LOCK TABLES `platforma` WRITE;
/*!40000 ALTER TABLE `platforma` DISABLE KEYS */;
INSERT INTO `platforma` VALUES (1,'Playstation'),(2,'Xbox'),(3,'PC'),(4,'Nintendo');
/*!40000 ALTER TABLE `platforma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recenze`
--

DROP TABLE IF EXISTS `recenze`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recenze` (
  `idrecenze` int(11) NOT NULL,
  `role` enum('Uzivatel','Redakce') NOT NULL,
  `prezdivka` varchar(25) NOT NULL,
  `idrecenzenti` int(11) NOT NULL,
  `idhra` int(11) NOT NULL,
  PRIMARY KEY (`idrecenze`),
  UNIQUE KEY `idrecenze_UNIQUE` (`idrecenze`),
  KEY `fk_recenze_recenzenti_idx` (`idrecenzenti`),
  KEY `fk_recenze_hra1_idx` (`idhra`),
  CONSTRAINT `fk_recenze_hra1` FOREIGN KEY (`idhra`) REFERENCES `hra` (`idhra`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_recenze_recenzenti` FOREIGN KEY (`idrecenzenti`) REFERENCES `recenzenti` (`idrecenzenti`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recenze`
--

LOCK TABLES `recenze` WRITE;
/*!40000 ALTER TABLE `recenze` DISABLE KEYS */;
INSERT INTO `recenze` VALUES (1,'Uzivatel','Opice',5,1),(2,'Redakce','Forkos',3,4),(3,'Uzivatel','Jajks',4,3),(4,'Uzivatel','Mikes',1,2),(5,'Redakce','Houks',5,5);
/*!40000 ALTER TABLE `recenze` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recenzenti`
--

DROP TABLE IF EXISTS `recenzenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recenzenti` (
  `idrecenzenti` int(11) NOT NULL,
  `pocetHvezd` enum('1','2','3','4','5') NOT NULL,
  `popisRecenze` text DEFAULT NULL,
  PRIMARY KEY (`idrecenzenti`),
  UNIQUE KEY `idrecenzenti_UNIQUE` (`idrecenzenti`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recenzenti`
--

LOCK TABLES `recenzenti` WRITE;
/*!40000 ALTER TABLE `recenzenti` DISABLE KEYS */;
INSERT INTO `recenzenti` VALUES (1,'5','Nejlepsi hra'),(2,'4','Dobre hej'),(3,'3','Take meh'),(4,'2','No nic moc'),(5,'1','BUUUU');
/*!40000 ALTER TABLE `recenzenti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vydani`
--

DROP TABLE IF EXISTS `vydani`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vydani` (
  `datum` date NOT NULL,
  `idhra` int(11) NOT NULL,
  `idplatforma` int(11) NOT NULL,
  KEY `fk_vydani_hra1_idx` (`idhra`),
  KEY `fk_vydani_platforma1_idx` (`idplatforma`),
  CONSTRAINT `fk_vydani_hra1` FOREIGN KEY (`idhra`) REFERENCES `hra` (`idhra`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_vydani_platforma1` FOREIGN KEY (`idplatforma`) REFERENCES `platforma` (`idplatforma`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vydani`
--

LOCK TABLES `vydani` WRITE;
/*!40000 ALTER TABLE `vydani` DISABLE KEYS */;
INSERT INTO `vydani` VALUES ('2015-05-15',1,3),('2019-10-25',5,1),('2018-10-23',2,2),('2018-10-02',3,3),('2019-09-24',4,4);
/*!40000 ALTER TABLE `vydani` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'mydb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-30 18:23:17
