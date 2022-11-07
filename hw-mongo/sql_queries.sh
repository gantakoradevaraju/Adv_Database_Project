#!/bin/sh
sqlite3 bikeshare.db <<'END_SQL'
.timeout 2000
.schema
.header on
.mode column
.timer on
.eqp on
select member_casual from trip limit 10;
--Query-1:
select count(*) from trip where member_casual= "member";
create index trip_member_causual on trip(member_casual);
select count(*) from trip where member_casual= "member";
--Query-2:
select count(*) from trip where end_lat > 38;
create index trip_end_lat on trip(end_lat);
select count(*) from trip where end_lat > 38;
--Query-3:
select count(*) from trip where start_station_name = "Georgia Ave & Morton St NW";
create index trip_start_station_name on trip(start_station_name);
select count(*) from trip where start_station_name = "Georgia Ave & Morton St NW";
--Query-4:
select count(*) from trip where rideable_type = "classic_bike";
create index trip_rideable_type on trip(rideable_type);
select count(*) from trip where rideable_type = "classic_bike";
--Query-5:
select count(*) from trip where start_station_name = "7th & T St NW" and end_station_name = "7th St & Massachusetts Ave NE";
select count(*) from trip where start_station_name = "7th & T St NW" or end_station_name = "7th St & Massachusetts Ave NE";
create index trip_start_station_name_end_station_name on trip(start_station_name , end_station_name );
select count(*) from trip where start_station_name = "7th & T St NW" and end_station_name = "7th St & Massachusetts Ave NE";
select count(*) from trip where start_station_name = "7th & T St NW" or end_station_name = "7th St & Massachusetts Ave NE";
--Query-6:
select count(*) from trip where rideable_type = "classic_bike" and member_casual = "casual";
create index trip_rideable_type_member_casual on trip(rideable_type , member_casual );
select count(*) from trip where rideable_type = "classic_bike" and member_casual = "casual";
--Query-7:
select count(*) from trip where rideable_type = "classic_bike" and member_casual = "casual" and start_station_name == "7th & T St NW";
create index trip_on_3_columns on trip(rideable_type , member_casual , start_station_name );
select count(*) from trip where rideable_type = "classic_bike" and member_casual = "casual" and start_station_name == "7th & T St NW";
--Query-8:
select count(*) from trip where rideable_type = "classic_bike" and member_casual = "casual" and start_station_name == "7th & T St NW" or end_station_name = "7th St & M
assachusetts Ave NE";
create index trip_on_4_columns on trip(rideable_type , member_casual , start_station_name , end_station_name );
select count(*) from trip where rideable_type = "classic_bike" and member_casual = "casual" and start_station_name == "7th & T St NW" or end_station_name = "7th St & M
assachusetts Ave NE";
END_SQL
