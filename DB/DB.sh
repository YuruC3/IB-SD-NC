#!/bin/bash

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
create table data (ID int, IPV4_SRC_ADDR varchar(100), IPV4_DST_ADDR varchar(100), NEXT_HOP varchar(100), INPUT varchar(100), OUTPUT varchar (100),
 IN_PACKETS varchar(100), IN_OCTETS varchar(100), FIRST_SWITCHED varchar(100), LAST_SWITCHED varchar(100), SRC_PORT varchar(100), DST_PORT varchar(100),
 TCP_FLAGS varchar(100), PROTO varchar(100), TOS varchar(100), SRC_AS varchar(100), DST_AS varchar(100), SRC_MASK varchar(100), DST_MASK varchar(100), DATE date);