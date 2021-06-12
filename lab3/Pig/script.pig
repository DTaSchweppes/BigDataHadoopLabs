teams = LOAD '/user/root/laba3/input/data_teams.txt' USING PigStorage(',') as ( id:int, name:chararray );
teammembers = LOAD '/user/root/laba3/input/data_teammembers.txt' USING PigStorage(',') as ( id:int, name:chararray, team_id:int );
cars = LOAD '/user/root/laba3/input/data_cars.txt' USING PigStorage(',') as ( id:int, name:chararray, team_id:int, year:int );

DUMP teams;
teammembers_filtered = FILTER teammembers BY team_id == 2;
DUMP teammembers_filtered;
joined_teams_members = JOIN teams BY id, teammembers BY team_id;
joined_teams_cars = JOIN teams BY id, cars BY team_id;
DUMP joined_teams_members;
DUMP joined_teams_cars;
ordered_teams_cars = ORDER joined_teams_cars BY year ASC;
DUMP ordered_teams_cars;

