

/*
We probably need another table for common shared-data like population of each age 
and state. Minidrugdataset only have population for 12-17 so it's incomplete
*/
DROP TABLE IF EXISTS Year_table;
ALTER TABLE Year_table ADD PRIMARY KEY (Year_id)
CREATE TABLE Alcohol_table (
    Year_no, int
);

DROP TABLE IF EXISTS State_table;
ALTER TABLE State_table ADD PRIMARY KEY (State_id)
CREATE TABLE State_table (
    Year_no, int
);

DROP TABLE IF EXISTS Alcohol_table;
FOREIGN KEY(State_id)
REFERENCES State_table (State_id);
FOREIGN KEY(Year_id)
REFERENCES Year_table (Year_id);
CREATE TABLE Alcohol_table (
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

DROP TABLE IF EXISTS Cocaine_table;
FOREIGN KEY(State_id)
REFERENCES State_table (State_id);
FOREIGN KEY(Year_id)
REFERENCES Year_table (Year_id);
CREATE TABLE Cocaine_table (
    Past_year_12To17 int,
    Past_year_18To25 int, 
    Past_year_26AndMore int, 
    Rate_year_12To17 float,
    Rate_year_18To25 float, 
    Rate_year_26AndMore float
);

DROP TABLE IF EXISTS Marijuana_table;
FOREIGN KEY(State_id)
REFERENCES State_table (State_id);
FOREIGN KEY(Year_id)
REFERENCES Year_table (Year_id);
CREATE TABLE Marijuana_table (
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

DROP TABLE IF EXISTS Tobacco_table;
FOREIGN KEY(State_id)
REFERENCES State_table(State_id);
FOREIGN KEY(Year_id)
REFERENCES Year_table(Year_id);
CREATE TABLE Tobacco_table (
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