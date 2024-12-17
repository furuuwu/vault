https://www.coursera.org/learn/sql-data-science/home/module/6


**views**
- views can't use ORDER BY

```sql
-- create or modify view
CREATE OR REPLACE VIEW EMPSALARY AS
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, JOB_TITLE,
MIN_SALARY, MAX_SALARY
FROM EMPLOYEES, JOBS
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;

-- query view
SELECT * FROM EMPSALARY;

-- drop it
DROP VIEW EMPSALARY;
```

```sql
-- Create a view “EMP_DEPT” which has the following information: EMP_ID, FNAME, LNAME and DEP_ID from EMPLOYEES table
CREATE VIEW EMP_DEPT AS
SELECT EMP_ID, F_NAME, L_NAME, DEP_ID
FROM EMPLOYEES;

-- Modify “EMP_DEPT” such that it displays Department names instead of Department IDs. For this, we need to combine information from EMPLOYEES and DEPARTMENTS as follows: EMP_ID, FNAME, LNAME from EMPLOYEES table and DEP_NAME from DEPARTMENTS table, combined over the columns DEP_ID and DEPT_ID_DEP.
CREATE OR REPLACE VIEW EMP_DEPT AS
SELECT EMP_ID, F_NAME, L_NAME, DEP_NAME
FROM EMPLOYEES, DEPARTMENTS
WHERE EMPLOYEES.DEP_ID = DEPARTMENTS.DEPT_ID_DEP;
```


**stored procedures**

