CREATE TABLE `blooddonation`.`blood_master` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `DonorName` VARCHAR(300) NOT NULL,
  `Bloodgroup` VARCHAR(20) NOT NULL,
  `MobileContact`  VARCHAR(20) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `Daibetic` VARCHAR(10) NOT NULL,
  `Comments` TEXT(1000) NULL,
  `datecreated` timestamp default now()
  )
  AUTO_INCREMENT = 1
COMMENT = 'blood_master table';