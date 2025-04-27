#Följande är de kommandon som används för att sätta upp databasen för replicate (dvs den databas som befinner sig på off-site enheten), efter att man har börjat sätta upp source-databasen.

change replication source to
SOURCE_HOST='mysql_source',
SOURCE_PORT=3306,
SOURCE_USER='replicate',
SOURCE_PASSWORD='cisco',
SOURCE_LOG_FILE='[file-värdet från source]',
SOURCE_LOG_POS=[position-värdet från source],
GET_SOURCE_PUBLIC_KEY=1;

start replica;
#Går att köra "show replica status\G" för att kolla om replication är uppsatt korrekt.
#Gå sedan tillbaka till source-databasen.

#Efter configen av source är klar gör följande.

use SFlow_Data;
create table old_data (ID int auto_increment, IPV4_SRC_ADDR varchar(100), IPV4_DST_ADDR varchar(100), SRC_PORT varchar(100), DST_PORT varchar(100), PROTO varchar(100), DATE timestamp default current_timestamp, primary key(ID));

delimiter //
create trigger archive before delete on data for each row BEGIN
    insert into old_data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, PROTO, DATE)
    values (OLD.IPV4_SRC_ADDR, OLD.IPV4_DST_ADDR, OLD.SRC_PORT, OLD.DST_PORT, OLD.PROTO, OLD.DATE);
End;
//
delimiter ;

