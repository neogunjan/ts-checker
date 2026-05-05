import pandas as pd

def detect_missing_values(df: pd.DataFrame, column: str) -> pd.Series:
    """Return a boolean Series indicating missing values in a specified column.

    Args:
        df (pd.DataFrame): df
        column (str): column to perform check on

    Returns:
        pd.Series: bool values where True means missing
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")

    return df[column].isna()