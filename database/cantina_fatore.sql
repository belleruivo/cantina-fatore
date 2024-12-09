-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: cantina_fatore
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

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
-- Current Database: `cantina_fatore`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `cantina_fatore` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `cantina_fatore`;

--
-- Table structure for table `carrinho`
--

DROP TABLE IF EXISTS `carrinho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carrinho` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `funcionario_id` int(11) DEFAULT NULL,
  `produto_id` int(11) DEFAULT NULL,
  `quantidade` int(11) DEFAULT 1,
  PRIMARY KEY (`id`),
  KEY `funcionario_id` (`funcionario_id`),
  KEY `produto_id` (`produto_id`),
  CONSTRAINT `carrinho_ibfk_1` FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`id`),
  CONSTRAINT `carrinho_ibfk_2` FOREIGN KEY (`produto_id`) REFERENCES `produtos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrinho`
--

LOCK TABLES `carrinho` WRITE;
/*!40000 ALTER TABLE `carrinho` DISABLE KEYS */;
INSERT INTO `carrinho` VALUES (118,NULL,14,1),(119,NULL,17,1),(120,NULL,26,1),(121,NULL,19,3),(122,NULL,28,2),(123,NULL,27,1);
/*!40000 ALTER TABLE `carrinho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funcionarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `total_gasto` decimal(10,2) DEFAULT 0.00,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (8,'Aline de Lucas',10.00),(9,'Murilo da Silva Dantas',35.46),(10,'Tardelli Stekel',0.00),(11,'Raul Castanhari',0.00),(12,'Olavo Matos',0.00),(13,'Tiago de Oliveira',0.00),(14,'Rafaela Vilela',0.00),(15,'Edson Pires',0.00),(16,'Flávia de Almeida',0.00),(17,'Patrícia Alencar',0.00),(18,'Priscila Gomes',0.00);
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itens_venda`
--

DROP TABLE IF EXISTS `itens_venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itens_venda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `venda_id` int(11) NOT NULL,
  `produto_id` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL,
  `valor_unitario` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `venda_id` (`venda_id`),
  KEY `produto_id` (`produto_id`),
  CONSTRAINT `itens_venda_ibfk_1` FOREIGN KEY (`venda_id`) REFERENCES `vendas` (`id`),
  CONSTRAINT `itens_venda_ibfk_2` FOREIGN KEY (`produto_id`) REFERENCES `produtos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itens_venda`
--

LOCK TABLES `itens_venda` WRITE;
/*!40000 ALTER TABLE `itens_venda` DISABLE KEYS */;
INSERT INTO `itens_venda` VALUES (17,20,18,1,5.00,5.00),(19,22,15,1,2.50,2.50),(20,22,30,1,3.00,3.00),(21,22,26,1,4.79,4.79),(22,23,18,1,5.00,5.00),(24,24,17,1,4.99,4.99),(25,24,14,3,6.99,20.97),(26,24,13,1,5.50,5.50),(27,25,31,1,5.00,5.00);
/*!40000 ALTER TABLE `itens_venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacoes`
--

DROP TABLE IF EXISTS `notificacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notificacoes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produto_id` int(11) DEFAULT NULL,
  `mensagem` varchar(255) DEFAULT NULL,
  `status` enum('vista','não vista') DEFAULT 'não vista',
  PRIMARY KEY (`id`),
  KEY `produto_id` (`produto_id`),
  CONSTRAINT `notificacoes_ibfk_1` FOREIGN KEY (`produto_id`) REFERENCES `produtos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacoes`
--

LOCK TABLES `notificacoes` WRITE;
/*!40000 ALTER TABLE `notificacoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `notificacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `produtos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  `categoria` varchar(100) DEFAULT NULL,
  `quantidade_estoque` int(11) NOT NULL DEFAULT 0,
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos`
--

LOCK TABLES `produtos` WRITE;
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` VALUES (13,'Coxinha com Catupiry',5.50,'Salgado',30,'uploads\\coxinha.png'),(14,'Fini Amora',6.99,'Doce',20,'uploads\\fini_amora.png'),(15,'Bala Freegels',2.50,'Doce',7,'uploads\\freegels.jpg'),(16,'Água Mineral',2.50,'Bebida',12,'uploads\\agua.jpg'),(17,'Misto Quente',4.99,'Lanche',10,'uploads\\misto.jpg'),(18,'Pão de Queijo',5.00,'Salgado',19,'uploads\\pao_de_queijo.jpg'),(19,'KitKat Branco',4.99,'Doce',12,'uploads\\kitkat.jpg'),(26,'Bolacha Oreo',4.79,'Doce',7,'uploads\\oreo.png'),(27,'Tortuguita',3.00,'Doce',14,'uploads\\tortuguita.png'),(28,'Refrigerante Lata',5.00,'Bebida',23,'uploads\\refri_latas.jpg'),(29,'Suco de Laranja',7.99,'Bebida',3,'uploads\\suco-laranja.png'),(30,'Toddynho',3.00,'Bebida',5,'uploads\\toddynho.jpg'),(31,'Mini Pizza',5.00,'Salgado',3,'uploads\\mini-pizza.png');
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comprador_tipo` enum('funcionario','aluno') NOT NULL,
  `comprador_id` int(11) DEFAULT NULL,
  `metodo_pagamento` enum('dinheiro','cartao','pix') NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `data_venda` datetime DEFAULT current_timestamp(),
  `valor_dinheiro` decimal(10,2) DEFAULT NULL,
  `valor_cartao` decimal(10,2) DEFAULT NULL,
  `valor_pix` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `vendas_ibfk_1` (`comprador_id`),
  CONSTRAINT `vendas_ibfk_1` FOREIGN KEY (`comprador_id`) REFERENCES `funcionarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendas`
--

LOCK TABLES `vendas` WRITE;
/*!40000 ALTER TABLE `vendas` DISABLE KEYS */;
INSERT INTO `vendas` VALUES (20,'funcionario',8,'cartao',5.00,'2024-12-08 21:21:39',0.00,5.00,0.00),(21,'aluno',NULL,'dinheiro',4.00,'2024-12-08 21:32:10',4.00,0.00,0.00),(22,'aluno',NULL,'',10.29,'2024-12-08 21:39:48',4.00,5.00,1.29),(23,'funcionario',8,'',5.00,'2024-12-08 21:44:47',4.00,1.00,0.00),(24,'funcionario',9,'pix',35.46,'2024-12-08 21:52:00',0.00,0.00,35.46),(25,'aluno',NULL,'dinheiro',5.00,'2024-12-08 21:56:28',5.00,0.00,0.00);
/*!40000 ALTER TABLE `vendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-08 22:16:18
