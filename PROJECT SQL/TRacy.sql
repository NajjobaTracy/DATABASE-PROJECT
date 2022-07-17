CREATE TABLE `Dogs` (
  `dog_id` int,
  `dog_name` text,
  `breed_id` int,
  `sex` text,
  `age` int,
  `price` int
);

CREATE TABLE `Customers` (
  `customer_id` int PRIMARY KEY,
  `customer_name` text,
  `breed_brought` text,
  `address` text,
  `dog_id` int
);

CREATE TABLE `breed` (
  `breed_name` text PRIMARY KEY,
  `breed_id` int
);

ALTER TABLE `Customers` ADD FOREIGN KEY (`breed_brought`) REFERENCES `breed` (`breed_name`);

ALTER TABLE `Customers` ADD FOREIGN KEY (`dog_id`) REFERENCES `Dogs` (`dog_id`);

ALTER TABLE `breed` ADD FOREIGN KEY (`breed_id`) REFERENCES `Dogs` (`breed_id`);
