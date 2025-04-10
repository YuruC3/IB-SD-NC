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
