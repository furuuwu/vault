
## delete all data

```sql
USE sakila;

TRUNCATE TABLE `actor`;
```

```sql
USE sakila;

--Disable foreign key checks
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE `actor`;
TRUNCATE TABLE `address`;
TRUNCATE TABLE `category`;
TRUNCATE TABLE `city`;
TRUNCATE TABLE `country`;
TRUNCATE TABLE `customer`;
TRUNCATE TABLE `film`;
TRUNCATE TABLE `film_actor`;
TRUNCATE TABLE `film_category`;
TRUNCATE TABLE `film_text`;
TRUNCATE TABLE `inventory`;
TRUNCATE TABLE `language`;
TRUNCATE TABLE `payment`;
TRUNCATE TABLE `rental`;
TRUNCATE TABLE `staff`;
TRUNCATE TABLE `store`;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;
```

```sql
USE sakila;
SET FOREIGN_KEY_CHECKS = 0;

-- Prepare a dynamic script to truncate all tables
SET @tables = NULL;

-- Concatenate all the truncate table statements for the tables in the sakila schema
SELECT GROUP_CONCAT(CONCAT('TRUNCATE TABLE `', TABLE_NAME, '`;') SEPARATOR ' ') INTO @tables
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'sakila';  -- Use your database name here

-- Check if @tables is populated with the truncate statements
-- You can execute this to verify the generated query
SELECT @tables;

-- Execute the dynamic statement
PREPARE stmt FROM @tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;
```