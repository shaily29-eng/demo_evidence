<h1 align="center">
    Demo on Evidence
</h1>

![image](https://github.com/shaily29-eng/demo_evidence/assets/59019087/854e5e13-9577-4c25-8ad7-05224edb1273)


### Tools and Technologies:

- Python (for unit tests)
- CSV (for data storage and handling)
- DuckDB (for data storage and querying)
- Evidence (for reporting and data visualization)

### Running Locally:
 ```shell
cd my-project
npm install
npm run sources
npm run dev
  ```

## Reference- Intermediate Steps Commands:

### Running Coverage Reports of Unit Tests:
 ```shell
cd unit_tests
coverage run -m unittest discover -s . -p 'test_*.py'
coverage report -m
  ```

### Py files to CSV:
 ```shell
cd unit_tests
pip install pytest pytest-csv
pytest --csv=test_report.csv
  ```

### CSV to DuckDB:
 ```shell
pip install duckdb
python import_csv_to_duckdb.py 
  ```
Hence, this creates my_duckdb_data.db (database file)

### To view tables in DuckDB:
 ```shell
cd my-project
cd my-project/sources/test_database
duckdb
.open my_duckdb_data.db
show tables;

  ```



