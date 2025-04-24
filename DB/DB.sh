#!/bin/bash
#Gammal, använd config-guiden istället.
if [ $(/usr/bin/id -u) -ne 0 ]
 then
	echo "Måste Köras med sudo"
	exit
fi

apt update
apt upgrade
apt install mysql-server
service mysql restart
mysql
create database Netflow_Data;
use Netflow_Data;
create table data (ID int auto_increment, IPV4_SRC_ADDR varchar(100), IPV4_DST_ADDR varchar(100), NEXT_HOP varchar(100), INPUT varchar(100), OUTPUT varchar (100), IN_PACKETS varchar(100), IN_OCTETS varchar(100), FIRST_SWITCHED varchar(100), LAST_SWITCHED varchar(100), SRC_PORT varchar(100), DST_PORT varchar(100), TCP_FLAGS varchar(100), PROTO varchar(100), TOS varchar(100), SRC_AS varchar(100), DST_AS varchar(100), SRC_MASK varchar(100), DST_MASK varchar(100), DATE timestamp default current_timestamp, primary key(ID));
create event prune_data on schedule every 1 day do delete from data where 2592000 <= UNIX_TIMESTAMP(UTC_DATE()) - UNIX_TIMESTAMP(DATE);
create database Switch_Conf;
use Switch_Conf;
create table conf (ID int auto_increment, CONF TEXT(65535), DATE timestamp default current_timestamp, primary key(ID));
create database QoS_Log;
use QoS_Log;
create table logs (ID int auto_increment, PROBLEM varchar(255), SOLUTION varchar(255), DATE timestamp default current_timestamp, primary key(ID));
