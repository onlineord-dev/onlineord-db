create table users(
 ID INT not null auto_increment,
 Email varchar(255),
 Name varchar(255),
 Surname varchar(255),
 Passwords varchar(255),
 Phone_number varchar(255),
 primary key(ID)
)

create table organization(
 ID INT not null auto_increment,
 Name varchar(255),
 Address varchar(255),
 Email varchar(255),
 Passwords varchar(255),
 Phone_number varchar(255),
 primary key(ID)
)


create table orders(
 ID INT not null auto_increment,
 User_id int,
 Organization_id int,
 Total_price float,
 primary key(ID),
 FOREIGN KEY (User_id)  REFERENCES users(ID),
 FOREIGN KEY (Organization_id)  REFERENCES organization(ID)
)


create table menu(
 ID INT not null auto_increment,
 Title varchar(255),
 Description(255),
 Organization_id int,
 primary key(ID),
 FOREIGN KEY (Organization_id)  REFERENCES organization(ID)
)

create table sub_menu(
  ID INT not null auto_increment,
  submenu_name varchar(255),
  menu_id int,
  primary key(ID),
  FOREIGN KEY (menu_id)  REFERENCES menu(ID)
)

create table food(
 ID INT not null auto_increment,
 Price float,
 Name varchar(255),
 Submenu_id int,
 Image varchar(255),
 weight int,
 primary key(ID),
 FOREIGN KEY (Submenu_id)  REFERENCES sub_menu(ID)
 
)

create table order_item(
 ID INT not null auto_increment,
 Order_id int,
 Food_id int,
 Item_price float,
 primary key(ID),
 FOREIGN KEY (Food_id)  REFERENCES food(ID),
 FOREIGN KEY (Order_id)  REFERENCES orders(ID)
)
