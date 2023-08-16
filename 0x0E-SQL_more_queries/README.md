# Project: SQL - More Queries

This project focuses on enhancing your understanding of SQL queries and database management. By completing the tasks in this project, you'll gain hands-on experience in creating users, managing privileges, working with keys and constraints, using subqueries, and employing JOIN and UNION operations. The goal of this project is to help you achieve a solid grasp of these concepts without relying on external resources.

## Learning Objectives

By the end of this project, you will be able to:

- Create new MySQL users
- Manage privileges for users on databases or tables
- Understand the purpose of a PRIMARY KEY
- Recognize the significance of a FOREIGN KEY
- Utilize NOT NULL and UNIQUE constraints
- Retrieve data from multiple tables in a single query
- Apply subqueries to solve complex problems
- Employ JOIN and UNION operations to combine and manipulate data

## Getting Started

These instructions will guide you through setting up the necessary environment and running SQL queries for this project.

### Prerequisites

- Operating System: Ubuntu 20.04 LTS
- MySQL Version: 8.0.25

### Installation

1. Update the package list:
   ```
   $ sudo apt update
   ```

2. Install MySQL 8.0:
   ```
   $ sudo apt install mysql-server
   ```

3. Verify the installation:
   ```
   $ mysql --version
   mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
   ```

### Connecting to MySQL Server

1. Connect to MySQL server using the MySQL monitor:
   ```
   $ sudo mysql
   ```

2. To exit the MySQL monitor, use:
   ```
   mysql> quit
   ```

### Using a Container (Optional)

If you prefer using a container, you can use the following instructions to run MySQL in a container:

1. Start MySQL in the container:
   ```
   $ service mysql start
   ```

2. Connect to the container via SSH or the Web terminal.

### Importing a SQL Dump

You can import a SQL dump as follows:

1. Create a new database:
   ```
   $ echo "CREATE DATABASE your_database_name;" | mysql -uroot -p
   ```

2. Import the SQL dump:
   ```
   $ curl "URL_TO_SQL_DUMP" -s | mysql -uroot -p your_database_name
   ```

3. Run queries on the imported data:
   ```
   $ echo "SELECT * FROM your_table_name" | mysql -uroot -p your_database_name
   ```

## Project Tasks

This project consists of tasks designed to enhance your understanding of SQL concepts. For each task, create SQL scripts that address the given requirements. Remember to use uppercase for SQL keywords and provide a comment before each query explaining its purpose.

## Plagiarism

Remember that plagiarism is strictly forbidden. You should solve the tasks on your own and refrain from copying and pasting someone else's work.

## Folder Structure

Your project folder should have the following structure:

```
0x0E-SQL_More_Queries/
├── task_0.sql
├── task_1.sql
├── ...
├── task_n.sql
└── README.md
```
