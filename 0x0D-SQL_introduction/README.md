0x0D. SQL - Introduction
Description
This project introduces the basics of SQL (Structured Query Language) and provides a foundation for understanding how to interact with databases using MySQL. The project covers fundamental concepts, database creation, table manipulation, data retrieval, data insertion, updating and deletion, and more.

Learning Objectives
Upon completing this project, you will be able to:

Explain the concept of a database and understand the role of relational databases.
Define SQL and understand its importance in managing databases.
Familiarize yourself with MySQL as a relational database management system.
Create databases using MySQL.
Distinguish between Data Definition Language (DDL) and Data Manipulation Language (DML).
Perform table creation and alteration using SQL commands.
Retrieve data from tables using the SELECT statement.
Insert, update, and delete data in database tables.
Understand the concept of subqueries.
Utilize MySQL functions to perform various operations.
Getting Started
To work with this project, you need to have MySQL installed. If you're using Ubuntu 20.04 LTS, you can follow these steps to install it:

Update package information:

sql
Copy code
sudo apt update
Install MySQL server:

Copy code
sudo apt install mysql-server
Check the version of MySQL:

css
Copy code
mysql --version
Connect to your MySQL server:

Copy code
sudo mysql
Running SQL Queries
You can run SQL queries in various ways:

You can use your MySQL terminal by entering mysql in your terminal.
You can run SQL scripts using the command mysql -uroot -p < script.sql in your terminal.
For example, if you have an SQL script named my_script.sql, you can run it using:

css
Copy code
mysql -uroot -p < my_script.sql
Using Container-on-Demand
If you prefer a controlled environment, you can utilize a Docker container to run MySQL. Credentials for the container are root/root.

Ask for a container with Ubuntu 20.04.
Connect via SSH or use the Web terminal.
Start MySQL inside the container using:
sql
Copy code
service mysql start
Additional Notes
Remember to explore the provided SQL scripts and experiment with various queries to solidify your understanding of SQL concepts.

Feel free to refer to the MySQL documentation for more detailed information and resources.

Author
[manal RAHALI]
