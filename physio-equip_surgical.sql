-- phpMyAdmin SQL Dump
-- version 4.0.4.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 23, 2021 at 06:55 PM
-- Server version: 5.5.32
-- PHP Version: 5.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `physio-equip surgical`
--
CREATE DATABASE IF NOT EXISTS `physio-equip surgical` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `physio-equip surgical`;

-- --------------------------------------------------------

--
-- Table structure for table `buy`
--

CREATE TABLE IF NOT EXISTS `buy` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `username` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pincode` int(10) NOT NULL,
  `purchase_type` varchar(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `quantity` int(10) NOT NULL,
  `product_price` int(10) NOT NULL,
  `total_price` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `buy`
--

INSERT INTO `buy` (`id`, `fname`, `lname`, `username`, `address`, `pincode`, `purchase_type`, `product_name`, `quantity`, `product_price`, `total_price`) VALUES
(1, 'Jignesh', 'Rana', 'Jignesh Rana', 'Koldongri Andheri(E)\n', 400069, 'Purchased', 'Software Diathermy 300 W', 2, 32000, 64000),
(2, 'Jignesh', 'Rana', 'Jignesh Rana', 'Koldongri Andheri(E)\n', 400069, 'Purchased', 'Software Diathermy 500 W', 2, 44000, 88000),
(3, 'Jignesh', 'Rana', 'Jignesh Rana', 'Koldongri Andheri(E)\n', 400069, 'Purchased', 'Cervical Cum Lumbar Traction', 2, 25000, 50000);

-- --------------------------------------------------------

--
-- Table structure for table `rent`
--

CREATE TABLE IF NOT EXISTS `rent` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `username` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pincode` int(10) NOT NULL,
  `purchase_type` varchar(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `quantity` int(10) NOT NULL,
  `product_price` int(10) NOT NULL,
  `total_price` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `rent`
--

INSERT INTO `rent` (`id`, `fname`, `lname`, `username`, `address`, `pincode`, `purchase_type`, `product_name`, `quantity`, `product_price`, `total_price`) VALUES
(1, 'Jignesh', 'Rana', 'Jignesh Rana', 'Koldongri Andheri(E)\n', 400069, 'On Leased', 'Software Diathermy 300 W', 2, 250, 500),
(2, 'Jignesh', 'Rana', 'Jignesh Rana', 'Koldongri Andheri(E)\n', 400069, 'On Leased', 'Software Diathermy 500 W', 2, 300, 600),
(3, 'Jignesh', 'Rana', 'Jignesh Rana', 'Koldongri Andheri(E)\n', 400069, 'On Leased', 'Cervical Cum Lumbar Traction', 2, 300, 600);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `pincode` int(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `fname`, `lname`, `username`, `password`, `pincode`, `address`) VALUES
(1, 'Jignesh', 'Rana', 'Jignesh Rana', 'Jignesh123', 400069, 'Koldongri Andheri(E)\n');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
