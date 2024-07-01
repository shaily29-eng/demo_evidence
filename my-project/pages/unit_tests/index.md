```sql database1_tests
SELECT module, AVG(duration) AS avg_duration
FROM test_database.test_data1
GROUP BY module
ORDER BY avg_duration DESC
LIMIT 5;
```


```sql database2_tests
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


```sql database3_tests
SELECT
    status,
    COUNT(*) AS num_tests,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM test_database.test_data1) AS percentage
FROM test_database.test_data1
GROUP BY status
ORDER BY percentage DESC;
```

<!-- test_database.test_data1 -->
