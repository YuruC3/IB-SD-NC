create database Sflow_Data;
use Sflow_Data;
create table data (ID int auto_increment, IPV4_SRC_ADDR varchar(100), IPV4_DST_ADDR varchar(100), SRC_PORT varchar(100), DST_PORT varchar(100), PROTO varchar(100), DATE datetime, primary key(ID));
