# Power BI (GPT)

## intro to Power BI

### **What is Power BI?**

Power BI is a business analytics and data visualization tool developed by Microsoft. It allows users to connect to various data sources, transform raw data, and create interactive reports and dashboards. Power BI is designed to help organizations make data-driven decisions by visualizing trends, patterns, and insights in a user-friendly interface.

Power BI is available in multiple versions, including:

- **Power BI Desktop**: Free application for creating reports.
- **Power BI Service**: A cloud-based platform for sharing and collaboration.
- **Power BI Pro**: Paid version of the service with additional collaboration and sharing capabilities.
- **Power BI Premium**: Offers advanced features like AI, on-premises report server, and enhanced performance.
- **Power BI Mobile**: Apps for viewing and interacting with reports on mobile devices.

---

### **Main Concepts of Power BI**

1. **Datasets**:
   - Collections of data imported from various sources (e.g., Excel, SQL databases, APIs, cloud services).
   - Data can be cleaned, transformed, and prepared using **Power Query**.

2. **Reports**:
   - A collection of visualizations (charts, tables, maps, etc.) displayed on one or more pages.
   - Created in Power BI Desktop and can be published to the Power BI Service.

3. **Dashboards**:
   - Single-page, interactive views of key metrics and visuals from one or more reports.
   - Designed for quick insights and decision-making.

4. **Visualizations**:
   - Graphical representations of data, such as bar charts, line graphs, pie charts, or maps.
   - Highly customizable and interactive.

5. **Power Query**:
   - A data transformation and preparation tool within Power BI.
   - Allows you to clean, merge, and shape data before analysis.

6. **Power BI Service**:
   - A cloud-based platform for sharing reports, dashboards, and datasets.
   - Provides collaboration features and scheduled data refresh.

7. **Data Sources**:
   - Power BI connects to various data sources like Excel, SQL Server, Azure, Google Analytics, Salesforce, and more.

8. **Data Modeling**:
   - Establishing relationships between tables, creating calculated columns, and writing measures using **DAX (Data Analysis Expressions)**.

9. **Row-Level Security (RLS)**:
   - Restricting access to data based on user roles.

10. **Natural Language Query**:
    - Allows users to ask questions in plain language (e.g., "Show sales by region") to generate visualizations automatically.

### **Semantic Modeling in Power BI: Factual vs. Custom Visuals**

#### **1. Semantic Modeling**

Semantic modeling in Power BI involves creating a structure for your data model that defines relationships, calculations, and hierarchies. It enables users to interact with data using business-friendly terms, abstracting the complexity of the underlying data.

**Key Concepts:**

- **Factual Models:** These typically involve data that contains measurable business facts (e.g., sales, profits). The model is based around **fact tables** (e.g., sales data) and **dimension tables** (e.g., products, regions). These are generally more straightforward and involve relationships between facts and dimensions.
  
  **Example:**
  - **Fact Table:** Sales transactions (with columns like Date, Product, Amount).
  - **Dimension Table:** Product (with columns like ProductID, ProductName).

- **Custom Visuals:** These are Power BI visuals that you create to suit your specific needs. They can be either:
  - **Custom visuals from the marketplace**: Power BI allows you to import custom visuals created by third parties.
  - **Custom visuals with custom DAX measures**: You create visualizations based on your data models, but these may be more customized or tailored than the default Power BI visuals.

  **Example:**
  - Using a custom visual like a **heatmap** or **hierarchical tree map** to represent data in a more meaningful or intuitive way.

### **Factual vs Custom Visuals:**

- **Factual Visuals**:
  - Default Power BI visuals like bar charts, line charts, tables, and pie charts.
  - Designed to display well-structured, factual data directly.
  - Focus on clarity and standard representations.

- **Custom Visuals**:
  - Created using **Power BI custom visual SDK** or sourced from the **AppSource** marketplace.
  - Useful for specialized data visualization needs (e.g., network graphs, custom charts).
  - Provide flexibility to represent data in non-standard ways.

**When to Use Custom Visuals:**

- When the **default visuals** do not fulfill specific business needs or when a particular **presentation style** is required.
- When you want to enhance **user interaction** with the data.
  
---

### **Sharing Power BI Reports: Embed as Iframe**

To share a Power BI report via an **iframe**, follow these steps:

1. **Publish to Power BI Service**:
   - First, you need to **publish** your report to the Power BI Service (online platform).

2. **Get the Embed Link**:
   - In Power BI Service, navigate to the report.
   - Click on **File** > **Publish to web**. This creates a link that can be embedded.

3. **Embed as Iframe**:
   - Once the **embed code** is generated, you can embed it as an iframe on your website.

   ```html
   <iframe width="800" height="600" src="https://app.powerbi.com/view?r=someEmbedURL" frameborder="0" allowFullScreen="true"></iframe>
   ```

**Important:**

- **Security**: If you are using "Publish to web," the report is publicly accessible. Be cautious about sharing sensitive or confidential data. If you need secure sharing, use **Power BI Embedded** or **Power BI Service with row-level security**.

---

### **Power BI Service: Dashboard vs. Report**

#### **1. Report**

- **What it is**: A **report** in Power BI is a collection of one or more visualizations (pages of charts, tables, graphs) built from data.
- **Characteristics**:
  - **Multiple pages**: A report can consist of multiple pages, each displaying different visualizations.
  - **Detailed Data**: Reports often contain detailed and segmented data with interactive elements like slicers and filters.
  - **Deep Exploration**: Reports are ideal for detailed exploration of data, where users can interact with the visualizations to drill down, filter, and get more insights.

  **Example**: A detailed sales report showing sales by region, product, and time period with slicers to filter data dynamically.

#### **2. Dashboard**

- **What it is**: A **dashboard** in Power BI is a single-page view that typically shows key performance indicators (KPIs) and summary information.
- **Characteristics**:
  - **Single-page summary**: Dashboards bring together visualizations from multiple reports or datasets into one page.
  - **Real-time data**: Dashboards are often used for high-level, **real-time monitoring**.
  - **Focused Metrics**: Dashboards typically focus on specific metrics, often summarized as KPIs, and don't provide deep drill-down functionality like reports.

  **Example**: A marketing dashboard that shows key metrics like total sales, conversion rates, and traffic sources, all on one page.

**Comparison**:

- **Report**: Great for detailed analysis, exploring data, and drilling into specifics.
- **Dashboard**: Great for high-level summaries and monitoring key metrics in one place.

---

### **Power BI Service: Workspace Apps**

#### **Workspace Apps**

- **What they are**: Power BI **workspace apps** provide an easy way to share content (reports, dashboards, datasets) within a team or organization.
- **Characteristics**:
  - **Organized Content**: Apps bundle reports, dashboards, and datasets in an organized way. Users can access them in one place.
  - **Customization**: Power BI admins can customize apps to include reports, dashboards, and even data sources relevant to specific teams or departments.
  - **Centralized Access**: Once an app is published, all members within the workspace can access the content without needing individual permissions for each report or dashboard.
  
#### **Steps to Create a Workspace App**

1. **Create a Workspace**: In Power BI Service, create a workspace for your team.
2. **Add Content**: Add reports, dashboards, and datasets to this workspace.
3. **Publish as an App**: Publish the workspace content as an app, which can be accessed by users with the appropriate permissions.

**Example Use Case**:

- A **Sales Team App** might include a set of dashboards with sales KPIs, a detailed report on quarterly performance, and access to sales data.

---

### **Alternatives to Power BI**

1. **Tableau**:
   - A popular data visualization tool with a strong focus on user-friendly dashboards and advanced visualizations.
   - Known for its flexibility and integration with many data sources.

2. **Looker (Google Cloud)**:
   - A business intelligence platform focused on data modeling and integration within the Google ecosystem.
   - Offers robust SQL-based data querying.

3. **Qlik Sense**:
   - A self-service data visualization and analytics tool with AI-powered insights.
   - Strong focus on associative data modeling.

4. **Google Data Studio**:
   - Free, cloud-based tool for creating basic reports and dashboards.
   - Best suited for small-scale projects and Google Workspace users.

5. **Domo**:
   - Cloud-based BI platform with integrated ETL, visualization, and collaboration tools.
   - Focuses on scalability for enterprise users.

6. **SAP Analytics Cloud**:
   - Combines BI, predictive analytics, and planning features in a single platform.
   - Strong integration with SAP systems.

7. **Sisense**:
   - Offers a full-stack BI solution with a focus on embedded analytics.
   - Known for handling large-scale datasets efficiently.

8. **IBM Cognos Analytics**:
   - Enterprise-grade BI tool with advanced reporting and analytics capabilities.

9. **Zoho Analytics**:
   - Affordable, user-friendly BI platform with extensive third-party integrations.

10. **Excel with Add-ins**:
    - For smaller-scale BI needs, Excel with Power Query, Power Pivot, and visualization add-ins can be a simple alternative.

---

### **When to Choose Power BI?**

Choose Power BI if:

- You are in a Microsoft ecosystem (e.g., using Excel, Azure, or SQL Server).
- You need a cost-effective solution for self-service BI.
- You value user-friendly interfaces for report creation and sharing.
- You need enterprise features like RLS, AI integration, or scheduled data refresh.

For advanced or unique requirements, Tableau or Looker may be better suited, while Google Data Studio is ideal for simpler, cost-effective projects.

## Data Modeling in Power BI

Data modeling is the process of designing how data tables relate to each other within Power BI. A well-structured data model ensures efficient querying, accurate results, and scalability for reporting. Here's a breakdown:

---

### **Core Principles of Data Modeling**

1. **Star Schema vs. Snowflake Schema**:
   - **Star Schema**:
     - Consists of a central fact table connected to multiple dimension tables.
     - Simple, intuitive, and optimized for performance in Power BI.
   - **Snowflake Schema**:
     - Dimension tables are normalized into multiple related tables.
     - Can lead to complex queries but reduces redundancy.

2. **Fact Tables**:
   - Store measurable, numeric data (e.g., sales, revenue, quantity).
   - Typically large tables with transactional or aggregated data.

3. **Dimension Tables**:
   - Contain descriptive attributes for slicing and dicing data (e.g., products, customers, dates).
   - Typically smaller and used as filters in reports.

4. **Relationships**:
   - Define how tables interact with one another.
   - Cardinality options:
     - **One-to-One (1:1)**: Uncommon but used for tables with unique mappings (e.g., user profiles).
     - **One-to-Many (1:N)**: Most common; dimension table relates to multiple rows in the fact table.
     - **Many-to-Many (M:N)**: Used for complex relationships, often via bridge tables.

5. **Filter Direction**:
   - **Single Direction**: Filters flow from one table (usually dimension) to another (fact table).
   - **Bidirectional**: Filters flow in both directions; useful in certain scenarios (e.g., many-to-many relationships) but can impact performance.

6. **Normalization vs. Denormalization**:
   - **Normalization**: Break data into multiple related tables to reduce redundancy.
   - **Denormalization**: Combine related tables into fewer, flatter tables for simplicity and performance.

---

### **Importance of Date Tables in Data Modeling**

Date tables are a critical component of a data model, especially when working with time-based data. They act as a dimension table specifically designed to support time intelligence calculations, filtering, and grouping.

#### **Why Date Tables Are Important**

1. **Time Intelligence Functions**:
   - Functions like `TOTALYTD`, `PREVIOUSYEAR`, `SAMEPERIODLASTYEAR`, and `PARALLELPERIOD` require a continuous date table.

2. **Multiple Date Columns**:
   - Fact tables often contain multiple date columns (e.g., OrderDate, ShipDate). A single date table allows consistent filtering across all these columns.

3. **Custom Calendars**:
   - Businesses often use fiscal calendars (e.g., starting in July). A date table can be customized for fiscal years, quarters, and other non-standard periods.

4. **Performance Optimization**:
   - Using a single, pre-calculated date table avoids repeated calculations and ensures consistency.

5. **Sorting and Grouping**:
   - Provides pre-defined fields for sorting (e.g., MonthKey) and grouping (e.g., Fiscal Quarter).

---

### **Building a Relationship with a Date Table**

1. **Create or Import a Date Table**:
   - Use DAX (`CALENDARAUTO` or `CALENDAR`) or import a date table from another source (e.g., Excel).

   Example:

   ```DAX
   DateTable = CALENDAR(DATE(2020, 1, 1), DATE(2030, 12, 31))
   ```

2. **Define Relationships**:
   - Connect the `Date` column in the date table to relevant date columns in fact tables (e.g., `Sales[OrderDate]`, `Sales[ShipDate]`).
   - Set the cardinality to **one-to-many** with the date table as the "one" side.

3. **Mark the Date Table**:
   - Power BI requires a table to be marked as a **Date Table** to enable time intelligence functions.
   - Go to `Modeling > Mark as Date Table`, and select the `Date` column.

4. **Leverage Calculated Columns**:
   - Add custom columns in the date table to support filtering and grouping.

   Examples:

   ```DAX
   Year = YEAR('DateTable'[Date])
   MonthName = FORMAT('DateTable'[Date], "MMMM")
   FiscalYear = "FY" & YEAR('DateTable'[Date]) + IF(MONTH('DateTable'[Date]) > 6, 1)
   ```

---

### **Example: Using a Date Table in a Star Schema**

#### **Schema**

- **Fact Table**: `Sales`
  - Columns: `OrderDate`, `ShipDate`, `Amount`
- **Dimension Table**: `Date`
  - Columns: `Date`, `Year`, `Quarter`, `MonthName`, `MonthKey`

#### **Relationships**

- Connect `Date[Date]` to `Sales[OrderDate]` (one-to-many).
- Connect `Date[Date]` to `Sales[ShipDate]` (one-to-many).
- Ensure single-directional filtering from `Date` to `Sales`.

#### **DAX Measure Example**

```DAX
SalesYTD = TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])
```

- This measure calculates year-to-date sales using the date table for filtering.

---

### **Scenarios That Require Date Tables**

1. **Fiscal Calendars**:
   - Businesses with fiscal years starting in months other than January.
   - Example:

     ```DAX
     FiscalYear = "FY" & YEAR('Date'[Date]) + IF(MONTH('Date'[Date]) > 6, 1)
     ```

2. **Time Period Comparisons**:
   - Comparing sales from the same period last year.
   - Example:

     ```DAX
     SalesLY = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR('Date'[Date]))
     ```

3. **Custom Grouping**:
   - Grouping months into seasons or custom periods.

4. **Multiple Date Columns**:
   - For tables with `OrderDate`, `ShipDate`, and `DueDate`, a single date table can relate to all columns for consistent filtering.

---

### **Best Practices for Data Modeling with Date Tables**

1. Always include a dedicated date table in your model.
2. Avoid relying on implicit date hierarchies; use explicit columns for Year, Quarter, etc.
3. Normalize your data where possible but prioritize simplicity (denormalize when it improves clarity).
4. Ensure the date table covers the full range of dates in your dataset.
5. Mark the date table in Power BI to unlock time intelligence features.

By integrating a date table into your data model, you gain robust capabilities for time-based analysis, enhancing both the accuracy and usability of your Power BI reports.

## Date tables

```DAX
Date = 
CALENDARAUTO(6)

Year = 
"FY" & YEAR('Date'[Date]) + IF(MONTH('Date'[Date]) > 6, 1)


Quarter = 
'Date'[Year] & " Q"
    & IF(
        MONTH('Date'[Date]) <= 3,
        3,
        IF(
            MONTH('Date'[Date]) <= 6,
            4,
            IF(
                MONTH('Date'[Date]) <= 9,
                1,
                2
            )
        )
    )


Month = 
FORMAT('Date'[Date], "yyyy MMM")

MonthKey = 
(YEAR('Date'[Date]) * 100) + MONTH('Date'[Date])
```

A date table is essential for time-based analysis, enabling features like filtering by years, quarters, months, and supporting time intelligence calculations.

Your code creates a Date table with calculated columns for fiscal year, fiscal quarter, month name, and a month key. This type of table is essential in Power BI for time intelligence calculations, as it provides structured and standardized date information.

### **Why Use a Date Table?**

1. Required for **time intelligence functions** in DAX.
2. Standardizes date hierarchies (Year, Quarter, Month, Day).
3. Allows for filtering, grouping, and sorting based on custom fiscal calendars.

### **When to Use a Date Table?**

- Anytime you need advanced date calculations (e.g., year-over-year comparisons, YTD totals, fiscal periods).

### **Your Date Table Example Explained**

1. **Date Table Definition**:

   ```DAX
   Date = CALENDARAUTO(6)
   ```

    - Generates a continuous date range based on existing data, assuming the fiscal year starts in July (6th month). Generates a date table with a range determined automatically from your model’s date fields.
    - The 6 specifies that the fiscal year starts in July. This means: Dates from July to June are grouped as a fiscal year. Example: July 2023 to June 2024 = Fiscal Year 2024.

2. **Fiscal Year Calculation**:

   ```DAX
   Year = "FY" & YEAR('Date'[Date]) + IF(MONTH('Date'[Date]) > 6, 1)
   ```

    - Creates a fiscal year label (e.g., FY2024).Creates a fiscal year column as a string (e.g., "FY2024").
    - Logic: Uses YEAR() to get the calendar year. Adds 1 to the year if the month is after June (MONTH('Date'[Date]) > 6). Ensures fiscal years align with the July-to-June period.

3. **Fiscal Quarter Calculation**:

   ```DAX
   Quarter = 'Date'[Year] & " Q" &
    IF(
        MONTH('Date'[Date]) <= 3, 3,
        IF(
            MONTH('Date'[Date]) <= 6, 4,
            IF(
                MONTH('Date'[Date]) <= 9, 1,
                2
            )
        )
    )
   ```

    - Assigns fiscal quarters based on months. Creates fiscal quarter labels (e.g., "FY2024 Q1").
    - Maps calendar months to fiscal quarters:
      - Jan–Mar → Q3
      - Apr–Jun → Q4
      - Jul–Sep → Q1
      - Oct–Dec → Q2

4. **Month Name**:

   ```DAX
   Month = FORMAT('Date'[Date], "yyyy MMM")
   ```

    - Outputs a readable month format (e.g., "2024 Jul"). Formats dates as "YYYY MMM" (e.g., "2023 Jul").
    - Helps with sorting and visualization of months.

5. **Month Key**:

   ```DAX
   MonthKey = (YEAR('Date'[Date]) * 100) + MONTH('Date'[Date])
   ```

    - Generates a unique integer key for sorting (e.g., 202407 for July 2024). Generates a numeric key for each month (e.g., 202307 for July 2023).
    - Useful for sorting months chronologically, especially in visuals.

### **What Could You Have Done Differently?**

#### **1. Use `SWITCH` for Fiscal Quarter**

Instead of nested `IF` statements, use `SWITCH` for readability:

```DAX
Quarter =
'Date'[Year] & " Q" &
SWITCH(
    TRUE(),
    MONTH('Date'[Date]) <= 3, 3,
    MONTH('Date'[Date]) <= 6, 4,
    MONTH('Date'[Date]) <= 9, 1,
    2
)
```

#### **2. Leverage Fiscal Functions for Simplicity**

Power BI has built-in **time intelligence** functions that simplify fiscal calculations. For example:

- Mark your Date table as a "Date Table" and use its `FiscalYearStartMonth` property.
- These built-in features reduce the need for manual fiscal year/quarter logic.

#### **3. Optimize Date Table Creation**

- Instead of `CALENDARAUTO`, explicitly define the range for better control:

```DAX
Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2020, 7, 1), DATE(2030, 6, 30)),
    "Year", "FY" & YEAR([Date]) + IF(MONTH([Date]) > 6, 1),
    "Quarter", "Q" & FORMAT(MONTH([Date]) + 3, "0"),
    "Month", FORMAT([Date], "yyyy MMM"),
    "MonthKey", YEAR([Date]) * 100 + MONTH([Date])
)
```

#### **4. Use Numeric Fiscal Year Instead of Text**

If you plan to sort or filter fiscal years in visuals, numeric fiscal years are better:

```DAX
FiscalYear = YEAR('Date'[Date]) + IF(MONTH('Date'[Date]) > 6, 1)
```

#### **5. Automate Sorting for `Month`**

The `Month` column (`"yyyy MMM"`) may not sort correctly if used in visuals. Create a numeric column (`MonthKey`) and set it as the sort column:

- Go to `Model View` in Power BI.
- Select the `Month` column.
- Set **Sort by Column** to `MonthKey`.

---

### **Why These Adjustments?**

1. **Improved Readability**: Using `SWITCH` and concise formulas enhances code clarity and reduces errors.
2. **Explicit Control**: Specifying the date range avoids surprises with `CALENDARAUTO` (e.g., pulling unintended date ranges).
3. **Optimized Performance**: Avoid unnecessary columns or calculations.
4. **Better Visual Sorting**: Ensures visuals display months or quarters in the correct order.
5. **Time Intelligence Integration**: By marking the Date table properly, you can leverage Power BI’s time intelligence functions for calculations like YTD, QTD, etc., without manual work.

## DAX

DAX (Data Analysis Expressions) is a formula language in Power BI, Power Pivot, and Analysis Services. It is designed for working with relational data and performing complex calculations within a data model. Below is a detailed review of DAX, its components, key features, and advanced use cases.

---

### **Core Features of DAX**

1. **Tabular Data Modeling**:
   - Works seamlessly with tables and relationships in Power BI's data model.
   - Designed for aggregations, filtering, and advanced analytics.

2. **Calculated Columns**:
   - Add new columns to tables using row-based operations.
   - Calculated once and stored in the model.
   - Example:

     ```DAX
     Profit = Sales[Revenue] - Sales[Cost]
     ```

3. **Measures**:
   - Perform dynamic calculations in visualizations based on user interaction.
   - Calculated on-the-fly and optimized for performance.
   - Example:

     ```DAX
     TotalSales = SUM(Sales[Amount])
     ```

4. **Row and Filter Context**:
   - **Row Context**: Operates on each row of a table, similar to Excel row operations.
   - **Filter Context**: Determines what subset of data is visible for a calculation.

5. **Time Intelligence**:
   - Enables calculations like year-to-date (YTD), same-period-last-year (SPY), rolling averages, etc.
   - Requires a properly structured and marked Date table.

---

### **Key Functions in DAX**

#### **Aggregation Functions**

- Perform operations over a table or column.
- Examples:

  ```DAX
  TotalSales = SUM(Sales[Amount])
  AveragePrice = AVERAGE(Products[Price])
  ```

#### **Logical Functions**

- Allow conditional logic within calculations.
- Examples:

  ```DAX
  HighSales = IF(Sales[Amount] > 1000, "High", "Low")
  ```

#### **Date and Time Functions**

- Support operations on dates, including custom fiscal calendars.
- Examples:

  ```DAX
  Year = YEAR(Date[Date])
  StartOfMonth = STARTOFMONTH(Date[Date])
  ```

#### **Text Functions**

- Manipulate text strings.
- Examples:

  ```DAX
  FullName = CONCATENATE(Employees[FirstName], Employees[LastName])
  MonthName = FORMAT(Date[Date], "MMMM")
  ```

#### **Filter and Context Modifier Functions**

- Modify or apply filters dynamically.
- Examples:

  ```DAX
  TotalSalesForRegion = CALCULATE(SUM(Sales[Amount]), Region[Name] = "East")
  AllSales = CALCULATE(SUM(Sales[Amount]), ALL(Region))
  ```

#### **Table Manipulation Functions**

- Work with entire tables or subsets of tables.
- Examples:

  ```DAX
  FilteredSales = FILTER(Sales, Sales[Amount] > 100)
  TopProducts = TOPN(5, Products, Products[Sales], DESC)
  ```

#### **Iterator Functions**

- Iterate row-by-row and aggregate results.
- Examples:

  ```DAX
  WeightedAverage = SUMX(Products, Products[Price] * Products[Quantity])
  ```

---

### **Advanced DAX Concepts**

#### 1. **Row Context vs. Filter Context**

- **Row Context**: Active when calculated columns or iterators (`SUMX`, `FILTER`) operate on individual rows.
- **Filter Context**: Created by slicers, filters, and DAX functions like `CALCULATE`.

   **Example**:

   ```DAX
   RevenuePerProduct = SUM(Sales[Revenue]) / COUNTROWS(Sales)
   ```

- Row context evaluates each product’s revenue.
- Filter context applies only to visible products in the report.

---

#### 2. **CALCULATE: The Most Powerful Function**

- Modifies filter context and allows custom aggregations.

   **Examples**:

- Calculate total sales for a specific product:

     ```DAX
     SalesForProductA = CALCULATE(SUM(Sales[Amount]), Products[Name] = "Product A")
     ```

- Apply multiple filters:

     ```DAX
     SalesIn2024 = CALCULATE(SUM(Sales[Amount]), Year(Date[Date]) = 2024, Region[Name] = "North")
     ```

---

#### 3. **Time Intelligence Functions**

- Use marked Date tables for calculations over time.

   **Examples**:

- Year-to-date sales:

     ```DAX
     SalesYTD = TOTALYTD(SUM(Sales[Amount]), Date[Date])
     ```

- Same period last year:

     ```DAX
     SalesLY = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR(Date[Date]))
     ```

- Rolling 3-month average:

     ```DAX
     RollingAvg = AVERAGEX(DATESINPERIOD(Date[Date], LASTDATE(Date[Date]), -3, MONTH), SUM(Sales[Amount]))
     ```

---

#### 4. **Dynamic Measures**

- React to user interactions in visualizations.

   **Example**:

   ```DAX
   SalesByRegion = SWITCH(
       SELECTEDVALUE(Region[Name]),
       "North", SUM(Sales[Amount]),
       "South", SUM(Sales[Amount]) * 0.9,
       SUM(Sales[Amount])
   )
   ```

---

#### 5. **Performance Optimization**

- Minimize calculated columns; prefer measures.
- Use `SUMX`, `FILTER`, and `ALL` judiciously to control filter propagation.
- Use `Variables` to simplify and optimize formulas:

     ```DAX
     OptimizedMeasure = 
     VAR TotalRevenue = SUM(Sales[Revenue])
     VAR TotalCost = SUM(Sales[Cost])
     RETURN TotalRevenue - TotalCost
     ```

---

### **Common DAX Challenges and Solutions**

#### **1. Context Transition**

- **Challenge**: When a row context automatically converts to filter context (e.g., using `CALCULATE` in a calculated column).
- **Solution**: Use functions like `RELATED` to explicitly define the relationship.

#### **2. Many-to-Many Relationships**

- **Challenge**: Complex relationships may lead to ambiguous calculations.
- **Solution**: Use bridge tables and the `CROSSFILTER` function for explicit control.

#### **3. Circular Dependencies**

- **Challenge**: Occurs when calculated columns or measures reference each other cyclically.
- **Solution**: Reorganize the logic to eliminate circular references.

---

### **DAX vs. Excel Formulas**

| Feature           | DAX                                         | Excel Formulas                         |
|--------------------|---------------------------------------------|----------------------------------------|
| **Scope**          | Works on entire tables and relationships   | Works on individual cells              |
| **Performance**    | Optimized for large datasets               | Limited to smaller datasets            |
| **Time Intelligence** | Built-in support for date-based calculations | Requires manual setup                 |
| **Data Context**   | Operates within the model’s row and filter context | Works only in the current worksheet |

---

### **Best Practices for Writing DAX**

1. **Understand Context**:
   - Always consider row and filter context when writing formulas.

2. **Use Measures Over Calculated Columns**:
   - Measures are dynamic and more efficient for aggregations.

3. **Optimize Filter Context**:
   - Use `CALCULATE` and `ALL` carefully to modify filters only when necessary.

4. **Leverage Variables**:
   - Simplify complex calculations and enhance performance with variables.

5. **Mark a Proper Date Table**:
   - Essential for using time intelligence functions effectively.

6. **Debug and Validate**:
   - Use tools like `Performance Analyzer` and `DAX Studio` to debug and optimize DAX queries.

---

### **Conclusion**

DAX is a powerful and versatile language for advanced analytics in Power BI. It provides capabilities to handle aggregations, filtering, time intelligence, and dynamic calculations in a highly optimized way. Mastering DAX requires understanding its core concepts (row and filter context), using its rich library of functions, and following best practices to build efficient and accurate data models.

## DAX - common functions

Here’s a breakdown of common DAX expressions with examples for key functions like `FILTER`, `TOPN`, `CONCATENATEX`, and others. These are useful in various scenarios for filtering data, ranking, aggregating, and creating calculated measures or columns.

---

### **1. FILTER**

The `FILTER` function is used to return a subset of a table based on specific conditions.

#### **Example: Filter Sales Greater Than $1000**

```DAX
FilteredSales = 
SUMX(
    FILTER(
        'Sales',
        'Sales'[Amount] > 1000
    ),
    'Sales'[Amount]
)
```

- Filters the `Sales` table to include only rows where the `Amount` column is greater than 1000.
- Sums the amounts from the filtered table.

---

### **2. TOPN**

The `TOPN` function returns the top N rows of a table based on a ranking criterion.

#### **Example: Top 3 Products by Sales**

```DAX
Top3Products = 
TOPN(
    3,
    SUMMARIZE(
        'Sales',
        'Product'[ProductName],
        "TotalSales", SUM('Sales'[Amount])
    ),
    [TotalSales],
    DESC
)
```

- Finds the top 3 products with the highest total sales.
- Uses `SUMMARIZE` to create a temporary table with product names and their total sales.
- Orders by `TotalSales` in descending order.

---

### **3. CONCATENATEX**

The `CONCATENATEX` function concatenates values from a table into a single string, optionally separated by a delimiter.

#### **Example: List All Products**

```DAX
AllProducts = 
CONCATENATEX(
    'Product',
    'Product'[ProductName],
    ", "
)
```

- Produces a single string with all product names separated by commas (e.g., `"Product A, Product B, Product C"`).

#### **Example: List Top 3 Products by Sales**

```DAX
Top3ProductNames = 
CONCATENATEX(
    TOPN(
        3,
        SUMMARIZE(
            'Sales',
            'Product'[ProductName],
            "TotalSales", SUM('Sales'[Amount])
        ),
        [TotalSales],
        DESC
    ),
    'Product'[ProductName],
    ", "
)
```

- Combines `TOPN` and `CONCATENATEX` to list the top 3 product names in a single string.

---

### **4. ALL**

The `ALL` function removes all filters from a column or table.

#### **Example: Calculate Sales Percentage of Total**

```DAX
SalesPctOfTotal = 
DIVIDE(
    SUM('Sales'[Amount]),
    CALCULATE(
        SUM('Sales'[Amount]),
        ALL('Sales')
    )
)
```

- Divides the sales amount for the current filter context by the total sales across all rows in the `Sales` table.

---

### **5. RELATED**

The `RELATED` function retrieves values from related tables (via relationships).

#### **Example: Bring Category into Sales Table**

```DAX
ProductCategory = 
RELATED('ProductCategory'[CategoryName])
```

- Retrieves the category name for each product in the `Sales` table, assuming there's a relationship between `Sales` and `ProductCategory`.

---

### **6. RANKX**

The `RANKX` function ranks values in a table based on a specific measure or column.

#### **Example: Rank Products by Sales**

```DAX
ProductRank = 
RANKX(
    ALL('Product'),
    SUM('Sales'[Amount]),
    ,
    DESC
)
```

- Ranks products by their total sales in descending order.

---

### **7. CALCULATE**

The `CALCULATE` function modifies the filter context for a calculation.

#### **Example: Sales for a Specific Region**

```DAX
SalesInNorth = 
CALCULATE(
    SUM('Sales'[Amount]),
    'Region'[RegionName] = "North"
)
```

- Sums the sales where the region is `"North"`.

---

### **8. DISTINCT**

The `DISTINCT` function returns a unique list of values from a column.

#### **Example: Count Unique Products**

```DAX
UniqueProducts = 
COUNTROWS(
    DISTINCT('Sales'[ProductID])
)
```

- Counts the number of unique products in the `Sales` table.

---

### **9. SUMMARIZE**

The `SUMMARIZE` function creates a table grouped by specific columns with calculated measures.

#### **Example: Total Sales by Region**

```DAX
SalesByRegion = 
SUMMARIZE(
    'Sales',
    'Region'[RegionName],
    "TotalSales", SUM('Sales'[Amount])
)
```

- Groups sales by region and calculates the total sales for each region.

---

### **10. TIME INTELLIGENCE FUNCTIONS**

#### **Example: Year-to-Date Sales**

```DAX
YTD_Sales = 
TOTALYTD(
    SUM('Sales'[Amount]),
    'Date'[Date]
)
```

- Calculates the year-to-date sales using the `Date` table.

#### **Example: Same Period Last Year Sales**

```DAX
SalesLastYear = 
CALCULATE(
    SUM('Sales'[Amount]),
    SAMEPERIODLASTYEAR('Date'[Date])
)
```

- Calculates sales for the same period in the previous year.

---

### **Putting It All Together: A Real-World Example**

#### **Top 3 Products in North America with Sales Percentage**

```DAX
Top3ProductsSalesPct = 
CALCULATE(
    DIVIDE(
        SUM('Sales'[Amount]),
        CALCULATE(
            SUM('Sales'[Amount]),
            ALL('Sales')
        )
    ),
    TOPN(
        3,
        SUMMARIZE(
            'Sales',
            'Product'[ProductName],
            "TotalSales", SUM('Sales'[Amount])
        ),
        [TotalSales],
        DESC
    ),
    'Region'[RegionName] = "North America"
)
```

This measure combines `CALCULATE`, `TOPN`, and other functions to calculate the percentage of total sales contributed by the top 3 products in North America.

## DAX example - 3-month moving average

To calculate a **3-month moving average of sales** in Power BI using DAX, you can create a **measure** that dynamically calculates the average sales over the past three months.

A measure is a model object that is designed to summarize data. Measure formulas, which are written in Data Analysis Expressions (DAX), can modify filter context by using the CALCULATE or CALCULATETABLE functions. These functions are powerful and provide you with the flexibility to add, remove, or modify filters. A set of DAX functions, known as time intelligence functions, also modify filter context. These functions can override any filters that are applied to the report structure.

---

### **DAX Code for 3-Month Moving Average**

```DAX
ThreeMonthMovingAverage = 
AVERAGEX(
    DATESINPERIOD(
        'Date'[Date], 
        MAX('Date'[Date]), 
        -3, 
        MONTH
    ),
    [Total Sales]
)
```

You don't need to wrap AVERAGEX in CALCULATE for the 3-month moving average because AVERAGEX already operates within the filter context defined by DATESINPERIOD.

---

### **Explanation**

1. **`DATESINPERIOD`**:
   - Creates a dynamic range of dates from the `Date` table.
   - Starts at the latest date in the current filter context (`MAX('Date'[Date])`).
   - Includes dates from 3 months prior to the latest date (`-3`, `MONTH`).

2. **`AVERAGEX`**:
   - Iterates over the date range returned by `DATESINPERIOD`.
   - Calculates the average value of the measure `[Total Sales]` over this date range.

3. **`[Total Sales]`**:
   - Replace this with the measure or column representing your sales data.
   - Example: If your sales column is named `Sales`, you could define `Total Sales` as:

     ```DAX
     Total Sales = SUM('Sales'[Sales Amount])
     ```

---

### **Steps to Implement in Power BI**

1. Ensure you have a **Date table** in your model, marked as a Date Table.
2. Create the **Total Sales** measure (if it doesn't already exist).

   ```DAX
   Total Sales = SUM('Sales'[Sales Amount])
   ```

3. Create the **3-Month Moving Average** measure using the DAX code above.
4. Add the **ThreeMonthMovingAverage** measure to your visuals, such as line charts or tables.

---

### **Alternative with CALCULATE**

If you prefer to use `CALCULATE`:

```DAX
ThreeMonthMovingAverage = 
CALCULATE(
    AVERAGE('Sales'[Sales Amount]),
    DATESINPERIOD(
        'Date'[Date], 
        MAX('Date'[Date]), 
        -3, 
        MONTH
    )
)
```

Both versions achieve the same result, but `AVERAGEX` provides more flexibility for complex calculations.

If you need to apply additional conditions, such as filtering by region or product category, you can use `CALCULATE`

```DAX
ThreeMonthMovingAverage =
CALCULATE(
    AVERAGEX(
        DATESINPERIOD(
            'Date'[Date],
            MAX('Date'[Date]),
            -3,
            MONTH
        ),
        [Total Sales]
    ),
    'Region'[Region] = "North America"
)
```

This measure calculates the 3-month moving average for sales only in North America

---

### **Example Use Case**

- You might use this measure in a **line chart** to visualize the trend of the 3-month moving average of sales.
- It smooths out fluctuations, helping you identify long-term trends.

---

### **Extending the Logic**

1. **Custom Time Periods**:
   - Replace `-3` and `MONTH` with other intervals (e.g., days, quarters).
   - For a 6-month moving average, change `-3` to `-6`.

2. **Weighted Moving Average**:
   - Apply a weighted average instead of a simple average:

     ```DAX
     WeightedMovingAverage = 
     SUMX(
         DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -3, MONTH),
         [Total Sales] * 'Date'[Weight]
     ) / SUM('Date'[Weight])
     ```

This provides a versatile foundation for advanced analytics in Power BI.

## Power Query

Power Query is a data transformation and preparation tool integrated into Power BI, Excel, and other Microsoft products. It simplifies the process of connecting to, cleaning, transforming, and loading data for analysis and visualization. Power Query operates on the **ETL (Extract, Transform, Load)** paradigm, enabling users to handle data from diverse sources with minimal coding.

---

### **Key Features of Power Query**

1. **Data Connectivity**:
   - Power Query supports connections to various data sources, including databases (SQL Server, PostgreSQL), files (Excel, CSV, JSON), web APIs, and cloud services (Azure, SharePoint, etc.).
   - Supports direct import or live connections.

2. **Query Editor**:
   - A user-friendly interface for data transformation.
   - Provides tools for filtering, sorting, merging, appending, and shaping data without writing code.

3. **Transformation Capabilities**:
   - Rich set of built-in operations, such as removing duplicates, pivoting/unpivoting, splitting columns, replacing values, and creating calculated columns.
   - Supports advanced transformations using the **M language**.

4. **Reusable Queries**:
   - Queries can be parameterized and reused, allowing dynamic adjustments without rewriting logic.

5. **Integration**:
   - Tight integration with Power BI and Excel.
   - Allows exporting transformed data into Power BI models or Excel tables.

6. **Incremental Refresh**:
   - Power Query supports incremental refresh, enabling efficient updates for large datasets.

---

### **Power Query Workflow**

1. **Extract (E)**:
   - Connect to a data source (e.g., SQL database, JSON file, API).
   - Example: Importing a CSV file.
     - Go to `Get Data` > `Text/CSV` > Select your file.

2. **Transform (T)**:
   - Clean and shape the data to meet your requirements.
   - Common transformations:
     - Removing unnecessary columns.
     - Replacing null values.
     - Splitting or merging columns.
     - Filtering rows.

3. **Load (L)**:
   - Save the transformed data to a destination (e.g., Power BI model or Excel worksheet).

---

### **Core Transformation Capabilities**

#### **1. Filtering and Sorting**

- Remove unnecessary rows or filter data based on conditions.
- Example: Filter for orders where the `Amount` > 1000.

#### **2. Column Operations**

- Add, rename, split, merge, or delete columns.
- Example: Combine `FirstName` and `LastName` columns into `FullName`.

#### **3. Pivot and Unpivot**

- **Pivot**: Transform rows into columns for cross-tabulation.
- **Unpivot**: Flatten data by converting columns into rows.
- Example:
  - Pivoting monthly sales data to show each month as a column.

#### **4. Group By**

- Aggregate data by grouping on one or more columns.
- Example: Sum `Sales` grouped by `Region`.

#### **5. Data Type Transformation**

- Convert columns to appropriate data types (e.g., Date, Integer, Text).

#### **6. Merge and Append Queries**

- **Merge**: Join tables based on a common key.
- **Append**: Combine tables with the same structure into one.

#### **7. Conditional Columns**

- Add calculated columns based on custom logic.
- Example:
  - Create a column `HighSales` where `Sales > 5000`.

#### **8. Replace Values**

- Replace nulls or specific values with defaults or other values.

---

### **The M Language in Power Query**

Power Query uses the **M language** under the hood, a case-sensitive, functional programming language. The Query Editor generates M code automatically, but users can customize it for more advanced scenarios.

#### **Key Features of M**

- Functional, row-based language.
- Can be edited directly in the Advanced Editor.
- Supports custom functions, parameters, and complex logic.

#### **Example M Code**: Remove Rows with Null Values

```M
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("...", BinaryEncoding.Base64), Compression.Deflate)), ...),
    RemovedNullRows = Table.SelectRows(Source, each ([ColumnName] <> null))
in
    RemovedNullRows
```

---

### **Common Use Cases for Power Query**

1. **Data Cleaning**:
   - Removing duplicates.
   - Standardizing formats (e.g., dates, currencies).

2. **Data Transformation**:
   - Reshaping data for analysis.
   - Aggregating or splitting datasets.

3. **Merging and Consolidating Data**:
   - Joining multiple datasets from different sources.

4. **Handling Complex Files**:
   - Importing and transforming nested JSON or XML files.

5. **Parameterization**:
   - Using parameters to dynamically adjust query behavior (e.g., filter by a specific region or date).

---

### **Advanced Power Query Features**

#### **1. Parameters**

- Create dynamic queries by defining parameters.
- Example: Use a parameter to select the source file path.

#### **2. Custom Functions**

- Write reusable functions for repetitive tasks.
- Example:

  ```M
  CustomFunction = (input as text) => Text.Upper(input)
  ```

#### **3. Nested Queries**

- Use queries as intermediate steps to build complex transformations.
- Example:
  - Query 1: Clean raw data.
  - Query 2: Aggregate cleaned data.

#### **4. Error Handling**

- Use `try ... otherwise` to handle errors gracefully.
- Example:

  ```M
  try Table.AddColumn(..., each ...)
  otherwise null
  ```

#### **5. Incremental Refresh**

- Enable refresh for large datasets by refreshing only new or changed data.

---

### **Power Query in Power BI vs. Excel**

| Feature                      | Power BI                             | Excel                                |
|------------------------------|---------------------------------------|--------------------------------------|
| **Primary Use**               | ETL for Power BI data models         | Data cleaning and preparation        |
| **Output**                    | Loads data into Power BI model       | Loads data into Excel worksheets     |
| **Integration with Visuals**  | Tightly integrated with Power BI visuals | Limited visual reporting             |
| **Performance**               | Optimized for large datasets         | Suitable for smaller datasets        |

---

### **Power Query vs. DAX**

| Feature                     | Power Query                              | DAX                                   |
|-----------------------------|------------------------------------------|---------------------------------------|
| **Purpose**                  | Data transformation and preparation     | Data analysis and aggregation         |
| **Stage**                    | Pre-load (ETL)                         | Post-load (reporting and modeling)    |
| **Scope**                    | Works on raw data                      | Works on loaded data models           |
| **Language**                 | M                                      | DAX                                   |
| **Flexibility**              | Handles complex transformations         | Handles dynamic calculations          |

---

### **Best Practices for Power Query**

1. **Keep Queries Modular**:
   - Break transformations into multiple steps for clarity.

2. **Minimize Load Time**:
   - Remove unnecessary columns and rows before loading data.

3. **Use Parameters**:
   - Make queries reusable and dynamic.

4. **Optimize Data Types**:
   - Ensure columns have the correct data types for efficient processing.

5. **Document Queries**:
   - Use descriptive step names and comments in M code.

6. **Reduce Complexity**:
   - Perform heavy transformations in the source system (e.g., database) when possible.
