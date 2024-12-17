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

-- 1.2. Write and execute a SQL query to list all crimes that took place at a school. Include case number, crime type and community name.

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

-- 3.1 Write the structure of a query to create or replace a stored procedure called UPDATE_LEADERS_SCORE that takes a in_School_ID parameter as an integer and a in_Leader_Score parameter as an integer.


-- 3.2 Inside your stored procedure, write a SQL statement to update the Leaders_Score field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID to the value in the in_Leader_Score parameter.


/*
3.3 Inside your stored procedure, write a SQL IF statement to update the Leaders_Icon field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID using the following information.
Score lower limit	Score upper limit	Icon
80	99	Very strong
60	79	Strong
40	59	Average
20	39	Weak
0	19	Very weak
*/

-- 3.4 Run your code to create the stored procedure. Write a query to call the stored procedure, passing a valid school ID and a leader score of 50, to check that the procedure works as expected.

-- 4.1 Update your stored procedure definition. Add a generic ELSE clause to the IF statement that rolls back the current work if the score did not fit any of the preceding categories.

-- 4.2 Update your stored procedure definition again. Add a statement to commit the current unit of work at the end of the procedure. Write and run one query to check that the updated stored procedure works as expected when you use a valid score of 38. Write and run another query to check that the updated stored procedure works as expected when you use an invalid score of 101.
```