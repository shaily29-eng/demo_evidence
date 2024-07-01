---
title: Welcome to Evidence
---

<Details title='How to edit this page'>
  This page can be found in your project at `/pages/index.md`. Make a change to the markdown file and save it to see the change take effect in your browser.
</Details>

```sql test_database
  select
      id
  from test_database.test_data1
  group by id
```

```sql database1_tests
  select
      time
  from database1.table2
  group by time
```

```sql categories1
select category
from needful_things.orders
  group by category
```

<Dropdown data={categories1} name=category value=category>
    <DropdownOption value="%" valueLabel="All Categories"/>
</Dropdown>

<Dropdown name=year>
    <DropdownOption value=% valueLabel="All Years"/>
    <DropdownOption value=2019/>
    <DropdownOption value=2020/>
    <DropdownOption value=2021/>
</Dropdown>

<!-- test_database.test_data -->

```sql Tests_over_Time
SELECT
    date,
    COUNT(*) AS num_tests,
    SUM(duration) AS total_duration,
    AVG(duration) AS avg_duration,
    MIN(duration) AS min_duration,
    MAX(duration) AS max_duration
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

<BarChart
    data={Tests_over_Time}
    title="Bar Chart"
    x="date"
    y="avg_duration"
    tooltip="module, name, file, doc, message"
/>

<ScatterPlot
    data={Tests_over_Time}  
    title="Scatter Plot"
    x="date"                  
    y="avg_duration"             
    xFmt="date"            
/>

<DataTable 
data={Tests_over_Time}
/>

```sql Unit_Tests
SELECT
    date,
    SUM(duration) AS total_duration,
    COUNT(*) AS num_tests
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

<AreaChart
    data={Unit_Tests}
    x="date"
    y="num_tests"
    xLabel="Date"
    yLabel="Number of Tests"
    tooltip="Num Tests"
/>

```sql Unit_Tests1
SELECT
    date,
    SUM(duration) AS total_duration,
    COUNT(*) AS num_tests
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

<LineChart
    data={Unit_Tests1}
    y="total_duration"
    title="Total Duration of Tests by Month"
/>


