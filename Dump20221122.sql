CREATE DATABASE  IF NOT EXISTS `splatoon3hub` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `splatoon3hub`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: splatoon3hub
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `loadout`
--

DROP TABLE IF EXISTS `loadout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loadout` (
  `user_id` int NOT NULL,
  `team_id` int NOT NULL,
  `weapon_id` int NOT NULL,
  PRIMARY KEY (`team_id`,`user_id`,`weapon_id`),
  KEY `fk_user_has_team_team1_idx` (`team_id`),
  KEY `fk_user_has_team_user_idx` (`user_id`),
  KEY `fk_user_has_team_weapon1_idx` (`weapon_id`),
  CONSTRAINT `fk_user_has_team_team1` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_has_team_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_has_team_weapon1` FOREIGN KEY (`weapon_id`) REFERENCES `weapon` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loadout`
--

LOCK TABLES `loadout` WRITE;
/*!40000 ALTER TABLE `loadout` DISABLE KEYS */;
INSERT INTO `loadout` VALUES (1,6,1),(2,6,1),(1,8,1);
/*!40000 ALTER TABLE `loadout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `special_weapon`
--

DROP TABLE IF EXISTS `special_weapon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `special_weapon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `special_name` varchar(255) NOT NULL,
  `special_image` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `special_weapon`
--

LOCK TABLES `special_weapon` WRITE;
/*!40000 ALTER TABLE `special_weapon` DISABLE KEYS */;
INSERT INTO `special_weapon` VALUES (1,'Tenta Missiles','Tenta_Missiles.png'),(2,'Inkjet','Inkjet.png'),(3,'Ink Storm','Ink_Storm.png'),(4,'Booyah Bomb','Booyah_Bomb.png'),(5,'Ultra Stamp','Ultra_Stamp.png'),(6,'Trizooka','Trizooka.png'),(7,'Big Bubbler','Big_Bubbler.png'),(8,'Zipcaster','Zipcaster.png'),(9,'Wave Breaker','Wave_Breaker.png'),(10,'Ink Vac','Ink_Vac.png'),(11,'Killer Wail 5.1','Killer_Wail_5.1.png'),(12,'Crab Tank','Crab_Tank.png'),(13,'Reefslider','Reefslider.png'),(14,'Triple Inkstrike','Triple_Inkstrike.png'),(15,'Tacticooler','Tacticooler.png');
/*!40000 ALTER TABLE `special_weapon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub`
--

DROP TABLE IF EXISTS `sub`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sub` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sub_name` varchar(255) NOT NULL,
  `sub_image` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub`
--

LOCK TABLES `sub` WRITE;
/*!40000 ALTER TABLE `sub` DISABLE KEYS */;
INSERT INTO `sub` VALUES (1,'Splat Bomb','Splat_Bomb_Flat.png'),(2,'Suction Bomb','Suction_Bomb_Flat.png'),(3,'Burst Bomb','Burst_Bomb_Flat.png'),(4,'Curling Bomb','Curling_Bomb_Flat.png'),(5,'Autobomb','Autobomb_Flat.png'),(6,'Ink Mine','Ink_Mine_Flat.png'),(7,'Toxic Mist','Toxic_Mist_Flat.png'),(8,'Point Sensor','Point_Sensor_Flat.png'),(9,'Splash Wall','Splash_Wall_Flat.png'),(10,'Sprinkler','Sprinkler_Flat.png'),(11,'Squid Beacon','Squid_Beakon_Flat.png'),(12,'Fizzy Bomb','Fizzy_Bomb_Flat.png'),(13,'Torpedo','Torpedo_Flat.png'),(14,'Angle Shooter','Angle_Shooter_Flat.png');
/*!40000 ALTER TABLE `sub` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `id` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creator_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cerator_idx` (`creator_id`),
  CONSTRAINT `creator_id` FOREIGN KEY (`creator_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (6,'InkStorm','2022-11-21 18:16:21','2022-11-21 18:16:21',1),(8,'Rainy Days','2022-11-21 18:17:00','2022-11-21 18:17:00',1);
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'clovs','david@gmail.com','$2b$12$sr.lPhhsknyrtCtx7SBq4eOu/feEu1dF/b8Pwls6sLTTlAL5atqWu','2022-11-21 17:35:38','2022-11-21 17:35:38'),(2,'agredakn','agredakat@gmail.com','$2b$12$PROLb1p8wEnuOw289ulLvuVrVyik4ZpQ85cbejFDqIB9ZHV7aN.Fu','2022-11-21 20:20:51','2022-11-21 20:20:51');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weapon`
--

DROP TABLE IF EXISTS `weapon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weapon` (
  `id` int NOT NULL,
  `weapon_name` varchar(255) NOT NULL,
  `weapon_type` varchar(255) NOT NULL,
  `weapon_image` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapon`
--

LOCK TABLES `weapon` WRITE;
/*!40000 ALTER TABLE `weapon` DISABLE KEYS */;
INSERT INTO `weapon` VALUES (1,'Hero Shot Replica','Shooters','Hero_Shot_Replica_Flat.png'),(2,'Splattershot Jr.','Shooters','Splattershot_Jr._Flat.png'),(3,'Splat Charger','Chargers','Splat_Charger_Flat.png'),(4,'Splat Roller','Rollers','Splat_Roller_Flat.png'),(5,'Splattershot','Shooters','Splattershot_Flat.png'),(6,'Blaster','Blasters','Blaster_Flat.png'),(7,'Splat Dualies','Dualies','Splat_Dualies_Flat.png'),(8,'Slosher','Sloshers','Slosher_Flat.png'),(9,'Octobrush','Brushes','Octobrush_Flat.png'),(10,'Heavy Splatling','Splatlings','Heavy_Splatling_Flat.png'),(11,'Tri-Stringer','Stringers','Tri-Stringer_Flat.png'),(12,'Splat Brella','Brellas','Splat_Brella_Flat.png'),(13,'Aerospray MG','Shooters','Aerospray_MG_Flat.png'),(14,'Splatana Wiper','Splatanas','Splatana_Wiper_Flat.png'),(15,'Carbon Roller','Rollers','Carbon_Roller_Flat.png'),(16,'N-ZAP \'85','Shooters','N-ZAP_85_Flat.png'),(17,'Rapid Blaster','Blasters','Rapid_Blaster_Flat.png'),(18,'Inkbrush','Brushes','Inkbrush_Flat.png'),(19,'Classic Squiffer','Chargers','Classic_Squiffer_Flat.png'),(20,'Dualie Squelchers','Dualies','Dualie_Squelchers_Flat.png'),(21,'Splatershot Pro','Shooters','Splattershot_Pro_Flat.png'),(22,'Sploosh-o-matic','Shooters','Sploosh-o-matic_Flat.png'),(23,'Splatterscope','Chargers','Splatterscope_Flat.png'),(24,'Tri-Slosher','Sloshers','Tri-Slosher_Flat.png'),(25,'REEF-LUX 450','Stringers','REEF-LUX_450_Flat.png'),(26,'Range Blaster','Blasters','Range_Blaster_Flat.png'),(27,'.52 Gal','Shooters','.52_Gal_Flat.png'),(28,'Dynamo Roller','Rollers','Dynamo_Roller_Flat.png'),(29,'Mini Splatling','Splatlings','Mini_Splatling_Flat.png'),(30,'Luna Blaster','Blasters','Luna_Blaster_Flat.png'),(31,'L-3 Nozzlenose','Shooters','L-3_Nozzlenose_Flat.png'),(32,'Dapple Dualies','Dualies','Dapple_Dualies_Flat.png'),(33,'Sloshing Machine','Sloshers','Sloshing_Machine_Flat.png'),(34,'Jet Squelcher','Shooters','Jet_Squelcher_Flat.png'),(35,'Splatana Stamper','Splatanas','Splatana_Stamper_Flat.png'),(36,'Tenta Brella','Brellas','Tenta_Brella_Flat.png'),(37,'Splach-o-matic','Shooters','Splash-o-matic_Flat.png'),(38,'Dark Tetra Dualies','Dualies','Dark_Tetra_Dualies_Flat.png'),(39,'.96 Gal','Shooters','.96_Gal_Flat.png'),(40,'Undercover Brella','Brellas','Undercover_Brella_Flat.png'),(41,'E-Liter 4K','Chargers','E-liter_4K_Flat.png'),(42,'Squeezer','Shooters','Squeezer_Flat.png'),(43,'Bloblobber','Sloshers','Bloblobber_Flat.png'),(44,'Flingza Roller','Rollers','Flingza_Roller_Flat.png'),(45,'Hydra Splatling','Splatlings','Hydra_Splatling_Flat.png'),(46,'Glooga Dualies','Dualies','Glooga_Dualies_Flat.png'),(47,'Clash Blaster','Blasters','Clash_Blaster_Flat.png'),(48,'Bamboozler 14 Mk 1','Chargers','Bamboozler_14_Mk_I_Flat.png'),(49,'H-3 Nozzlenose','Shooters','H-3_Nozzlenose_Flat.png'),(50,'Goo Tuber','Chargers','Goo_Tuber_Flat.png'),(51,'Rapid Blaster Pro','Blasters','Rapid_Blaster_Pro_Flat.png'),(52,'E-Liter 4K Scope','Chargers','E-liter_4K_Scope_Flat.png'),(53,'Nautilus 47','Splatlings','Nautilus_47_Flat.png'),(54,'Explosher','Sloshers','Explosher_Flat.png'),(55,'Ballpoint Splatling','Splatlings','Ballpoint_Splatling_Flat.png');
/*!40000 ALTER TABLE `weapon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weapon_loadout`
--

DROP TABLE IF EXISTS `weapon_loadout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weapon_loadout` (
  `weapon_id` int NOT NULL,
  `sub_id` int NOT NULL,
  `special_weapon_id` int NOT NULL,
  PRIMARY KEY (`weapon_id`,`sub_id`,`special_weapon_id`),
  KEY `fk_weapon_has_sub_sub1_idx` (`sub_id`),
  KEY `fk_weapon_has_sub_weapon1_idx` (`weapon_id`),
  KEY `fk_weapon_has_sub_special_weapon1_idx` (`special_weapon_id`),
  CONSTRAINT `fk_weapon_has_sub_special_weapon1` FOREIGN KEY (`special_weapon_id`) REFERENCES `special_weapon` (`id`),
  CONSTRAINT `fk_weapon_has_sub_sub1` FOREIGN KEY (`sub_id`) REFERENCES `sub` (`id`),
  CONSTRAINT `fk_weapon_has_sub_weapon1` FOREIGN KEY (`weapon_id`) REFERENCES `weapon` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weapon_loadout`
--

LOCK TABLES `weapon_loadout` WRITE;
/*!40000 ALTER TABLE `weapon_loadout` DISABLE KEYS */;
INSERT INTO `weapon_loadout` VALUES (2,1,7),(3,1,10),(8,1,14),(18,1,11),(20,1,9),(23,1,10),(30,1,8),(47,1,6),(1,2,6),(5,2,6),(7,2,12),(9,2,8),(16,2,15),(26,2,9),(29,3,5),(35,3,8),(37,3,12),(4,4,7),(22,4,5),(25,4,1),(31,4,12),(6,5,7),(15,5,8),(38,5,13),(45,5,4),(48,5,11),(17,6,14),(40,6,13),(41,6,9),(44,6,1),(52,6,9),(11,7,11),(24,7,2),(51,7,10),(19,8,7),(49,8,15),(53,8,3),(54,8,3),(27,9,11),(42,9,6),(46,9,4),(10,10,9),(12,10,14),(28,10,15),(39,10,10),(43,10,3),(32,11,15),(36,11,10),(13,12,13),(33,12,4),(55,12,2),(14,13,5),(50,13,1),(21,14,12),(34,14,10);
/*!40000 ALTER TABLE `weapon_loadout` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-22 18:04:47
