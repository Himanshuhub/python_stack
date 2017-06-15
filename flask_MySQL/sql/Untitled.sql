-- select * from friends;
-- 
-- -- INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
-- -- VALUES ("Jay", "Patel", "Instructor", NOW(), NOW());
-- -- INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
-- -- VALUES ("Matt", "Matt", "Student", NOW(), NOW());
-- 
-- SELECT  *, created_at as friendSince, YEAR ( created_at ) as yearJoined FROM friends;
-- 
-- 
-- create database email_validation;
create table email_validation. email_validation_table(
id int
, email varchar(200) NULL
);