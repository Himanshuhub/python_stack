-- MySQL Script generated by MySQL Workbench
-- Tue Jun 13 11:30:40 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

-- -----------------------------------------------------
-- Schema new_books_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema new_books_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `new_books_schema` DEFAULT CHARACTER SET utf8 ;
USE `new_books_schema` ;

-- -----------------------------------------------------
-- Table `new_books_schema`.`favourite_books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `new_books_schema`.`favourite_books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `author` VARCHAR(255) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


