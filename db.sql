/**
 * @Author: Abdellah Oulahyane
 * @Date:   2021-03-25 02:36:20
 * @Last Modified by:   Abdellah Oulahyane
 * @Last Modified time: 2021-03-29 00:01:36
 */
/* Uncomment next 2 lines IF you have used MYSQL/SQLSERVER */
/*CREATE database Book;*/
/*use Book;*/
CREATE TABLE IF NOT EXISTS  category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label varchar(55) NOT NULL,
    description varchar(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS  user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference varchar(5) NOT NULL,
    fullname varchar(55) NOT NULL,
    username varchar(25) NOT NULL,
    password varchar(100) NOT NULL,
    role varchar(10) NOT NULL default 'client',
    contact varchar(55) NOT NULL,
    address varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS  book_details(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language varchar(15) NOT NULL,
    pages int NOT NULL,
    isbn_10 varchar(20) NOT NULL,
    isbn_13 varchar(20) NOT NULL,
    book_weight float NOT NULL,
    dementions varchar(25) NOT NULL,
    description varchar(255) NOT NULL,
    date_published varchar(15) NOT NULL,
    publisher int ,
    category int ,
    FOREIGN KEY(publisher) REFERENCES user(id),
    FOREIGN KEY(category) REFERENCES category(id)
);
CREATE TABLE IF NOT EXISTS  book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(55) NOT NULL,
    author varchar(20) NOT NULL,
    price float NOT NULL,
    quantity int NOT NULL default 0,
    book_details int ,
    FOREIGN key(book_details) REFERENCES book_details(id)
);

CREATE TABLE IF NOT EXISTS  sales(
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    client int ,
    book int ,
    quantity int NOT NULL,
    user int ,
    date_created varchar(20) NOT NULL,
    FOREIGN key(client) REFERENCES user(id),
    FOREIGN key(book) REFERENCES book(id),
    FOREIGN key(user) REFERENCES user(id)
);

