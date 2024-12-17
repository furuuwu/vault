# Representation of relationships

1. **One-to-One (1:1):**
    
    - **Definition**: Each record in Table A relates to exactly one record in Table B, and vice versa.
    - **Example**: A `User` table and a `Profile` table. Each user has exactly one profile, and each profile belongs to one user.
    - **Sample Data**:
        
        ```plaintext
        Users Table:
        | user_id | username  |
        |---------|-----------|
        | 1       | john_doe  |
        | 2       | jane_doe  |
        
        Profiles Table:
        | profile_id | user_id | bio            |
        |------------|---------|----------------|
        | 1          | 1       | Loves hiking   |
        | 2          | 2       | Enjoys cooking |
        ```
        
    - **Query**:
        - To get a user with their profile:
            
            ```sql
            SELECT u.username, p.bio
            FROM Users u
            JOIN Profiles p ON u.user_id = p.user_id;
            ```
            
2. **Many-to-One (M:1):**
    
    - **Definition**: Many records in Table A relate to one record in Table B.
    - **Example**: A `Books` table and an `Authors` table. Many books can belong to the same author.
    - **Sample Data**:
        
        ```plaintext
        Books Table:
        | book_id | title              | author_id |
        |---------|--------------------|-----------|
        | 1       | War and Peace      | 1         |
        | 2       | Anna Karenina      | 1         |
        | 3       | Crime and Punishment | 2       |
        
        Authors Table:
        | author_id | name            |
        |-----------|-----------------|
        | 1         | Leo Tolstoy     |
        | 2         | Fyodor Dostoevsky |
        ```
        
    - **Query**:
        - To get books along with their authors:
            
            ```sql
            SELECT b.title, a.name
            FROM Books b
            JOIN Authors a ON b.author_id = a.author_id;
            ```
            
3. **Many-to-Many (M:N):**
    
    - **Definition**: Many records in Table A relate to many records in Table B.
        
    - **Example**: A `Students` table and a `Courses` table. A student can enroll in multiple courses, and a course can have multiple students.
        
    - **Ways to Implement**:
        
        - Using an **Associative Entity (Join Table)**.
        - Without an associative entity (e.g., arrays in a NoSQL database).
    - **Using an Associative Entity**:
        
        - **Tables**:
            
            ```plaintext
            Students Table:
            | student_id | name   |
            |------------|--------|
            | 1          | Alice  |
            | 2          | Bob    |
            
            Courses Table:
            | course_id | title          |
            |-----------|----------------|
            | 101       | Math           |
            | 102       | Science        |
            
            Enrollment Table (Associative Entity):
            | student_id | course_id |
            |------------|-----------|
            | 1          | 101       |
            | 1          | 102       |
            | 2          | 101       |
            ```
            
        - **Query**:
            - To get all students and their enrolled courses:
                
                ```sql
                SELECT s.name, c.title
                FROM Students s
                JOIN Enrollment e ON s.student_id = e.student_id
                JOIN Courses c ON e.course_id = c.course_id;
                ```
                
    - **Without an Associative Entity**:
        
        - Some systems (e.g., NoSQL databases) allow storing arrays:
            
            ```plaintext
            Students Table:
            | student_id | name   | courses          |
            |------------|--------|------------------|
            | 1          | Alice  | [101, 102]       |
            | 2          | Bob    | [101]           |
            ```
            
        - **Query**:
            - Use system-specific array functions (e.g., MongoDB's `$lookup`).

---

### Can We Avoid Associative Entities in M:N Relationships?

- **Yes, but with limitations**:
    - **Embedded Arrays**: Use arrays in one table to reference the other.
        - Example: Store `course_ids` array in the `Students` table.
    - **Challenges**:
        - Harder to enforce referential integrity.
        - Complicated queries when data scales.
        - Not suitable for SQL databases (which lack array-like joins).

---

### Benefits of Associative Entities

1. Allows normalization and better data integrity.
2. Easy to manage additional attributes for relationships (e.g., enrollment date).

# Full outer join vs cross join

No, these two queries are **not the same**. Let me explain why:

### 1. **`FULL JOIN` Behavior**
The query:
```sql
SELECT * FROM borrower b FULL JOIN loan l ON b.borrower_id = l.borrower_id
```
performs a **full outer join**, which means:
- It includes all rows from both the `borrower` and `loan` tables.
- If there is a match on `borrower_id`, the matched rows from both tables are combined into one.
- If there is no match:
  - Rows from `borrower` with no corresponding `loan` will have `NULL` values for the `loan` columns.
  - Rows from `loan` with no corresponding `borrower` will have `NULL` values for the `borrower` columns.

### 2. **`CROSS JOIN` Behavior (Implicit JOIN)**
The query:
```sql
SELECT * FROM borrower b, loan l
```
performs a **cross join**, which means:
- It produces the **Cartesian product** of the two tables.
- Every row in `borrower` is combined with **every row in `loan`**, regardless of any relationship between them.
- The total number of rows in the result is the product of the number of rows in `borrower` and `loan`.

### Key Differences:
| **Aspect**          | **FULL JOIN**                                     | **CROSS JOIN**                                 |
|----------------------|--------------------------------------------------|-----------------------------------------------|
| **Join Type**        | Full outer join with a matching condition.       | Cartesian product (no condition).            |
| **Number of Rows**   | At most, the total rows in both tables combined. | The product of rows in both tables.           |
| **NULL Handling**    | Includes unmatched rows with `NULL` for missing columns. | No `NULL` values due to unmatched rows.       |

### Example:
Suppose:
- `borrower` has 2 rows:  
  | borrower_id | name      |  
  |-------------|-----------|  
  | 1           | Alice     |  
  | 2           | Bob       |  

- `loan` has 2 rows:  
  | borrower_id | amount    |  
  |-------------|-----------|  
  | 1           | 1000      |  
  | 3           | 1500      |  

#### `FULL JOIN` Output:
```sql
SELECT * FROM borrower b FULL JOIN loan l ON b.borrower_id = l.borrower_id;
```
Result:
| borrower_id | name  | borrower_id | amount |  
|-------------|-------|-------------|--------|  
| 1           | Alice | 1           | 1000   |  
| 2           | Bob   | NULL        | NULL   |  
| NULL        | NULL  | 3           | 1500   |  

#### `CROSS JOIN` Output:
```sql
SELECT * FROM borrower b, loan l;
```
Result:
| borrower_id | name   | borrower_id | amount |  
|-------------|--------|-------------|--------|  
| 1           | Alice  | 1           | 1000   |  
| 1           | Alice  | 3           | 1500   |  
| 2           | Bob    | 1           | 1000   |  
| 2           | Bob    | 3           | 1500   |  

---

### Conclusion:
- The **full outer join** produces results based on matching the `borrower_id`, along with unmatched rows from both sides.
- The **cross join** produces all possible combinations of rows without any matching condition.
