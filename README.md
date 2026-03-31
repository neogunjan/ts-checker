**ts-checker** is a lightweight python library for validating, profiling, and monitoring time series datasets in analytics pipelines.

This tool can be used by data scientists and engineers to validate time-series data used in analytics workflows. The tool will reduce the risk of incorrect insights from unexpected data which can lead to pipeline breaks and wrong business decisions.

Core features (v1):
1. Basic time-series validations (duplicate timestamps, gaps)
2. Detect missing values
3. Generate simple data quality summaries
4. Detect anomalous values via configurable thresholds


Example usage:
```python
from ts_checker import detect_threshold_outliers

outliers = detect_threshold_outliers(df, column="value", threshold=500, outliers="above")
outlier_count = outliers.sum()
print(f"Outliers detected: {outlier_count}") 