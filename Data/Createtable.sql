

/*
We probably need another table for common shared-data like population of each age 
and state. Minidrugdataset only have population for 12-17 so it's incomplete
*/
DROP TABLE IF EXISTS Alcohol;
CREATE TABLE Alcohol (
    State text,
    Year int,
    Population_12To17 int,
    Population_18To25 int,
    Population_26AndMore int,
    Past_year_12To17 int,
    Past_year_18To25 int, 
    Past_year_26AndMore int, 
    Rate_year_12To17 float,
    Rate_year_18To25 float, 
    Rate_year_26AndMore float,
    Past_month_12To17 int,
    Past_month_18To25 int,
    Past_month_26AndMore int,
    Rate_month_12To17 float,
    Rate_month_18To25 float,
    Rate_month_26AndMore float
);

DROP TABLE IF EXISTS Cocaine;
CREATE TABLE Cocaine (
    State text,
    Year int,
    Population_12To17 int,
    Population_18To25 int,
    Population_26AndMore int,
    Past_year_12To17 int,
    Past_year_18To25 int, 
    Past_year_26AndMore int, 
    Rate_year_12To17 float,
    Rate_year_18To25 float, 
    Rate_year_26AndMore float
);

DROP TABLE IF EXISTS Marijuana;
CREATE TABLE Marijuana (
    State text,
    Year int,
    Population_12To17 int,
    Population_18To25 int,
    Population_26AndMore int,
    New_users_12To17 int,
    New_users_18To25 int,
    New_users_26AndMore int,
    Rate_newusers_12To17 float,
    Rate_newusers_18To25 float,
    Rate_newusers_26AndMore float,
    Past_month_12To17 int,
    Past_month_18To25 int,
    Past_month_26AndMore int,
    Rate_month_12To17 float,
    Rate_month_18To25 float,
    Rate_month_26AndMore float,
    Past_year_12To17 int,
    Past_year_18To25 int, 
    Past_year_26AndMore int, 
    Rate_year_12To17 float,
    Rate_year_18To25 float, 
    Rate_year_26AndMore float
);

DROP TABLE IF EXISTS Tobacco;
CREATE TABLE Tobacco (
    State text,
    Year int,
    Population_12To17 int,
    Population_18To25 int,
    Population_26AndMore int,
    Past_year_12To17 int,
    Past_year_18To25 int, 
    Past_year_26AndMore int, 
    Rate_year_12To17 float,
    Rate_year_18To25 float, 
    Rate_year_26AndMore float,
    Past_month_12To17 int,
    Past_month_18To25 int,
    Past_month_26AndMore int,
    Rate_month_12To17 float,
    Rate_month_18To25 float,
    Rate_month_26AndMore float
);