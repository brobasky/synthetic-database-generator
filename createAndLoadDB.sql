/*
script used to create database and load data
paths need to be edited with load data
*/

create table stores (
  address varchar(20),
  storenumber varchar(20),
  city varchar(20),
  cost float(20),
  primary key(storenumber)
);

create table instruments(
  serialno varchar(20),
  type varchar(20),
  brand varchar(20),
  model varchar(20),
  price float(20),
  primary key(serialno)
);

create table employees(
  idno varchar(20),
  name varchar(20),
  sales varchar(20),
  salary float(20),
  phone varchar(20),
  primary key(idno)
);

create table teachers(
  idno varchar(20),
  name varchar(20),
  lessonrevenue float(20),
  availibility varchar(20),
  phone varchar(20),
  instrument varchar(20),
  primary key(idno)
);

create table students(
  phone varchar(20),
  name varchar(20),
  instrument varchar(20),
  lessondate varchar(20),
  paymentstatus varchar(20),
  primary key (phone)
);

create table sells(
  storenumber varchar(20),
  serialno varchar(20),
  foreign key (storenumber) references stores(storenumber),
  foreign key (serialno) references instruments(serialno)
);

create table employs(
  storenumber varchar(20),
  idno varchar(20),
  foreign key(storenumber) references stores(storenumber),
  foreign key(idno) references employees(idno)
);

create table have(
  idno varchar(20),
  phone varchar(20),
  foreign key(idno) references teachers(idno),
  foreign key(phone) references students(phone)
);


load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/teacherdata.csv' into table teachers
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/employeedata.csv' into table employees
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/storesdata.csv' into table stores
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/instrumentdata.csv' into table instruments
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/studentdata.csv' into table students
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/sellsdata.csv' into table sells
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/R_employsData.csv' into table employs
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/mnt/c/Users/broba/OneDrive/Desktop/COMP3421/Assignment4/havedata.csv' into table have
  fields terminated by ','
  lines terminated by '\n'
  ;
