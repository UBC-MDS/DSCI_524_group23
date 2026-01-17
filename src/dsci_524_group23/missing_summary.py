import pandas as pd


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize missing values in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with one row per column and the following columns:
        - "column": original column name
        - "missing_count": number of missing values (NaN/None)
        - "missing_pct": percentage of missing values (0 to 100)

        The result is sorted by "missing_count" (descending), then "column" (ascending).

    Raises
    ------
    TypeError
        If df is not a pandas DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    total_rows = len(df)

    missing_count = df.isna().sum()

    if total_rows == 0:
        missing_pct = missing_count.astype(float) * 0.0
    else:
        missing_pct = (missing_count / total_rows) * 100.0

    out = pd.DataFrame(
        {
            "column": missing_count.index.astype(str),
            "missing_count": missing_count.values.astype(int),
            "missing_pct": missing_pct.values.astype(float),
        }
    )

    out = out.sort_values(by=["missing_count", "column"], ascending=[False, True]).reset_index(
        drop=True
    )
    return out
