delimiter //
create trigger archive before delete on data for each row BEGIN
    insert into old_data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, PROTO, DATE)
    values (OLD.IPV4_SRC_ADDR, OLD.IPV4_DST_ADDR, OLD.SRC_PORT, OLD.DST_PORT, OLD.PROTO, OLD.DATE);
End;
//
delimiter ;
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('10.0.0.0', '10.0.0.0', '1', '1', '2021-04-20 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('20.0.0.0', '20.0.0.0', '2', '2', '2022-03-20 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('30.0.0.0', '30.0.0.0', '3', '3', '2025-02-20 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('40.0.0.0', '40.0.0.0', '4', '4', '2024-04-23 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('50.0.0.0', '50.0.0.0', '5', '5', '2005-04-22 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('60.0.0.0', '60.0.0.0', '6', '6', '2025-02-27 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('70.0.0.0', '70.0.0.0', '7', '7', '2014-03-26 10:00:00');
insert into data (IPV4_SRC_ADDR, IPV4_DST_ADDR, SRC_PORT, DST_PORT, DATE) values ('80.0.0.0', '80.0.0.0', '8', '8', '2008-04-02 10:00:00');