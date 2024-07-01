```sql database1_tests
  select
      date
  from test_database.test_data1
  group by date
```

```sql Unit_Tests2
SELECT
    date,
    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) AS num_failures,
    COUNT(*) AS total_tests,
    SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS failure_rate_percentage
FROM test_database.test_data1
GROUP BY date
ORDER BY date;
```

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
