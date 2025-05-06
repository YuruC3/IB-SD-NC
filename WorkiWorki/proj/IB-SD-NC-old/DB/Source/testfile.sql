#Följande är de kommandon som används för att sätta upp databasen för source (dvs den databas som befinner sig på RPi).

set global binlog_format = 'STATEMENT';
create user 'replicate'@'%' identified by 'cisco';
grant replication slave on *.* to 'replicate'@'%';
flush privileges;
show binary log status;

#Notera de värden som finns under file och position och gå sedan till att sätta upp replicate databasen.

#När replicate är uppsatt och fungerar, följ följande steg.

create database SFlow_Data;
use SFlow_Data;
create table data (ID int auto_increment, IPV4_SRC_ADDR varchar(100), IPV4_DST_ADDR varchar(100), SRC_PORT varchar(100), DST_PORT varchar(100), PROTO varchar(100), DATE timestamp default current_timestamp, primary key(ID));
create event prune_data on schedule every 1 day do delete from data where 2592000 <= UNIX_TIMESTAMP(UTC_DATE()) - UNIX_TIMESTAMP(DATE);
create database Switch_Conf;
use Switch_Conf;
create table conf (ID int auto_increment, CONF TEXT(65535), DATE timestamp default current_timestamp, primary key(ID));
create database QoS_Log;
use QoS_Log;
create table logs (ID int auto_increment, PROBLEM varchar(255), SOLUTION varchar(255), DATE timestamp default current_timestamp, primary key(ID));

#Configen av source är nu klar.

#Följande är kommandon för att lägga in flera artiklar i data tabellen.
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('10.0.0.0', '10.0.0.0', '1', '1', '2021-04-20 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('20.0.0.0', '20.0.0.0', '2', '2', '2022-03-20 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('30.0.0.0', '30.0.0.0', '3', '3', '2025-02-20 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('40.0.0.0', '40.0.0.0', '4', '4', '2024-04-23 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('50.0.0.0', '50.0.0.0', '5', '5', '2005-04-22 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('60.0.0.0', '60.0.0.0', '6', '6', '2025-02-27 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('70.0.0.0', '70.0.0.0', '7', '7', '2014-03-26 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('80.0.0.0', '80.0.0.0', '8', '8', '2008-04-02 10:00:00');