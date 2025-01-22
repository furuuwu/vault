You have to analyze the following datasets for the city of Chicago, as available on the Chicago City data portal.
* Socioeconomic indicators in Chicago
* Chicago public schools
* Chicago crime data

the tables will be created:
* chicago_public_schools
* chicago_socioeconomic_data
* chicago_crime

```sql
-- 1.1 Write and execute a SQL query to list the school names, community names and average attendance for communities with a hardship index of 98.

-- chicago_socioeconomic_data, chicago_public_schools, chicage_crime
-- SELECT * FROM chicago_public_schools LIMIT 5;

SELECT school.NAME_OF_SCHOOL, school.COMMUNITY_AREA_NAME, school.AVERAGE_STUDENT_ATTENDANCE
FROM chicago_public_schools school
LEFT JOIN chicago_socioeconomic_data econ
ON school.COMMUNITY_AREA_NUMBER = econ.COMMUNITY_AREA_NUMBER
WHERE econ.HARDSHIP_INDEX = 98;

-- 1.2. Write and execute a SQL query to list all crimes that took place at a school. Include case number, crime type and community name.

-- chicago_socioeconomic_data, chicago_public_schools, chicage_crime

-- SELECT DISTINCT(LOCATION_DESCRIPTION) FROM chicago_crime WHERE LOCATION_DESCRIPTION LIKE "%School%";

SELECT crimes.CASE_NUMBER, crimes.PRIMARY_TYPE, crimes.COMMUNITY_AREA_NUMBER, crimes.LOCATION_DESCRIPTION
FROM chicago_crime crimes
JOIN chicago_socioeconomic_data econ
ON crimes.COMMUNITY_AREA_NUMBER = econ.COMMUNITY_AREA_NUMBER
WHERE crimes.LOCATION_DESCRIPTION LIKE "%School%";

/*
2.1 Write and execute a SQL statement to create a view showing the columns listed in the following table, with new column names as shown in the second column.
Column name in CHICAGO_PUBLIC_SCHOOLS	Column name in view
NAME_OF_SCHOOL	School_Name
Safety_Icon	Safety_Rating
Family_Involvement_Icon	Family_Rating
Environment_Icon	Environment_Rating
Instruction_Icon	Instruction_Rating
Leaders_Icon	Leaders_Rating
Teachers_Icon	Teachers_Rating

2.2 Write and execute a SQL statement that returns all of the columns from the view.

2.3 Write and execute a SQL statement that returns just the school name and leaders rating from the view.
*/

DROP VIEW IF EXISTS question1;
CREATE VIEW question1 AS
SELECT 
    schools.NAME_OF_SCHOOL AS School_Name, 
    schools.Safety_Icon AS Safety_Rating, 
    schools.Family_Involvement_Icon AS Family_Rating, 
    schools.Environment_Icon AS Environment_Rating, 
    schools.Instruction_Icon AS Instruction_Rating, 
    schools.Leaders_Icon AS Leaders_Rating, 
    schools.Teachers_Icon AS Teachers_Rating
FROM chicago_public_schools schools;

SELECT * FROM question1;

SELECT School_Name, Leaders_Rating FROM question1;

-- 3.1 Write the structure of a query to create or replace a stored procedure called UPDATE_LEADERS_SCORE that takes a in_School_ID parameter as an integer and a in_Leader_Score parameter as an integer.

DELIMITER $$
CREATE OR REPLACE PROCEDURE UPDATE_LEADERS_SCORE (in_School_ID INT, in_Leader_Score INT)
BEGIN
-- TODO
END
$$
DELIMITER ;


-- 3.2 Inside your stored procedure, write a SQL statement to update the Leaders_Score field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID to the value in the in_Leader_Score parameter.

DELIMITER $$

CREATE PROCEDURE UPDATE_LEADERS_SCORE (in_School_ID INT, in_Leader_Score INT)
BEGIN
    UPDATE chicago_public_schools
    SET Leaders_Score = in_Leader_Score
    WHERE School_ID = in_School_ID;
END
$$

DELIMITER ;

/*
3.3 Inside your stored procedure, write a SQL IF statement to update the Leaders_Icon field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID using the following information.
Score lower limit	Score upper limit	Icon
80	99	Very strong
60	79	Strong
40	59	Average
20	39	Weak
0	19	Very weak
*/

DELIMITER $$

CREATE PROCEDURE UPDATE_LEADERS_ICON (in_School_ID INT, in_Leader_Score INT)
BEGIN
    DECLARE leader_icon VARCHAR(20);

    -- Determine the Leaders_Icon value based on the score ranges
    IF in_Leader_Score BETWEEN 80 AND 99 THEN
        SET leader_icon = 'Very strong';
    ELSEIF in_Leader_Score BETWEEN 60 AND 79 THEN
        SET leader_icon = 'Strong';
    ELSEIF in_Leader_Score BETWEEN 40 AND 59 THEN
        SET leader_icon = 'Average';
    ELSEIF in_Leader_Score BETWEEN 20 AND 39 THEN
        SET leader_icon = 'Weak';
    ELSE
        SET leader_icon = 'Very weak';
    END IF;

    -- Update the Leaders_Icon field in the database
    UPDATE chicago_public_schools
    SET Leaders_Icon = leader_icon
    WHERE School_ID = in_School_ID;
END$$

DELIMITER ;


-- 3.4 Run your code to create the stored procedure. Write a query to call the stored procedure, passing a valid school ID and a leader score of 50, to check that the procedure works as expected.

CALL UPDATE_LEADERS_ICON(610038, 50);

-- 4.1 Update your stored procedure definition. Add a generic ELSE clause to the IF statement that rolls back the current work if the score did not fit any of the preceding categories.

DELIMITER $$

CREATE PROCEDURE UPDATE_LEADERS_ICON (in_School_ID INT, in_Leader_Score INT)
BEGIN
    DECLARE leader_icon VARCHAR(20);

    -- Start a transaction
    START TRANSACTION;

    -- Determine the Leaders_Icon value based on the score ranges
    IF in_Leader_Score BETWEEN 80 AND 99 THEN
        SET leader_icon = 'Very strong';
    ELSEIF in_Leader_Score BETWEEN 60 AND 79 THEN
        SET leader_icon = 'Strong';
    ELSEIF in_Leader_Score BETWEEN 40 AND 59 THEN
        SET leader_icon = 'Average';
    ELSEIF in_Leader_Score BETWEEN 20 AND 39 THEN
        SET leader_icon = 'Weak';
    ELSEIF in_Leader_Score BETWEEN 0 AND 19 THEN
        SET leader_icon = 'Very weak';
    ELSE
        -- Rollback transaction if the score is invalid
        ROLLBACK;
        LEAVE;
    END IF;

    -- Update the Leaders_Icon field in the database
    UPDATE chicago_public_schools
    SET Leaders_Icon = leader_icon
    WHERE School_ID = in_School_ID;

    -- Commit the transaction
    COMMIT;
END$$

DELIMITER ;


-- 4.2 Update your stored procedure definition again. Add a statement to commit the current unit of work at the end of the procedure. Write and run one query to check that the updated stored procedure works as expected when you use a valid score of 38. Write and run another query to check that the updated stored procedure works as expected when you use an invalid score of 101.


DELIMITER $$

CREATE PROCEDURE UPDATE_LEADERS_ICON (in_School_ID INT, in_Leader_Score INT)
BEGIN
    DECLARE leader_icon VARCHAR(20);

    -- Start a transaction
    START TRANSACTION;

    -- Determine the Leaders_Icon value based on the score ranges
    IF in_Leader_Score BETWEEN 80 AND 99 THEN
        SET leader_icon = 'Very strong';
    ELSEIF in_Leader_Score BETWEEN 60 AND 79 THEN
        SET leader_icon = 'Strong';
    ELSEIF in_Leader_Score BETWEEN 40 AND 59 THEN
        SET leader_icon = 'Average';
    ELSEIF in_Leader_Score BETWEEN 20 AND 39 THEN
        SET leader_icon = 'Weak';
    ELSEIF in_Leader_Score BETWEEN 0 AND 19 THEN
        SET leader_icon = 'Very weak';
    ELSE
        -- Rollback transaction if the score is invalid
        ROLLBACK;
        LEAVE PROCEDURE;
    END IF;

    -- Update the Leaders_Icon field in the database
    UPDATE chicago_public_schools
    SET Leaders_Icon = leader_icon
    WHERE School_ID = in_School_ID;

    -- Commit the transaction
    COMMIT;
END$$

DELIMITER ;

-- Test with a valid score (38)
CALL UPDATE_LEADERS_ICON(610038, 38);

-- Test with invalid score (101)
CALL UPDATE_LEADERS_ICON(123, 101);

```