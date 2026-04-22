 """
 MYSQL commands
 
 CREATE DATABASE atm;
 USE atm;

 CREATE TABLE data (
   my_name VARCHAR(50),
   pass_word VARCHAR(255),
   balance INT,
   account_no BIGINT PRIMARY KEY
 );

 CREATE TABLE transactions (
   id INT AUTO_INCREMENT PRIMARY KEY,
   account_no BIGINT,
   type VARCHAR(20),
   amount INT,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );
"""

