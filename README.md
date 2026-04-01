**_ts-checker_** is a lightweight python library for validating, profiling, and monitoring time series datasets in analytics pipelines.

This tool can be used by data scientists and engineers to validate time-series data used in analytics workflows. The tool will reduce the risk of incorrect insights from unexpected data which can lead to pipeline breaks and wrong business decisions.

### Core features (v1):
1. Basic time-series validations (duplicate timestamps, gaps)
2. Detect missing values
3. Generate simple data quality summaries
4. Detect anomalous values via configurable thresholds

### Example usage:
```python
from ts_checker import detect_threshold_outliers

outliers = detect_threshold_outliers(df, column="value", threshold=500, direction="above")
outlier_count = outliers.sum()
print(f"Outliers detected: {outlier_count}")
```

# API Concept
- `validate_timestamps(df: pd.DataFrame, timestamp_column: str) -> dict`
Checks for duplicate timestamps and gaps in the data returning a dict with T/F values.

- `detect_missing_values(df: pd.DataFrame, column: str) -> pd.Series`
Checks for missing values in dataset, returning a series of T/F.

- `data_summary(df: pd.DataFrame, timestamp_column: str, value_columns: list[str]) -> dict`
Summarizes the columns of interest in a dataframe returning a dictionary with 3 keys:
    * _num_timestamp_duplicates_
    * _num_timestamp_gaps_
    * _columns_with_missing_values_

- `detect_threshold_outliers(df: pd.DataFrame, column: str, threshold: float, direction: str) -> pd.Series`
Checks for outliers above/below a certain threshold value, returning a series of T/F.